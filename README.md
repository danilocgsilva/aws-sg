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

## Usages

* [Listing securities groups](docs/List_Groups.md)
* [Creating a new security group](docs/Create_Security_Group.md)
* [Delete a security groups](docs/Delete_Security_Group.md)
* [Check rules from security group](docs/Check_rules_from_security_group.md)
* [Create a scurity group with rules](docs/Create_Security_Group_With_Rules.md)

