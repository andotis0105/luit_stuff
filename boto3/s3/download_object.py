import boto3
import os

from list_objects import list_object_keys

def download_single_object(client, bucket, key, filename):
    s3.download_file(bucket, key, filename)
    
if __name__ == '__main__':
    
    bucket = 'boto3-test-bucket-otis-123'
    key = 'another_test.txt'
    fielname = 'another_test.txt'
    
    s3 = boto3.client('s3')
    
    keys = list_object_keys(s3, bucket)

    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else: 
            download_single_object(s3, bucket, key, key)
            print(keys)