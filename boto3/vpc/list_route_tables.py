import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for routetable in response['RouteTables']:
    print(routetable['VpcId'], routetable['RouteTableId'])
    
    for association in routetable['Associations']:
        print(association['RouteTableAssociationId'])
        if 'SubnetId' in association:
            print(association['SubnetId'])
    
    for route in routetable['Routes']:
        print(route['DestinationCidrBlock'])
        if 'GatewayId' in route:
            print(route['GatewayId'])