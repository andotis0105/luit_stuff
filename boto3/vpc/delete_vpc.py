import boto3

ec2 = boto3.client('ec2')
vpc_id = 'vpc-0c13b0bc0df3d2f5d'

ec2.delete_vpc(VpcId=vpc_id)