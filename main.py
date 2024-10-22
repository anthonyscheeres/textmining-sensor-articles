
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
  
    number = 1

    for filename in os.listdir(pathToPdf):



        print (filename)
        if filename.find(".py")==-1:
            #do stuff with the files


            text = []
          


            text=  read_text(pathToPdf + filename)


        

            textEnglish = filter_text(text, number)



            try:
                textDutch = translate_text(textEnglish)
                append_text_file(textDutch, pathToOutput)
                number = number + 1 
            except:
                print ("oops")



def get_header(myString):

    mySubString = myString[myString.find("20"):myString.find("www.mdpi.com/journal/")]


    return mySubString

def get_introduction(myString):
     mySubString = myString[myString.find("Introduction"):myString.find("2.")]
     return mySubString



def append_text_file(text, x):
    with open(x, "a", encoding="utf-8") as myfile:
        myfile.write(text)
        myfile.close()


def check_is_none(text):
    return text!=None



def get_title(myString):

    firstPage = myString[0]


    subString = firstPage[firstPage.find("\n"):-1]

    return subString


def filter_text(textArray, number ):
    
    text = "Sensor technologie gerelateerd artikel nummer "+str(number) + get_title(textArray)  

    


    for textPage in textArray:

        textPage = get_introduction(textPage)

        
        sub2 = ""
        
        sub2 = get_header(textPage)


        if check_is_none(sub2):
            textPage = textPage.replace(sub2, "")

        
        while check_is_none(get_mirror2(textPage)):

            sub = ""
           
     

            sub = get_mirror2(textPage)

         


         


            if check_is_none(sub):
                textPage = textPage.replace(sub, "")


           

        text = text + textPage

        if "2." in textPage:
            break

        
    return text


def translate_text(text):
    translator = Translator()
    return translator.translate(text, dest="nl", src="en").text


def read_text(path):

    # creating a pdf file object 
    pdfFileObj = open(path, 'rb') 
  
# creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    textArray =[]

    for page in range(pdfReader.numPages):
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

    if not os.path.exists(pathToPdf):
        os.makedirs(pathToPdf)


    pathToOutput = dir + "//"+x

    rename_alll(pathToPdf, pathToOutput, x)



if __name__ == "__main__":

    main()