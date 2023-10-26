import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()

for gateway in response['InternetGateways']:
    print(gateway['InternetGatewayId'])
    for attachment in gateway['Attachments']:
        print(attachment['VpcId'], attachment['State'])