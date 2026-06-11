# Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

## Objective

Automate EBS volume backups using AWS Lambda and Boto3 and implement snapshot retention management.

## Services Used

- AWS Lambda
- Amazon EC2
- Amazon EBS
- IAM
- Python
- Boto3

## Steps Performed

1. Identified an EBS volume.
2. Created an IAM role with AmazonEC2FullAccess.
3. Created a Lambda function named `ebs-snapshot-automation`.
4. Developed a Boto3 script to:
   - Create EBS snapshots.
   - Tag snapshots.
   - Identify old snapshots.
   - Delete snapshots beyond the retention period.
5. Executed the Lambda function manually.
6. Verified snapshot creation in the EC2 console.

Note:
For demonstration purposes during testing, the retention period was temporarily set to 1 minute to validate the cleanup logic. The final submission uses the assignment requirement of 30 days.

## Outcome

The Lambda function successfully created an EBS snapshot and implemented automated snapshot retention logic.

## Screenshots

Refer to the Screenshots folder.