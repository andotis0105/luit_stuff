import boto3

ec2 = boto3.client('ec2')

ig_id = 'igw-06b846b5607c28397'
vpc_id = 'vpc-0c13b0bc0df3d2f5d'

attach_ig_vpc = ec2.attach_internet_gateway(InternetGatewayId=ig_id,VpcId=vpc_id)
print(attach_ig_vpc)