import boto3
import webbrowser
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
instance = ec2.Instance(new_instances[0].id)
instance.wait_until_running()

#!/usr/bin/env python3
import sys
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
unique_bucket_name = f"my-unique-bucket-{timestamp}"
s3 = boto3.resource("s3")
bucket_name = unique_bucket_name
s3.create_bucket(Bucket=bucket_name)

website_configuration = {
 'ErrorDocument': {'Key': 'error.html'},
 'IndexDocument': {'Suffix': 'index.html'},
}
bucket_website = s3.BucketWebsite(bucket_name) # replace with your
for bucket in s3.buckets.all():
    print (bucket.name)
    print ("---")
    for item in bucket.objects.all():
        print ("\t%s" % item.key)
print ("Upload an index.html file to test it works!")
