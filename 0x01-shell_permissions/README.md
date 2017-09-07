Learning permissions in linux

Descriptions of scripts
0:sends su with argument betty to switch to user betty
1:sends whoami command to print current user
2:sends touch command with hello as argument to create a file named hello with nothing in it(script 4-empty)
3:sends id command with -Gn commands -G for current groups and -n for names instead of numbers(script 2-groups)
4:sends chown with argument betty as owner and hello as file name(script 3-new_owner)
5:send chmod with u+x argument to give execute permission to the file owner to the hello file
6:send chmod with ug+x,o+r to the hello file.  ug+x gives execute to the file owner and group owner. o+r gives other users read permissions
7:send chmod with a+x to hello file. a+x gives all users execute permissions
8:send chmod with 007 to hello file. 007 gives no permissions to file owner or group owner but other users have full permissions
9:send chmod with 753 to hello file. 753 gives full permissions to file owner, read and execute to group owner, and write and execute permissions to other users
10:send chmod --reference=olleh hello copies permissions of file olleh to hello
11:send find ./* -type d -exec chmod a+x {} + finds all directories in the current working directory and sends that output to the chmod command to give them all execute permissions
12:send mkdir -m 751 dir_holberton makes a new directory called dir_holberton with the permissions 751
13:send chown :holberton hello changes the group to holberton
14:send chown betty:holberton hello changes the owner to betty and group to holberton
15:send chown -h betty:holberton _hello changes owner to betty and group to holberton on the symbolic link _hello
16:send find ./hello -user guilluame -exec chown betty {} + finds all files in current directory named hello that are owned by guilluame and sends those to chown command to change user to betty