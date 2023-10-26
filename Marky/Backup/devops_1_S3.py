import boto3
import json
import random
import string

# s3 bucket
"""
length = 6;
random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
bucket_name = f"{random_chars}-bucket"
"""
bucket_name = "bucket-test-112233"
image_file = "logo.jpg"
index = "script.html"
style = "style.css"
#!/usr/bin/env python3
s3 = boto3.resource("s3")
s3.create_bucket(Bucket=bucket_name)

website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration=website_configuration
    )

s3client = boto3.client("s3")
s3client.delete_public_access_block(Bucket=bucket_name)   # delete bucket access block

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

s3.upload_file(index, bucket_name, "index.html")
print(f'Image uploaded to {bucket_name}')
