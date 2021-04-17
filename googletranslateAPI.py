import googletrans
from googletrans import Translator #importing the translator
#print(googletrans.LANGUAGES) #shows us all possible languages. We will be using French since that is the second language of Canada. 

#creating a translator object:


#we have to create a function that will take in the user input and return a response in french

def toFrench(text):
    responseInFrench = Translator.translate(text, dest = 'fr')
    #Have to return with .text!!
    return responseInFrench.text 

#we have to create a function that will take in the user input and return a response in punjabi

def toPunjabi(text):
    responseInPunjabi = Translator.translate(text, dest = 'pa')
    #Have to return with .text!!
    return responseInPunjabi.text 

