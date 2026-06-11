import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    stop_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': ['auto-stop']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    stop_instances = [
        instance['InstanceId']
        for reservation in stop_response['Reservations']
        for instance in reservation['Instances']
    ]

    if stop_instances:
        ec2.stop_instances(InstanceIds=stop_instances)
        print(f"Stopped Instances: {stop_instances}")

    start_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': ['auto-start']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['stopped']
            }
        ]
    )

    start_instances = [
        instance['InstanceId']
        for reservation in start_response['Reservations']
        for instance in reservation['Instances']
    ]

    if start_instances:
        ec2.start_instances(InstanceIds=start_instances)
        print(f"Started Instances: {start_instances}")

    return {
        'statusCode': 200,
        'body': 'EC2 automation completed'
    }