import boto3


route_table_id = 'rtb-0833483db6b62ede8'
ec2 = boto3.client('ec2')



ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId= route_table_id,
)