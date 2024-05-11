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


if __name__ == '__main__':
    instance_id = input("Enter your ec2 instance id: ")
    start_ec2(instance_id)
