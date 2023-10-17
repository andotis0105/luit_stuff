import boto3

s3 = boto3.client('s3')
 
s3.put_object(Bucket="boto3-test-bucket-otis-123", Key="test_text_string.txt", Body='This shit is a string', ContentType="text/plain") 
