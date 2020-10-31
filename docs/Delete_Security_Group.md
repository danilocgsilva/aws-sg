# Delete a security group

Want to delete some security group?
```
awssg --delete security_group_id
```

You may need to delete several securities groups at once. You can do separating several securiti groups names by comas:
```
awssg --delete <security_group_id1>,<security_group_id2>
```

If the available information is the name and not the security group id, then:
```
awssg --delete-name security_group_name
```
