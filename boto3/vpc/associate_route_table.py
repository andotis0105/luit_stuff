import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-0833483db6b62ede8'
subnet_id = 'subnet-096be102da3377a2d'

response = ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)

print(response)