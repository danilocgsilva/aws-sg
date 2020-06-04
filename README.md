# aws-sg (AWS Security Group)

An wrapper around aws cloud lib to facilitates some development tasks over the securities groups.

## Access resources directly from local development computer

Sometimes, you may need to make a database dump to your local computer. But your database is protected from web access by the security group.

Wouldn't be great if there's a command directly in your development computer that changes the rules from yours resource's security group to allow your acces from where are you? This problem will be addresses here.

## How to use:

Installing:

1. Go to the root project folder

2. Execute:
```
pip install .
```

Executing command:

```
awssg
```

By default, will lists all securities groups for each region.

You may want lists the security group from a single region. Then, type:

```
awssg --region <your_region>
```

Some environments may have several profiles configured. Or is required to get a profile name. In this case, you will need to provides the profile name:

```
awssg --profile <your_profile>
```

You may want to know a list of securities groups from a specific rds. Type:

```
awssg --rds <your_rds>
```

(NOT DEVELOPED YET) List the rules from some specific security group:

```
awssg --rules-from <security_group_id>
```
