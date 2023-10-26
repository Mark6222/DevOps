import boto3

# Replace 'your-bucket-name' and 'your-region' with your desired bucket name and AWS region.
bucket_name = 'your-bucket-name-123409877'
region = 'us-east-1'
image_file = "logo.jpg"
index = "index.html"

# Initialize an S3 client with the specified region.
s3 = boto3.client('s3')

# Create the S3 bucket.
try:
	s3.create_bucket(Bucket=bucket_name)
	website_configuration = {
	'ErrorDocument': {'Key': 'error.html'},
	'IndexDocument': {'Suffix': 'index.html'},
	}
	s3.put_bucket_website(
	Bucket=bucket_name,
	WebsiteConfiguration=website_configuration
	)
	s3.upload_file(image_file, bucket_name, "Images/image.jpg")
	print(f"Bucket '{bucket_name}' created successfully in region '{region}'.")
except Exception as e:
	print(f"Error creating the bucket: {e}")