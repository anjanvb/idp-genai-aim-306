#!/usr/bin/env python3
import aws_cdk as cdk
from stack.simple_async_workflow import SimpleAsyncWorkflow

app = cdk.App()
SimpleAsyncWorkflow(app, "SimpleAsyncWorkflow")

app.synth()
