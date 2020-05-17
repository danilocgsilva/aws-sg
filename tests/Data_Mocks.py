class Data_Mocks:

    def get_sample_string_response(self) -> str:
            return '''{
    "SecurityGroups": [
        {
            "Description": "Access from the backery",
            "GroupName": "my-first-sg",
            "IpPermissions": [],
            "OwnerId": "123324134",
            "GroupId": "sg-2f31fa12094",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "My Mysql access"
                }
            ],
            "VpcId": "vpc-1fda238a"
        },
        {
            "Description": "Access from another place",
            "GroupName": "Any other place",
            "IpPermissions": [
                {
                    "FromPort": 22,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "123.12.123.123/16"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 22,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "129384710927",
            "GroupId": "sg-423fa34f43def",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Allow ssh from anywhere"
                }
            ],
            "VpcId": "vpc-34fa890d"
        },
        {
            "Description": "This comes from Elastic Beanstalk",
            "GroupName": "crazy-hash-from-elastic-beanstalk",
            "IpPermissions": [
                {
                    "FromPort": 80,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 80,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "86876876986897",
            "GroupId": "sg-96f7d999a98f",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "Tags": [
                {
                    "Key": "elasticbeanstalk:environment-id",
                    "Value": "e-laiuefgkjagfkagalkdsjfakjh"
                },
                {
                    "Key": "aws:cloudformation:logical-id",
                    "Value": "AWSEBSecurityGroup"
                },
                {
                    "Key": "aws:cloudformation:stack-name",
                    "Value": "awseb-e-laksjfhdlkajsfkldjah-stack"
                },
                {
                    "Key": "elasticbeanstalk:environment-name",
                    "Value": "not-allowed-now"
                },
                {
                    "Key": "Name",
                    "Value": "either-not-allowed"
                },
                {
                    "Key": "aws:cloudformation:stack-id",
                    "Value": "arn:aws:cloudformation:us-east-1:928479582798798:stack/awseb-e-asdfugakjsdfgkja-stack/34653465354-356-3465-476546-536346534"
                }
            ],
            "VpcId": "vpc-45f12a71"
        }
    ],
    "ResponseMetadata": {
        "RequestId": "laihfkjh-asdkjfaksjdh-asdflaksjdh-asdjbhfasjdb-ajsdhf",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "askdjfh-dfgh-dhfg-asf-35670398475",
            "content-type": "text/xml;charset=UTF-8",
            "transfer-encoding": "chunked",
            "vary": "accept-encoding",
            "date": "Sat, 16 May 2020 18:33:13 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}
'''

    def get_single_security_group_string_data(self) -> str:
        return '''{
            "Description": "Access from the backery",
            "GroupName": "my-first-sg",
            "IpPermissions": [],
            "OwnerId": "123324134",
            "GroupId": "sg-2f31fa12094",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "My Mysql access"
                }
            ],
            "VpcId": "vpc-1fda238a"
        }
'''

    def get_regions_string_mocked_data(self) -> str:
        return '''{
    "Regions": [
        {
            "Endpoint": "ec2.sa-north-1.amazonaws.com",
            "RegionName": "sa-north-1",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.ju-south-1.amazonaws.com",
            "RegionName": "ju-south-1",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.mo-west-3.amazonaws.com",
            "RegionName": "mo-west-3",
            "OptInStatus": "opt-in-not-required"
        }
    ],
    "ResponseMetadata": {
        "RequestId": "1-2-3-4-5",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "1-2-3-4-5",
            "content-type": "text/xml;charset=UTF-8",
            "vary": "accept-encoding",
            "date": "Sat, 23 May 1920 23:28:08 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}
'''
