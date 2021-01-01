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
            "IpPermissions": [
                {
                    "FromPort": 3306,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "189.18.172.95/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 3306,
                    "UserIdGroupPairs": []
                }
            ],
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

    def get_rds_request_string_mocked_data(self) -> str:
        return '''{
    "DBInstances": [
        {
            "DBInstanceIdentifier": "myinstance",
            "DBInstanceClass": "db.t2.micro",
            "Engine": "mysql",
            "DBInstanceStatus": "available",
            "MasterUsername": "master_name",
            "DBName": "main_database",
            "Endpoint": {
                "Address": "main_database.luisdkjsghf.mo-east-2.rds.amazonaws.com",
                "Port": 3306,
                "HostedZoneId": "asldjfhakslalkj"
            },
            "AllocatedStorage": 20,
            "PreferredBackupWindow": "06:19-06:49",
            "BackupRetentionPeriod": 7,
            "DBSecurityGroups": [],
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-asdkljhkjhasdf",
                    "Status": "active"
                },
                {
                    "VpcSecurityGroupId": "sg-asdlfkjahfsd",
                    "Status": "active"
                }
            ],
            "DBParameterGroups": [
                {
                    "DBParameterGroupName": "default.mysql5.6",
                    "ParameterApplyStatus": "in-sync"
                }
            ],
            "AvailabilityZone": "us-east-1zz",
            "DBSubnetGroup": {
                "DBSubnetGroupName": "default",
                "DBSubnetGroupDescription": "default",
                "VpcId": "vpc-asdlkfjha",
                "SubnetGroupStatus": "Complete",
                "Subnets": [
                    {
                        "SubnetIdentifier": "subnet-adlkjhaflskjdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-aldksjfhalkjsdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-asdlkfhaklsjdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-alsdjfhalksjdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-asdbjaskjdhf",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-alkdjfhalkjfdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    }
                ]
            },
            "PreferredMaintenanceWindow": "fri:04:33-fri:05:03",
            "PendingModifiedValues": {},
            "MultiAZ": false,
            "EngineVersion": "5.6.41",
            "AutoMinorVersionUpgrade": false,
            "ReadReplicaDBInstanceIdentifiers": [],
            "LicenseModel": "general-public-license",
            "OptionGroupMemberships": [
                {
                    "OptionGroupName": "default:mysql-5-6",
                    "Status": "in-sync"
                }
            ],
            "PubliclyAccessible": true,
            "StorageType": "gp2",
            "DbInstancePort": 0,
            "StorageEncrypted": false,
            "DbiResourceId": "db-lkjdhflakjsfhdl",
            "CACertificateIdentifier": "rds-ca-2015",
            "DomainMemberships": [],
            "CopyTagsToSnapshot": false,
            "MonitoringInterval": 0,
            "DBInstanceArn": "arn:aws:rds:us-east-1:asdlkfjahskljfdh:db:alksjdfhklajh",
            "IAMDatabaseAuthenticationEnabled": false,
            "PerformanceInsightsEnabled": false,
            "DeletionProtection": false,
            "AssociatedRoles": []
        }
    ],
    "ResponseMetadata": {
        "RequestId": "kjdhasdf-alksjdfh-sdfasd-asdkjf-kjdafh",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "asldg-jkgsda-lskdajfh-alkjsdhf-alkjsdfhaskjhd",
            "content-type": "text/xml",
            "vary": "accept-encoding",
            "date": "Sun, 24 May 2020 18:59:18 GMT"
        },
        "RetryAttempts": 0
    }
}
'''

    def get_json_string_from_single_rds(self) -> str:
        return '''{
            "DBInstanceIdentifier": "myinstancename",
            "DBInstanceClass": "db.t2.micro",
            "Engine": "mysql",
            "DBInstanceStatus": "available",
            "MasterUsername": "master_name",
            "DBName": "main_database",
            "Endpoint": {
                "Address": "main_database.akhsdgkagf.us-east-1.rds.amazonaws.com",
                "Port": 3306,
                "HostedZoneId": "asldjfhakslalkj"
            },
            "AllocatedStorage": 20,
            "PreferredBackupWindow": "06:19-06:49",
            "BackupRetentionPeriod": 7,
            "DBSecurityGroups": [],
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-asdkljhkjhasdf",
                    "Status": "active"
                },
                {
                    "VpcSecurityGroupId": "sg-asdlfkjahfsd",
                    "Status": "active"
                }
            ],
            "DBParameterGroups": [
                {
                    "DBParameterGroupName": "default.mysql5.6",
                    "ParameterApplyStatus": "in-sync"
                }
            ],
            "AvailabilityZone": "us-east-1zz",
            "DBSubnetGroup": {
                "DBSubnetGroupName": "default",
                "DBSubnetGroupDescription": "default",
                "VpcId": "vpc-asdlkfjha",
                "SubnetGroupStatus": "Complete",
                "Subnets": [
                    {
                        "SubnetIdentifier": "subnet-adlkjhaflskjdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-aldksjfhalkjsdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-asdlkfhaklsjdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-alsdjfhalksjdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-asdbjaskjdhf",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-alkdjfhalkjfdh",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1z"
                        },
                        "SubnetStatus": "Active"
                    }
                ]
            },
            "PreferredMaintenanceWindow": "fri:04:33-fri:05:03",
            "PendingModifiedValues": {},
            "MultiAZ": false,
            "EngineVersion": "5.6.41",
            "AutoMinorVersionUpgrade": false,
            "ReadReplicaDBInstanceIdentifiers": [],
            "LicenseModel": "general-public-license",
            "OptionGroupMemberships": [
                {
                    "OptionGroupName": "default:mysql-5-6",
                    "Status": "in-sync"
                }
            ],
            "PubliclyAccessible": true,
            "StorageType": "gp2",
            "DbInstancePort": 0,
            "StorageEncrypted": false,
            "DbiResourceId": "db-lkjdhflakjsfhdl",
            "CACertificateIdentifier": "rds-ca-2015",
            "DomainMemberships": [],
            "CopyTagsToSnapshot": false,
            "MonitoringInterval": 0,
            "DBInstanceArn": "arn:aws:rds:us-east-1:asdlkfjahskljfdh:db:alksjdfhklajh",
            "IAMDatabaseAuthenticationEnabled": false,
            "PerformanceInsightsEnabled": false,
            "DeletionProtection": false,
            "AssociatedRoles": []
        }
'''        


    def get_json_string_several_security_group(self) -> str:
        return '''{
    "SecurityGroups": [
        {
            "Description": "Allow ssh from my business",
            "GroupName": "Allow ssh from my business",
            "IpPermissions": [
                {
                    "FromPort": 22,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "234.33.147.232/8"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 22,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "098472908375",
            "GroupId": "sg-19982634857623",
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
                    "Value": "From my business"
                }
            ],
            "VpcId": "vpc-2983479"
        },
        {
            "Description": "SecurityGroup for ElasticBeanstalk environment",
            "GroupName": "awseb-e-sadjkfa-stack-AWSEBSecurityGroup-asdfoiasdfiu",
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
            "OwnerId": "2984359283",
            "GroupId": "sg-2034590283479",
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
                    "Value": "e-lasdlkjh"
                },
                {
                    "Key": "aws:cloudformation:logical-id",
                    "Value": "AWSEBSecurityGroup"
                },
                {
                    "Key": "aws:cloudformation:stack-name",
                    "Value": "awseb-e-adsfadsl-stack"
                },
                {
                    "Key": "elasticbeanstalk:environment-name",
                    "Value": "some-random-name"
                },
                {
                    "Key": "Name",
                    "Value": "some-random-name"
                },
                {
                    "Key": "aws:cloudformation:stack-id",
                    "Value": "arn:aws:cloudformation:us-east-1:23984752983475:stack/awseb-e-sdfadgsdf-stack/986-fkg-ghd-sdfg-sdfgsd"
                }
            ],
            "VpcId": "vpc-20349857209384"
        },
        {
            "Description": "Remote Connection to Windows",
            "GroupName": "rdp",
            "IpPermissions": [
                {
                    "FromPort": 3389,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 3389,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "203948572098347",
            "GroupId": "sg-23452340987",
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
            "VpcId": "vpc-23459876"
        },
        {
            "Description": "Dynamic access for mysql",
            "GroupName": "dynamic_mysql",
            "IpPermissions": [
                {
                    "FromPort": 3306,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "202.17.188.12/16"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 3306,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "356345345",
            "GroupId": "sg-785639367",
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
                    "Value": "Dynamic mysql ip"
                }
            ],
            "VpcId": "vpc-24352345"
        },
        {
            "Description": "CloudDesktop",
            "GroupName": "CloudDesktop",
            "IpPermissions": [
                {
                    "FromPort": 22,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 22,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 3389,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 3389,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "2340979087",
            "GroupId": "sg-9768976243",
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
            "VpcId": "vpc-987687665"
        },
        {
            "Description": "default VPC security group",
            "GroupName": "default",
            "IpPermissions": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": [
                        {
                            "GroupId": "sg-9986795",
                            "UserId": "23458792364"
                        }
                    ]
                },
                {
                    "FromPort": 22,
                    "IpProtocol": "tcp",
                    "IpRanges": [],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 22,
                    "UserIdGroupPairs": [
                        {
                            "GroupId": "sg-29348765",
                            "UserId": "23458792364"
                        }
                    ]
                },
                {
                    "FromPort": 21,
                    "IpProtocol": "tcp",
                    "IpRanges": [],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 21,
                    "UserIdGroupPairs": [
                        {
                            "Description": "ftp",
                            "GroupId": "sg-2345234",
                            "UserId": "23458792364"
                        }
                    ]
                },
                {
                    "FromPort": 3306,
                    "IpProtocol": "tcp",
                    "IpRanges": [],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 3306,
                    "UserIdGroupPairs": [
                        {
                            "Description": "Description from user",
                            "GroupId": "sg-878765765",
                            "UserId": "23458792364"
                        }
                    ]
                }
            ],
            "OwnerId": "23458792364",
            "GroupId": "sg-87687875",
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
            "VpcId": "vpc-2453098"
        }
    ],
    "ResponseMetadata": {
        "RequestId": "3563456-7345-756-243523-365364563",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "3563456-7345-756-243523-365364563",
            "content-type": "text/xml;charset=UTF-8",
            "transfer-encoding": "chunked",
            "vary": "accept-encoding",
            "date": "Thu, 04 Jun 2020 19:59:18 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}'''

    def get_json_string_sgs(self) -> str:
        return '''{
            "SecurityGroups": [
                {
                    "Description": "Allows access to http protocol",
                    "GroupName": "allow-http",
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
                    "OwnerId": "2039845702934",
                    "GroupId": "sg-092498379087908",
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
                            "Value": "Allow http"
                        }
                    ],
                    "VpcId": "vpc-857654764"
                }
            ],
            "ResponseMetadata": {
                "RequestId": "35463456-3456-7456-23452-2452234",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid": "35463456-3456-7456-23452-2452234",
                    "content-type": "text/xml;charset=UTF-8",
                    "content-length": "1697",
                    "date": "Sat, 06 Jun 2020 18:58:04 GMT",
                    "server": "AmazonEC2"
                },
                "RetryAttempts": 0
            }
        }'''

    def get_json_string_filtered_sgs(self, security_group_name: str) -> str:
        if security_group_name == "allow-http":
            return self.get_json_string_sgs()
        raise Exception()

    def get_json_string_filtered_sgs_by_id(self, security_group_id: str) -> str:
        if security_group_id == "sg-092498379087908":
            return self.get_json_string_sgs()
        raise Exception()

    def get_string_single_ip_permission(self) -> str:
        return '''{
    "FromPort": 22,
    "IpProtocol": "tcp",
    "IpRanges": [
        {
            "CidrIp": "210.64.32.200/32"
        }
    ],
    "Ipv6Ranges": [],
    "PrefixListIds": [],
    "ToPort": 22,
    "UserIdGroupPairs": []
}'''

    def get_json_vpcs_string(self) -> str:
        return '''{
  "Vpcs": [
    {
      "CidrBlock": "121.24.0.0/16",
      "DhcpOptionsId": "dopt-1234abcd",
      "State": "available",
      "VpcId": "vpc-abcd1234",
      "OwnerId": "10293806345",
      "InstanceTenancy": "default",
      "CidrBlockAssociationSet": [
        {
          "AssociationId": "vpc-cidr-assoc-1234abcd",
          "CidrBlock": "121.24.0.0/16",
          "CidrBlockState": {
            "State": "associated"
          }
        }
      ],
      "IsDefault": true
    }
  ],
  "ResponseMetadata": {
    "RequestId": "abcd1234-abcd1234-abcd1234-abcd1234",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "abcd1234-abcd1234-abcd1234-abcd1234",
      "content-type": "text/xml;charset=UTF-8",
      "content-length": "959",
      "date": "Thu, 30 Jul 1820 20:33:00 GMT",
      "server": "AmazonEC2"
    },
    "RetryAttempts": 0
  }
}'''

    def get_multiple_vpcs_response(self) -> str:
        return '''{
    "Vpcs": [
        {
            "CidrBlock": "201.32.1.1/28",
            "DhcpOptionsId": "dopt-affacddb",
            "State": "available",
            "VpcId": "vpc-71d99e528f6bdc8d2",
            "OwnerId": "505304424871",
            "InstanceTenancy": "default",
            "CidrBlockAssociationSet": [
                {
                    "AssociationId": "vpc-cidr-assoc-7706dd189b7c817d0",
                    "CidrBlock": "98.171.1.1/14",
                    "CidrBlockState": {
                        "State": "associated"
                    }
                }
            ],
            "IsDefault": true
        },
        {
            "CidrBlock": "23.4.1.77/27",
            "DhcpOptionsId": "dopt-98edb585",
            "State": "available",
            "VpcId": "vpc-a30ff249b44e63bfe",
            "OwnerId": "505304424871",
            "InstanceTenancy": "default",
            "CidrBlockAssociationSet": [
                {
                    "AssociationId": "vpc-cidr-assoc-2c0b4be471b88f658",
                    "CidrBlock": "231.90.91.22/25",
                    "CidrBlockState": {
                        "State": "associated"
                    }
                }
            ],
            "IsDefault": false,
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Unamed"
                }
            ]
        }
    ],
    "ResponseMetadata": {
        "RequestId": "332b77f8-9aeb-29b4-cf55-1b5ebcdefade",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "332b77f8-9aeb-29b4-cf55-1b5ebcdefade",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "content-type": "text/xml;charset=UTF-8",
            "content-length": "1876",
            "date": "Thu, 31 Dec 2020 17:26:11 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}'''

    def get_string_response_after_security_group_creation(self) -> str:
        return '''{
    "GroupId": "sg-c8ccc93558277d449",
    "ResponseMetadata": {
        "RequestId": "4e3cdc20-141a-24b9-8e2b-601390aab01e",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "4e3cdc20-141a-24b9-8e2b-601390aab01e",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "content-type": "text/xml;charset=UTF-8",
            "content-length": "11231",
            "date": "Thu, 31 Dec 2020 22:11:49 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}'''
