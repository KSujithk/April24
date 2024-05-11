"""This module will contain utility functions to start and stop ec2
"""
import boto3

def start_ec2(instance_id, region = 'ap-south-1'):
    """Start ec2 instance
    """
    client = boto3.client('ec2',region_name=region)
    response = client.start_instances(InstanceIds=[instance_id])
    return response

def stop_ec2(instance_id, region = 'ap-south-1'):
    """stop ec2 instance
    """
    client = boto3.client('ec2',region_name=region)
    response = client.stop_instances(InstanceIds=[instance_id])
    return response


def ec2_instance_ids(tag_name, tag_value, region = 'ap-south-1'):
    """This method will return a list of instance ids 
    based on tag name and value
   
    Arguments:
      tag_name: str
      tag_value: str

    Returns:
      list
    """
    instance_ids = []
    client = boto3.client('ec2',region_name=region)
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

def start_ec2_instances_by_tag(tag_name, tag_value, region):
    """
    This method will start ec2 instances by tag value
    """
    resp_instance_ids = ec2_instance_ids(tag_name, tag_value, region)
    for resp_instance_id in resp_instance_ids:
        start_ec2(resp_instance_id, region)

def stop_ec2_instances_by_tag(tag_name, tag_value, region):
    """
    This method will stop ec2 instances by tag value
    """
    resp_instance_ids = ec2_instance_ids(tag_name, tag_value, region)
    for resp_instance_id in resp_instance_ids:
        stop_ec2(resp_instance_id, region)





if __name__ == '__main__':
    stop_ec2_instances_by_tag('Name', 'sample', 'ap-south-1')

