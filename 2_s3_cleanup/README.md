Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Objective

Automate the deletion of files older than 30 days from an Amazon S3 bucket using AWS Lambda and Boto3.

## Services Used

- AWS Lambda
- Amazon S3
- IAM
- Python 3.x
- Boto3

## Steps Performed

1. Created an S3 bucket.
2. Uploaded test files.
3. Created IAM role:
   - Lambda-S3-Cleanup-Role
   - AmazonS3FullAccess policy attached.
4. Created Lambda function:
   - s3-cleanup
5. Developed a Python script using Boto3.
6. Listed S3 objects.
7. Deleted objects older than the configured retention period.
8. Verified object deletion from the S3 bucket.

## Outcome

The Lambda function successfully identified and deleted old objects from the S3 bucket.

## Screenshots

Refer to the screenshots folder.