# Listing groups


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
git a