import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def lambda_handler(event, context):

    buckets = s3.list_buckets()

    encrypted_buckets = []
    unencrypted_buckets = []

    for bucket in buckets['Buckets']:

        bucket_name = bucket['Name']

        try:
            s3.get_bucket_encryption(
                Bucket=bucket_name
            )

            encrypted_buckets.append(bucket_name)

        except ClientError:

            unencrypted_buckets.append(bucket_name)

    print("Encrypted Buckets:")
    for bucket in encrypted_buckets:
        print(bucket)

    print("Unencrypted Buckets:")
    for bucket in unencrypted_buckets:
        print(bucket)

    return {
        "statusCode": 200,
        "encrypted_buckets": encrypted_buckets,
        "unencrypted_buckets": unencrypted_buckets
    }