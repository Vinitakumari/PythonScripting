#Write a Python script to terminate unused EC2 instances (e.g., stopped for >7 days).
import boto3
import json

ec2 = boto3.client("ec2")
def describe_instances():
   
    instances =ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    #print(f"all instances described:{instances}")
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'], instance['State']['Name'])
    response = json.dumps(instances, indent=4, default=str)

    return response


def stop_instances():
    stopped_instances =ec2.stop_instances(InstanceIds= ["i-0e5d1d6ef699dfca6"])
    print(f"stopped instance:{stopped_instances}")


if __name__=='__main__':
   all_instances= describe_instances()
   print(f"all instance in json format:{all_instances}")

   stopped_instances=stop_instances()
   print(f"stopped instances in json format: {stopped_instances}")
