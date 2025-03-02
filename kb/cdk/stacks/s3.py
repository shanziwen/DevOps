from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_iam as iam,
)
from constructs import Construct


class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 Bucket for Site Hosting
        self.mkdocs_s3 = s3.Bucket(
            self,
            "MkdocsS3",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            bucket_name=f"prod-{self.region}-mkdocs",
            enforce_ssl=True,
        )

        self.mkdocs_s3.add_to_resource_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                principals=[iam.ServicePrincipal(service="cloudfront.amazonaws.com")],
                resources=[self.mkdocs_s3.arn_for_objects("*")],
            )
        )

        # Upload Site Static Resources to S3
        self.mkdocs_site = s3_deployment.BucketDeployment(
            self,
            "MkdocsSite",
            destination_bucket=self.mkdocs_s3,
            sources=[
                s3_deployment.Source.asset(
                    path="../site",
                )
            ],
        )
