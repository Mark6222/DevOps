#!/usr/bin/env python3
import sys
import boto3
import datetime

# Generate a unique bucket name
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
