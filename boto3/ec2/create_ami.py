import boto3

ec2 = boto3.client('ec2')

instance_id = 'i-0eb181171940e7a32'
name = 'OtisCorpImage'

response = ec2.create_image(InstanceId= instance_id, Name= name)

print(response)