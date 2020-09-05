# Creates Security Group With Rules

A security group without rules are useless. So, type:
```
awssg --create <my-securyt-group-name-prefix> --ip 0.0.0.0 --protocol tcp --port 1234
```
You can create a security group with the current external ip, so the securlity group allows just your ip to access AWS resources, but you will need the [wimi-api](https://github.com/danilocgsilva/wimi-api) package to set working.

After that, you can do the following:
```
awssg --create <my-securyt-group-name-prefix> --ip mine --protocol tcp --port 1234
```
