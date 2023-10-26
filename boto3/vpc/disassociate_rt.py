import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-0833483db6b62ede8'


response = ec2.describe_route_tables(
    RouteTableIds=[route_table_id])

for association in  response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        assoc_id = association['RouteTableAssociationId']
        print(assoc_id)

        ec2.disassociate_route_table(AssociationId=assoc_id)
        
