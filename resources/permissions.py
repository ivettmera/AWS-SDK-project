import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c212088a5370669l15230211t1w256062372894-s3bucket-8nf3qzir84zt"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")