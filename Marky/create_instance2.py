import boto3

ec2 = boto3.resource('ec2')


new_instances = ec2.create_instances(
    ImageId='ami-00c6177f250e07ec1',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.nano',
    SecurityGroupIds=['sg-03e384e19871111c1'],
    KeyName='demo instance 1',
    UserData="""#!/bin/bash
    yum install httpd -y
    systemctl enable httpd
    systemctl start httpd"""
)
