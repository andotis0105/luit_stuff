import boto3

ec2 = boto3.client('ec2')
ig_id = 'igw-06b846b5607c28397'


ec2.delete_internet_gateway(InternetGatewayId= ig_id)
