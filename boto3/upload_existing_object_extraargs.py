import boto3

s3 = boto3.client('s3')


s3.upload_file('test_text.txt', 'boto3-test-bucket-otis-123', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})