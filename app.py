import boto3
s3 = boto3.client("s3", region_name='us-east-1')
s3Bucket = boto3.resource('s3')

response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
    
    # buckets = response
    bucket_name = bucket["Name"]
    
    # code below from https://github.com/kaisewhite/S3-Block-Public-Access/blob/main/app.py
    # Check if bucket actually exists
    if s3Bucket.Bucket(bucket_name).creation_date is None:
        print(f"The following bucket does not exist: {bucket}")
    else:
        try:
            s3.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                },
            )
            # response = s3.get_public_access_block(
            #    Bucket=bucket
            # )
            # print(response)
            print(f"Block Public Access Enabled For: {bucket}")
        except:
            # Handle Error Here
            pass
