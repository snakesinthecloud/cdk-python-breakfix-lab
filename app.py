#!/usr/bin/env python3
from aws_cdk import App

from stacks.orphaned_resources_import.stack import OrphanedResources

app = App()

# Deploy all: cdk deploy --require-approval never --all --profile <aws profile>
# Deploy single stack: cdk deploy --require-approval never <name> --profile <aws profile>

OrphanedResources(app, "OrphanedResources")

app.synth()
