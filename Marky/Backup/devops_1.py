import boto3

# EC2 instance
ec2 = boto3.resource('ec2')
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
instance = ec2.Instance(new_instances[0].id)
instance.wait_until_running()
name_tag = {'Key': 'Name', 'Value': 'assignment1'}
instance.create_tags(Tags=[name_tag])



# s3 bucket
"""
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
"""
