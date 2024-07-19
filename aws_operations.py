import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Download a file from S3
s3.download_file('roulettechsunny', '', '')

# Upload a file to S3
s3.upload_file('/home/ali023/recipes/recipesreact/package.json', 'roulettechsunny', 'package.json')
