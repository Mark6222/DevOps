import boto3
import json
import random
import string
import requests
import webbrowser
import subprocess

# EC2 instance
ec2 = boto3.resource('ec2')
try:
    new_instances = ec2.create_instances(
        ImageId='ami-00c6177f250e07ec1',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.nano',
        SecurityGroupIds=['sg-03e384e19871111c1'],
        KeyName='MarksEC2Key',
        UserData="""#!/bin/bash
        yum install httpd -y
        systemctl enable httpd
        systemctl start httpd
        echo '<html>' > index.html
        echo 'Private IP address: ' >> index.html
        curl http://169.254.169.254/latest/meta-data/local-ipv4 >> index.html
        echo '<br>Instance Type: ' >> index.html
        curl http://169.254.169.254/latest/meta-data/instance-type >> index.html
        echo '<br>Availability Zone: ' >> index.html
        curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html
        echo '<br><p><<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Freflection%2F&psig=AOvVaw1YU_Bl8ptFRPls4gef89g6&ust=1697799794877000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJCRyJ77gYIDFQAAAAAdAAAAABAE" alt="A beautiful image">></p>: ' >> index.html
        cp index.html /var/www/html/index.html"""
    )
    print(f"EC2 {new_instances[0].id} created successfully")
except Exception as e:
	print(f"Error creating the instance: {e}")
instance = ec2.Instance(new_instances[0].id)
instance.wait_until_running()
name_tag = {'Key': 'Name', 'Value': 'assignment1'}
instance.create_tags(Tags=[name_tag])




# downloads image
try:
    image_url = "http://devops.witdemo.net/logo.jpg"
    response = requests.get(image_url)
    local_file_name = "logo.jpg"
    open(local_file_name, "wb").write(response.content)
    print(f"Image downloaded and saved as '{local_file_name}'")
except Exception as e:
	print(f"Error creating the image file: {e}")

# s3 bucket
length = 6;
random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
bucket_name = f"{random_chars}-mhogan"
image_file = "logo.jpg"
index = "indexImage.html"
style = "style.css"

#!/usr/bin/env python3
try:
    s3 = boto3.resource("s3")
    s3.create_bucket(Bucket=bucket_name)
    
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
        }
    print(f"succesfully created bucket {bucket_name}")
except Exception as e:
	print(f"Error creating the bucket: {e}")


s3client = boto3.client("s3")
s3client.delete_public_access_block(Bucket=bucket_name)   # delete bucket access block

s3client.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration=website_configuration
)

bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}
s3.Bucket(bucket_name).Policy().put(Policy=json.dumps(bucket_policy))
s3_object = s3.Object(bucket_name, "index.html")
s3_object.put(
    Body=open(index, 'rb'),
    ContentType = 'text/html'
)
s3client.upload_file(image_file, bucket_name, "Images/image.jpg")
print(f'Image uploaded to {bucket_name}')

url1 = f"http://{bucket_name}-bucket.s3-website-us-east-1.amazonaws.com"
url2 = f"http://{instance.public_ip_address}"
webbrowser.open_new_tab(url1)
webbrowser.open_new_tab(url2)

local_file_name = "mhogan-websites.txt"
open(local_file_name, "w").write(f"Instance: {url1} bucket: {url2}")

# monitoring
try:
    instancePublicID = instance.public_ip_address
    cmd = f"scp -i MarksEC2Key.pem monitoring.sh ec2-user@{instancePublicID}:."
    cmd2 = f"ssh -i MarksEC2Key.pem ec2-user@{instancePublicID} 'chmod 700 monitoring.sh'"
    cmd3 = f"ssh -o StrictHostKeyChecking=no -i MarksEC2Key.pem ec2-user@{instancePublicID} './monitoring.sh'"
    result = subprocess.run(cmd, shell=True)
    print (result.returncode)
    result = subprocess.run(cmd2, shell=True)
    print (result.returncode)
    result = subprocess.run(cmd3, shell=True)
    print (result.returncode)
except Exception as e:
	print(f"Error monitoring: {e}")
