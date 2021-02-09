subnets = self.ec2_client.describe_subnets(
    Filters=[{
        "Name": "vpc-id",
        "Values": [vpc_id]
    }]
)