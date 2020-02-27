import boto3


def lambda_handler(object, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    #Iterate through the regions
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Region:", region)

        # List only unattached volumes with filter ('available' vs. 'in-use')
        volumes = ec2.volumes.filter(
            Filters=[{'Name': 'status', 'Values': ['available']}])

        # Loop through and delete the volume
        for volume in volumes:
            v = ec2.Volume(volume.id)
            print("Deleting EBS volume: {}, Size: {} GiB".format(v.id, v.size))
            v.delete()