import boto3

ig_id = 'igw-06b846b5607c28397'
route_table_id = 'rtb-0833483db6b62ede8'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId= ig_id,
    RouteTableId= route_table_id,
)   