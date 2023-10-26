import boto3

vpc_id = 'vpc-0c13b0bc0df3d2f5d'
ec2 = boto3.client('ec2')


routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])