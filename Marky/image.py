import boto3
bucket_name = "website-1222333"
image_file = "logo.jpg"
index = "index.html"
s3 = boto3.client("s3")
s3.upload_file(image_file, bucket_name, "Images/image.jpg")

website_configuration = {
 'ErrorDocument': {'Key': 'error.html'},
 'IndexDocument': {'Suffix': 'index.html'},
}
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration=website_configuration
)
s3.upload_file(index, bucket_name, "index.html")
print(f'Image uploaded to {bucket_name}')
