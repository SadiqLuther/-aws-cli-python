import boto3
region = 'ap-south-1'
instances = ['i-09587b4cb446b0072']
ec2 = boto3.client('ec2', region_name=region)
ec2.stop_instances(InstanceIds=instances)
print('Stopped your instances: ' + str(instances))
