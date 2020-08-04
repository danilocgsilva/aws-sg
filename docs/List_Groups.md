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

Want to get more information than just the id? So you have the option to prints together the name and the rules count.
```
awssg --fields name
awssg --fields rulescount
awssg --fields name,rulescount
```
Any of these formats works.
