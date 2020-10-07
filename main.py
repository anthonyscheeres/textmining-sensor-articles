
# importing os module
import os

from googletrans import Translator


import subprocess

# importing shutil module
import shutil

import os.path
import sys




def get_dir():
    dirpath = os.getcwd()
    foldername = os.path.basename(dirpath)
    #print("Directory name is : " + dirpath)
    return dirpath


def rename_alll(dir, x):
  
    for filename in os.listdir(dir):
        if filename.find(".py")==-1:
            #do stuff with the files
            print ("hi")






def get_mirror2(myString):

    if myString.find("[")!=-1:
        mySubString = myString[myString.find("["):myString.find("]")+1]

        return mySubString




def main():
    dir=get_dir()
    rename_alll(dir, x)



if __name__ == "__main__":

    main()