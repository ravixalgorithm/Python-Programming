# Ques4: Print all the folders in a directory
# Ques5: Comment all the steps in Ques4
import os

#specify the directory you want to list
directory_path = '/'

#List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)