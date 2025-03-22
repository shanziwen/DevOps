from aws_cdk import (
    Stack,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as cloudfront_origins,
    aws_route53 as r53,
    aws_certificatemanager as acm,
    aws_lambda as _lambda,
)
from constructs import Construct


class CloudFrontStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, s3_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Cloudfront Distribution
        self.domain_cert = acm.Certificate.from_certificate_arn(
            self, "DomainCertificate", self.node.try_get_context("acm_arn")
        )
        self.primary_domain = self.node.try_get_context("primary_domain")
        self.sub_domain = "kb"

        self.domain = f"{self.sub_domain}.{self.primary_domain}"
        self.mkdocs_origin_access_control = cloudfront.S3OriginAccessControl(
            self,
            "MkdocsS3OriginAccessIdentity",
            origin_access_control_name=f"mkdocs-origin-access-control",
        )
        with open("lambdas/origin_request.py", "r") as origin_request_lambda_code:

            self.lambda_edge_func = _lambda.Function(
                self,
                "MkdocsOriginRequestLambdaEdgeFunc",
                code=_lambda.Code.from_inline(origin_request_lambda_code.read()),
                runtime=_lambda.Runtime.PYTHON_3_13,
                architecture=_lambda.Architecture.X86_64,
                handler="index.handler",
            )

        self.mkdocs_cloudfront_distro = cloudfront.Distribution(
            self,
            "MkdocsCloudFrontDistro",
            default_behavior=cloudfront.BehaviorOptions(
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD_OPTIONS,
                cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD_OPTIONS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                origin=cloudfront_origins.S3BucketOrigin(
                    bucket=s3_stack.mkdocs_s3,
                    origin_access_control_id=self.mkdocs_origin_access_control.origin_access_control_id,
                ),
                origin_request_policy=cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                edge_lambdas=[
                    cloudfront.EdgeLambda(
                        event_type=cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST,
                        function_version=self.lambda_edge_func.current_version,
                        include_body=False,
                    )
                ],
            ),
            certificate=self.domain_cert,
            default_root_object="index.html",
            enabled=True,
            domain_names=[self.domain],
            error_responses=[
                cloudfront.ErrorResponse(
                    http_status=404,
                    response_http_status=404,
                    response_page_path="/404.html",
                )
            ],
        )

        # Add Route53 Domain
        self.mkdocs_domain_record = r53.CnameRecord(
            self,
            "MkdocsDomainRecord",
            domain_name=self.mkdocs_cloudfront_distro.distribution_domain_name,
            zone=r53.HostedZone.from_lookup(
                self,
                "HostedZone",
                domain_name=self.primary_domain,
            ),
            record_name=self.sub_domain,
        )
