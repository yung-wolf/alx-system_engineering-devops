
# Definitions of Scripts for Permissions Project

```bash
# change current user to user 'betty'
0-iam_betty

# prints the effective username of current user
1-who_am_i

# prints all the groups user is in
2-groups

# change owner of file 'hello' to 'betty'
3-new_owner

# create empty file 'hello'
4-empty

# adds execute permissions to 'hello' file
5-execute

# adds execute permissions to owner and group owners, and read permissions to other users
6-multiple_permissions

# adds execute permissions to user, group, others of 'hello' file
7-everybody

# sets no permissions to user and group, but all permissions to others of 'hello' file
8-James_Bond

# sets permissions of 'hello' file in a specific order
9-John_Doe

# set the permission of 'hello' file to that of 'olleh'
10-mirror_permissions

# add execute permissions to all subdirectories of current directory for user,group,others. Regular files excluded
11-directories_permissions

# create a dir in working directory and set permissions to 751
12-directory_permissions

# change group owner of 'hello' file to 'school'
13-change_group

# change the owner to 'vincent' and group to 'staff' for all files and directory in working directory
100-change_owner_and_group

# change the owner and group owner of '_hello' to vincent and staff respectively
101-symbolic_link_permissions
```
