import boto3

s3 = boto3.client('s3')

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = s3.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if(extension in content['Key'][-(len(extension)):]):
            keys.append(content['Key'])
        
    return keys
    
def list_object_keys(client, bucket, prefix=''):
    keys = []
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response['Contents']:
        keys.append(content['Key'])
        
    return keys
    
    
    
#response = filter_objects_extension(s3, 'boto3-test-bucket-otis-123', '/')
#print(response)
    
if __name__ == '__main__':
    s3 = boto3.client('s3')

    response = list_object_keys(s3, 'boto3-test-bucket-otis-123')
    print(response)
    
    response = list_object_keys(s3, 'boto3-test-bucket-otis-123', '/')
    print(response)

#s3 = boto3.client('s3')
#
#response = s3.list_objects_v2(Bucket='boto3-test-bucket-otis-123') #, Prefix='folder/example/'

#for content in response['Contents']:
#    if('.txt' in content['Key'][-4:]):
# if(extension in content['Key'][-(len(extension):]):
#        print(content['Key'])