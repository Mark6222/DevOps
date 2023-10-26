import boto3

ec2 = session.resource('ec2')
s3 = session.resource('s3')

def ec2_instances():
    print("EC2 Instances:")
    for inst in ec2.instances.all():
        print("Instance ID:", inst.id)
        print("Public IP Address:", inst.public_ip_address)
        print()

def s3_buckets():
    print("S3 Buckets:")
    for bucket in s3.buckets.all():
        print("Bucket Name:", bucket.name)
        print()

if True:
    ec2_instances()
    print()
    s3_buckets()
