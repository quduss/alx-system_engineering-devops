# 0X01-SHELL_PERMISSIONS
This directory contains bash scripts to test knowledge of permissions.
1. **0-iam_betty** - switches the current user to the user `betty`.
2. **1-who_am_i** - prints the effective username of the current user.
3. **2-groups** - prints all the groups the current user is part of.
4. **3-new_owner** - changes the owner of the file `hello` to the user `betty`.
5. **4-empty** - creates an empty file called `hello`.
6. **5-execute** - adds execute permission to the owner of the file `hello`.
7. **6-multiple_permissions** - adds execute permission to the owner and the group owner, read permission to other users, to the file `hello`.
8. **7-everybody** - adds execution permission to the owner, the group owner and the other users, to the file `hello`.
9. **8-James_Bond** - sets no permissions to owner and group but all permissions to other users to file `hello`.
10. **9-John_Doe** - sets the mode of file `hello` to `-rwxr-x-wx`.
11. **10-mirror_permissions** - sets the mode of the file `hello` the same as `olleh’s` mode.
12. 
