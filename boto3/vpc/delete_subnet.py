import boto3

ec2 = boto3.client('ec2')

subnet_id = 'subnet-0fd662fc85d5c4a3b'


ec2.delete_subnet(SubnetId=subnet_id)
