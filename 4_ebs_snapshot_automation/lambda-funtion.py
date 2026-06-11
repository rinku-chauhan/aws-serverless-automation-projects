import boto3
from datetime import datetime, timezone, timedelta

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Replace with your EBS Volume ID
VOLUME_ID = "vol-07776739a0be936f6"

def lambda_handler(event, context):

    created_snapshot = None
    deleted_snapshots = []

    # Create a new snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description='Automated EBS Snapshot'
    )

    created_snapshot = snapshot['SnapshotId']

    # Tag the snapshot
    ec2.create_tags(
        Resources=[created_snapshot],
        Tags=[
            {
                'Key': 'CreatedBy',
                'Value': 'LambdaAutomation'
            }
        ]
    )

    # Retention period: 30 days
    retention_date = datetime.now(
        timezone.utc
    ) - timedelta(days=30)

    # Retrieve snapshots owned by this account
    snapshots = ec2.describe_snapshots(
        OwnerIds=['self']
    )['Snapshots']

    # Delete snapshots older than 30 days
    for snap in snapshots:

        if snap['StartTime'] < retention_date:

            snapshot_id = snap['SnapshotId']

            try:
                ec2.delete_snapshot(
                    SnapshotId=snapshot_id
                )

                deleted_snapshots.append(
                    snapshot_id
                )

                print(
                    f"Deleted old snapshot: {snapshot_id}"
                )

            except Exception as e:

                print(
                    f"Could not delete {snapshot_id}: {e}"
                )

    return {
        "statusCode": 200,
        "created_snapshot": created_snapshot,
        "deleted_snapshots": deleted_snapshots
    }