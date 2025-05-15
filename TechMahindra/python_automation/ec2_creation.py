#Automate EC2 Instance Creation Using Python
import boto3
ec2 = boto3.resource("ec2")
instances = ec2.create_instances( 
    ImageId = "ami-0e58b56aa4d64231b",
    InstanceType = "t2.micro",
    KeyName = "MyKeyPair",
    MinCount= 1,
    MaxCount = 1,
    TagSpecifications=[
        {
        'ResourceType': 'instance',
        'Tags': [
                {'Key': 'Name', 'Value': 'MyBoto3Instance'}
                ]
        }
    ]
)
