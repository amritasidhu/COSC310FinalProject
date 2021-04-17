# **COSC310-Interactive-Conversational-Agent**

## **Individual Project Based off Group 23**

This is Amrita Sidhu's Individual project working off from Group 23's Assignment 3. 
This project was created for COSC 310, and its goal is to create an interactive conversational agent that would take in sentence input from the user and would output an appropriate response. The ChatBot we created is based on the current Prime Minister of Canada, Justin Trudeau, who answers the user's questions based on his past, present, future and his relationships.

This ChatBot implentation uses deeplearning through tensorflow's and tflearn's APIs. The basic idea is that through tensorflow, we will create a probabilistic function based on our input data (intents.json) and use this to estimate which "tag" most appropriately fits our user's input. Using this "tag", we can simply output a random hardcoded response. For example, if the user is to input "hello", the bot will calculate which tag is most fitting to the user's input. This will be returned as a float, representing a precentage from 0-100. The bot then simply takes the MAX float and says that is the closest matching tag, and then grabs a random response belonging to the same tag, in this case the "greetings" tag. This is a good approach to the problem, as it allows the bot to work with fewer constraints and without handling only hardcoded inputs.

The idea behind using tensorflow is that with a fully inter-connected neural network, passing data through it will give us a probablity gradient for each of our responses and their belonging tags.  Using something similar to a one-hot-encoded pattern, tensorflow works based on an array of "0s", representing all the words we have included in our expected inputs. When the user passes in a string, we increment at the index of the matching word in this "0's" array to a "1". Using this we can pass it through our nodes and pop out a response.

We have also implemented some features to further enhance the user's experience and to improve the flow of conversation with the chat bot. A Graphical User Interfance(GUI) has been used in place of the terminal for input/output, so that the user has a more pleasant experience when talking with the bot. The bot also utilizes Stanford's CoreNLP Toolkit to make use of features such as Sentiment Analysis, which allows the bot to provide appropriate responses to statements that are not not present in the the question bank, and Part-of-speech(POS) tagging which helps the bot recognize certain key words as parts of speech(useful for performing other functions). Synonym recognition was also implemented with the use of NLTK's WordNet. This feature helps the bot understand a wider range of vocabulary and sentences while providing the correct response.

Further, this Chatbot now has two new implementations. It is now connected to 2 API's. A API is a Application Programming Interface, which allows me to connect this GUI to web applications and access and use their data. Specifically, I have connected to a Wikipedia API for the purpose of providing a definition and more information on the question the user asks the bot. This is done by it being linked with synonym recognition, and it giving a defintion based on the key word. Second, I have connected to a Google Translate API which allows the user to choose whether they would like to get a response in English, French, Punjabi. The user is able to just type in the language they would like for their responses to be in out of the three languages.
## **Downloading required APIs**
> ```install nltk```  https://www.nltk.org/install.html
>
> ```install tensorflow``` https://www.tensorflow.org/install
>
> ```install tflearn``` http://tflearn.org/installation/
>
> ```install numpy``` https://numpy.org/install/
>
> ```install pycorenlp``` https://pypi.org/project/pycorenlp/
>
> ```install googletrans``` https://pypi.org/project/googletrans/ 
>
> ```install wikipedia-API``` https://pypi.org/project/Wikipedia-API/
>
> ```install wikipedia``` https://pypi.org/project/wikipedia/

## **Google Maps Setting up**
## **Setting up**
* Clone the COSC310-Interactive-Conversational-Agent repository
* Open ```chatbot.py``` in your prefered Python IDE
* In the terminal enter:
> ```import nltk```
> 
> ```nltk.download('punkt')```
>
> ```nltk.download('wordnet')```

* Download the Stanford NLP Toolkit (CoreNLP) zip folder https://stanfordnlp.github.io/CoreNLP/
* Extract the zip file to one directory level above this project's folder
> For example, if your project folder is located at 
> ```C:\Users\USER\COSC310-INTERACTIVE-CONVERSATIONAL-AGENT```, then extract file to ```C:\Users\USER\```


## **Running**
* Compile and run stanfordload.py
* Compile and run gui.py


## **Files**
* **chatbot.py** *Has the chat function that returns bot's response to ```gui.py``` and calls ```load.py``` to create training data if none exists.*
* **load.py** *Loads in intents.json and processes the data into a trained tflearn model for a response based on a probabilty of the corresponding tag to the question asked*
* **intents.json** *Database of tags, patterns, and responses.*
* **data.pickle** *Pickle file to store the processed files and not have to reprocesses them everytime*
* **model.tflearn** *tflearn models that have been stored as not to run the training algorithm everytime*
* **stanfordload.py** *Establishes connection to Stanford's CoreNLP Server*
* **gui.py** *Comprises of functions that make the GUI for the chat bot*
* **sentiment.py** *Contains functions that conduct sentiment analysis on the user's input statement using Stanford's CoreNLP Toolkit*
* **syn_recognition.py** *Contains functions that tag parts-of-speech in user's input, and creates different sentences with different combinations of synonyms*
* **test_chatbot.py** *Contains unit tests for major functions and classes to validate them*
* **googletranslateAPI.py** *Contains two functions, one which will translate response to French,and one which will translate response to Punjabi.*
**wikipediaAPI.py** *Contains a function that grabs defintion which is the first sentence, and two more sentences for further clarity if necessary.*


## **List of New Features**

### 7. Extract Knowledge from Main Keywords

This bot provides a definition and more information based on the key word from the question that the user asks the bot.

### 8. Translate Response

The user may choose to have the response they recieve from the bot translated to French or Punjabi. They can also change back to English, or switch between languages at any time. 

