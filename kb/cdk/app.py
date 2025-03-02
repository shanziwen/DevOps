#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.s3 import S3Stack
from stacks.cloudfront import CloudFrontStack


app = cdk.App()
s3_stack = S3Stack(
    app,
    "MkdocsS3Stack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)
CloudFrontStack(
    app,
    "MkdocsCloudFrontStack",
    env=cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region="us-east-1"),
    cross_region_references=True,
    s3_stack=s3_stack,
)

app.synth()
