import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = "rinku-s3-cleanup-lab"

def lambda_handler(event, context):

    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)

    cutoff_date = datetime.now(timezone.utc) - timedelta(minutes=1)

    deleted_files = []

    if 'Contents' in objects:

        for obj in objects['Contents']:

            if obj['LastModified'] < cutoff_date:

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=obj['Key']
                )

                deleted_files.append(obj['Key'])
                print(f"Deleted: {obj['Key']}")

    return {
        'statusCode': 200,
        'deleted_files': deleted_files
    }