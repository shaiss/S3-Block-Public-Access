import boto3
s3 = boto3.client("s3", region_name='us-east-1')
s3Bucket = boto3.resource('s3')

buckets = [""]

for bucket in buckets:
    # Check if bucket actually exists
    if s3Bucket.Bucket(bucket).creation_date is None:
        print(f"The following bucket does not exist: {bucket}")
    else:
        try:
            s3.put_public_access_block(
                Bucket=bucket,
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
