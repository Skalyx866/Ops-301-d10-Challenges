#/bin/bash

#ask user for folder name
echo "Please enter a folder name"
read folder

#ask user for permissions they want
echo "Please enter permissions you want"
read permissions

#change permissions of folder
cd $folder
chmod $permissions *

#lists everything in the folder with changed permissions
ls -al