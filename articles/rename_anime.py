# importing os module
import os

import subprocess

# importing shutil module
import shutil

import os.path
import sys



print(sys.version)  # parentheses necessary in python 3.




def get_dir():
    dirpath = os.getcwd()
    foldername = os.path.basename(dirpath)
    print("Directory name is : " + dirpath)
    return dirpath

def remove_string(filename, subString, x):


   
    filearray=filename.split(subString, 1)
    this = "["+x+"]"+filearray[0]+filearray[-1]

    if filearray[0]==filearray[-1]:
        this = "["+x+"]"+filename

    
    
    return this


def renamethis(path, filename, new_file_name_with_ext):

    try:
        os.rename(os.path.join(path, filename), os.path.join(path, new_file_name_with_ext))
        print(filename + " --> succesfully created")


    except:
        print (filename +" file exists")

def try_all_icons(dir, x):

    for filename in os.listdir(dir):
        if filename.find(".")==-1:
            filePaths = dir +"\\"+ filename
            for file in os.listdir(filePaths):
                if file.find(".")!=-1:
                    dir1 = os.path.join(dir, filename)
                    rename_wrapper(file, dir1, x)



def retrieve_file_paths(dirName):
    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths



def rename_wrapper(filename, dir, x):
    subString=get_mirror(filename)
    new_file_name=remove_string(filename, subString, x)
    renamethis(dir, filename, new_file_name.lower().strip())


def rename_alll(dir, x):
  
    for filename in os.listdir(dir):
        if filename.find(".py")==-1:
            rename_wrapper(filename, dir, x)



def get_mirror(myString):

    if myString.find("[")!=-1:
        mySubString = myString[myString.find("["):myString.find("]")+1]

        return mySubString







def main():
    print('Enter your name:')
    x = input()
    
    dir=get_dir()
    rename_alll(dir, x)
    try_all_icons(dir, x)



if __name__ == "__main__":

    main()
