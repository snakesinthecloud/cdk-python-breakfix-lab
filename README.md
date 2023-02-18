# cdk-python-breakfix-lab
A testing area for breaking and fixing CDK / Cloudformation


# Steps

## Create the problem
`cdk deploy --require-approval never --all --profile snakesinthecloud`
`cdk destroy --require-approval never --all --profile snakesinthecloud`

cdk-python-breakfix-lab-bucket1 will remain
`cdk deploy --require-approval never --all --profile snakesinthecloud`

Error: 

    cdk-python-breakfix-lab-bucket1 already exists
    The following resource(s) failed to create: [CustomS3AutoDeleteObjectsCustomResourceProviderRole3B1BD092, BreakfixS3BucketRetain928689F4, BreakfixS3BucketDeleteB5D79AE0]. Rollback requested by user.


## Fix

Output the expected config to a yaml file

`cdk synth OrphanedResources --profile snakesinthecloud -> expected.yml`

In CloudFormation, under the AWS Management Console, output the current config.  Save this as `import.yml`

1. CloudFormation -> Stacks -> OrphanedResources -> Template -> View in Designer
2. Choose template language: YAML
3. Copy the template and save as `import.yml`
4. For every resource the fails to create because it already exists, do the following:
    a. Search expected.yml for this resource.  (e.g. `BucketName: cdk-python-breakfix-lab-bucket1`)
    b. Copy the entire config for this resource, and paste this into `import.yml` under the `Resources:` section.
    ```
      BreakfixS3BucketRetain928689F4:
        Type: AWS::S3::Bucket
        Properties:
        BucketName: cdk-python-breakfix-lab-bucket1
        OwnershipControls:
            Rules:
            - ObjectOwnership: ObjectWriter
        PublicAccessBlockConfiguration:
            BlockPublicAcls: true
            BlockPublicPolicy: true
            IgnorePublicAcls: true
            RestrictPublicBuckets: true
        UpdateReplacePolicy: Retain
        DeletionPolicy: Retain
        Metadata:
        aws:cdk:path: OrphanedResources/BreakfixS3BucketRetain/Resource
    ```
    c. Save import.yml
5. Remove resources from import.yml that cannot be imported
    a. AWS::CDK::Metadata
    b. AWS::S3::BucketPolicy
    b. Custom::S3AutoDeleteObjects
6. Navigate back to the CloudFormation Stack in the AWS Management Console
    a. Click Create stack -> With existing resources (import resources)
    b. Import `import.yml`
    c. For each of the imported buckets, enter the BucketName property that corresponds.
    d. Enter stack name `OrphanedResources`