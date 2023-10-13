#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stack.simple_async_workflow import SimpleAsyncWorkflow

app = cdk.App()
SimpleAsyncWorkflow(app, "SimpleAsyncWorkflow", env=cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]))

app.synth()
