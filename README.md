# aws-sg (AWS Security Group)

An wrapper around aws cloud lib to facilitates some development tasks over the securities groups.

## Access resources directly from local development computer

Sometimes, you may need to make a database dump to your local computer. But your database is protected from web access by the security group.

Wouldn't be great if there's a command directly in your development computer that changes the rule from yours resource's security group to allow your acces from where are you? This problem will be addresses here.
