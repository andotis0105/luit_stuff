import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instance_types(
    Filters=[{'Name': 'free-tier-eligible','Values': ['true']}])

for InstanceType in response['InstanceTypes']:
    print(InstanceType['InstanceType'], InstanceType['FreeTierEligible'])
    
