#!/usr/bin/env python3
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-026b57f3c383c2eec',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.nano')
print (instance[0].id)
