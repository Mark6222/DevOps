import boto3
import json
import random
import string
import requests

# downloads image
image_url = "http://devops.witdemo.net/logo.jpg"
response = requests.get(image_url)
local_file_name = "logo.jpg"
open(local_file_name, "wb").write(response.content)
print(f"Image downloaded and saved as '{local_file_name}'")
# s3 bucket
length = 6;
random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
bucket_name = f"{random_chars}-bucket"
image_file = "logo.jpg"
index = "indexImage.html"
style = "style.css"
#!/usr/bin/env python3
s3 = boto3.resource("s3")
s3.create_bucket(Bucket=bucket_name)

website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}


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
# s3client.upload_file(index, bucket_name, "index.html")
s3_object = s3.Object(bucket_name, "index.html")
s3_object.put(
    Body=open(index, 'rb'),
    ContentType = 'text/html'
)
s3client.upload_file(image_file, bucket_name, "Images/image.jpg")
print(f'Image uploaded to {bucket_name}')
