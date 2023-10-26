import boto3

ec2 = boto3.client('ec2')



gateway = ec2.create_internet_gateway()

print(gateway['InternetGateway']['InternetGatewayId'])



#igw-06b846b5607c28397