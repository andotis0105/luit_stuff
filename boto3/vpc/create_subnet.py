import boto3

cidr_block = '11.0.2.0/24'
vpc_id = 'vpc-0c13b0bc0df3d2f5d'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidr_block,VpcId=vpc_id)
print(subnet['Subnet']['SubnetId'])