# Removing Unattached EBS Volumes
## First Change the root volume of a running instance to persist
1. Add a mapping.json file, set the value of the `DeviceName` to your block name.
2. Using the AWS CLI, modify the `DeleteOnTermination` attribute.
`aws ec2 modify-instance-attribute --instance-id i-0ac12a2d06f346e0f --block-device-mappings file://mapping.json`
