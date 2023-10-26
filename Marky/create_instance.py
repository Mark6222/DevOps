import boto3
ec2 = boto3.resource('ec2')
new_instances = ec2.create_instances(
ImageId='ami-00c6177f250e07ec1',
MinCount=1,
MaxCount=1,
InstanceType='t2.nano')
print (new_instances[0].id)

