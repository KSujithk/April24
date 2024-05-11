"""This module will contain utility functions to start and stop ec2
"""
import boto3

def start_ec2(instance_id):
    """Start ec2 instance
    """
    client = boto3.client('ec2')
    response = client.start_instances(InstanceIds=[instance_id])
    return response

def stop_ec2(instance_id):
    """stop ec2 instance
    """
    client = boto3.client('ec2')
    response = client.stop_instances(InstanceIds=[instance_id])
    return response


def ec2_instance_ids(tag_name, tag_value):
    """This method will return a list of instance ids 
    based on tag name and value
   
    Arguments:
      tag_name: str
      tag_value: str

    Returns:
      list
    """
    instance_ids = []
    client = boto3.client('ec2')
    response = client.describe_instances(
        Filters = [
            {
                'Name': f"tag:{tag_name}",
                'Values': [tag_value]
            }
        ]
    )
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    return instance_ids




if __name__ == '__main__':
    instance_ids = ec2_instance_ids('Name', 'sample')
    for instance_id in instance_ids:
        stop_ec2(instance_id)

