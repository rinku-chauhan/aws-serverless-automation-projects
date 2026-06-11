# Monitor S3 Bucket Encryption Using AWS Lambda and Boto3

## Objective

Detect Amazon S3 buckets that do not have server-side encryption enabled using AWS Lambda and Boto3.

## Services Used

* AWS Lambda
* Amazon S3
* IAM
* Python 3.x
* Boto3

## Steps Performed

1. Created multiple Amazon S3 buckets.
2. Created an IAM role with AmazonS3ReadOnlyAccess permissions.
3. Created a Lambda function named `s3-encryption-monitor`.
4. Used Boto3 to:

   * List all S3 buckets.
   * Check bucket encryption settings.
   * Identify encrypted and unencrypted buckets.
5. Executed the Lambda function manually.
6. Reviewed execution logs and results.

## Outcome

The Lambda function successfully inspected all S3 buckets and reported their encryption status.

## Security Benefit

This automation can be used to continuously monitor storage security compliance and identify buckets that do not meet encryption requirements.

## Screenshots

Refer to the Screenshots folder for implementation and verification evidence.
