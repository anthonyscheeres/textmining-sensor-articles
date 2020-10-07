
# importing os module
import os

from googletrans import Translator
import PyPDF2 

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


def rename_alll(pathToPdf, pathToOutput, x):
  
    for filename in os.listdir(pathToPdf):
        if filename.find(".py")==-1:
            #do stuff with the files


            text = []

          

            text=  read_text(dir + filename)

            textEnglish = filter_text(text)

            textDutch = translate_text(textEnglish)

            append_text_file(textDutch, pathToOutput)





def append_text_file(text, x):
    with open(x, "a") as myfile:
        myfile.write(text)


def filter_text(textArray):



    for index in textArray:
        
        textPage = textArray(index)

        text = null

        while get_mirror2(textPage) !=null:
            sub = get_mirror2(textPage)
            textPage.remove(sub)


        text = text + textPage

        if "2." in textPage:
            break

        
    return text


def translate_text(text):
    translator = Translator()
    return translator.translate(text, dest="nl", src="en")


def read_text(path):

    # creating a pdf file object 
    pdfFileObj = open(path, 'rb') 
  
# creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    textArray =[]

    for page in pdfReader.numPages:
        # creating a page object 
        pageObj = pdfReader.getPage(page) 
        # extracting text from page 
        textArray.append(pageObj.extractText())


    return textArray;
  



# closing the pdf file object 
    pdfFileObj.close() 


    return text



def get_mirror2(myString):

    if myString.find("[")!=-1:
        mySubString = myString[myString.find("["):myString.find("]")+1]

        return mySubString




def main():

    x = "output.txt"
    dir=get_dir()

    pathToPdf = dir +"//articles//"

    pathToOutput = dir + "//"+x

    rename_alll(pathToPdf, pathToOutput, x)



if __name__ == "__main__":

    main()