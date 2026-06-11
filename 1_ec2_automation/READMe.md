Automated EC2 Instance Management Using AWS Lambda and Boto3

## Objective

Automate EC2 instance start and stop operations based on instance tags using AWS Lambda and Boto3.

## Resources Used

- AWS Lambda
- Amazon EC2
- IAM
- Python 3.14
- Boto3

## Steps Performed

1. Created two EC2 instances.
2. Added tags:
   - Action=auto-stop
   - Action=auto-start
3. Created IAM Role:
   - Lambda-EC2-Management-Role
   - AmazonEC2FullAccess policy attached
4. Created Lambda function:
   - ec2-start-stop
5. Developed Python script using Boto3.
6. Tested Lambda function manually.
7. Verified EC2 state changes.

## Outcome

The Lambda function successfully:
- Stops instances tagged with Action=auto-stop
- Starts instances tagged with Action=auto-start

## Screenshots

Refer to the screenshots folder.