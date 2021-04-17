import wikipediaapi
import wikipedia


#search method: 
#print(wikipedia.search("Trudeau")) #gives various results that I would find on google if I searched on google

#simple search:
#print(wikipedia.summary("Justin Trudeau")) #grabs all info about Justin Trudeau and displays it like huge paragraph

#user input:
#value = input("user input"); #interactive, use in gui.py

#grabs content of page of user input: referenes, external links, everything 
#print(wikipedia.page(value.content)

#there is a sentence property: This will grab the amount of sentences specified, so you dont have a full page of data! 
#print(wikipedia.summary(value, sentences = 3))

#how to get external links:
#print(wikipedia.page(value).references)

#print(wikipedia.page(value).title)

#Here all I need to do is create a function that will grab a short summary from wikipedia based on what the user wants 

def forInformation(text):
    title = wikipedia.page(text).title
    info = wikipedia.summary(text, sentences=3)
    return info