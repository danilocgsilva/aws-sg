# Creates Security Group With Rules

A security group without rules are useless. So, type:
```
aws --create <my-securyt-group-name-prefix> --ip 0.0.0.0 --protocol tcp --port 1234
```
