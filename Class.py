##############################################
#              Ultis_Gaurav                  #
#          ALL code by Gaurav.Shukla         #
#               v:0.1(01/03/2023)            #
##############################################
import time  # gives access to the time module
import scratchconnect  # gives access to the Scratch Connect module
import speech_recognition as sr  # gives access to the Speech recognition module
import pyttsx3  # gives access to the Pyttsx3 module
from chatterbot import ChatBot  # gives access to the Chatterbot module
from chatterbot.trainers import ChatterBotCorpusTrainer  # gives access to the chatterbot trainer dataset

r = sr.Recognizer()  # initialises the Recogniser Function (no arguments) in the sr(Speech Recognition) Class
Gaurav = ChatBot("Gaurav")  # initialises the ChatBot Class with 1 parameter/argument name which is set to the string Gaurav and  this is set to the variable assigned Gaurav
trainer = ChatterBotCorpusTrainer(Gaurav)  # initialises the ChatterBotCorpustrainer Class with 1 parameter/argument -the Chatbot class- this is set to the variable assigned Trainer
trainer.train("chatterbot.corpus.english")  # trainer(a variable) which has an attribute of train which is a function in the ChatterBotCorpusTrainer Class with 1 argument type string


def SpeakText(command):  # a function/Subroutine named SpeakText with 1 argument command the def keyword is used to define the function
    engine = pyttsx3.init()  # initialises the init()subroutine and sets it to the variable assigned as engine
    engine.say(command)  # engine(a variable) which has an attribute of say which is a function in the pyttsx3 module with 1 argument type string command
    engine.runAndWait()  # engine(a variable) which has an attribute of runAndWait which is a function in the pyttsx3 module with 1 argument self


def receive():  # a function/Subroutine named SpeakText  def keyword is used to define the function
    try:  # Tries the following code check for errors that might be raised
        with sr.Microphone() as source2:  # calls the Microphone() function /attribute as keyword used to give a temporary name for example source2
            r.adjust_for_ambient_noise(source2, duration=0.2)  # calls the adjust_for_ambient_noise function with 2 arguments microphone source ,duration
            audio2 = r.listen(source2)  # calls the listen function with 1 argument microphone also known as source2 and is set to the variable assigned audio2
            MyText = r.recognize_google(audio2)  # calls the recognize_google function with one argument which is the sound input this function coverts the sound input into text using the Google Ai model and sets the variable assigned Mytext
            MyText = MyText.lower()  # first the Mytext has an  attribute lower which makes it lower case, and then it is set to the variable assigned Mytext
            return MyText  # returns the Mytext Variable

    except sr.RequestError:  #  the except keyword tells the computer how to handle a RequestError only used with the try function
        return "NO INPUT"  #  Returns a string called NO INPUT

    except sr.UnknownValueError:  # the except keyword tells the computer how to handle a UnknownValueError only used with the try function
        return "NO INPUT"  #  Returns a string called NO INPUT


def find(word, var):  #  a function/Subroutine named find  def keyword is used to define the function with 2 parameters word and var standing for keyword and data set
    WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
    ret = 0   # initialises a variable assigned ret indicates that it is going to be an integer
    new_word = ""  #  initialises a variable assigned new_word indicates that it is going to be a string
    speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
    for i in range(len(var)):  # a for loop that is going to repeat length of var
        item = var[i]  # sets variable assigned item to the  i character of var
        WORD = WORD + item  # sets variable assigned WORD to itself + variable item
        if item == "'":  # an if statement that activates the tabbed code under if the statement is true
            if speech_marks == 1:  # an if statement that activates the tabbed code under if the statement is true
                if WORD == "'" + word + "'":  # an if statement that activates the tabbed code under if the statement is true
                    speech_marks = 0   # initialises a variable assigned speech_marks indicates that it is going to be an integer
                    WORD = ""  #  initialises a variable assigned WORD indicates that it is going to be a string
                    ret = 1  # sets variable assigned ret to  1
                elif ret == 1:  # else if statement
                    for i in range(len(WORD)):  # a for loop that is going to repeat length of WORD
                        letter = WORD[i]  # sets variable assigned letter to the  i character of WORD
                        if letter != "'":  # an if statement that activates the tabbed code under if the statement is true
                            new_word = new_word + letter   # sets variable assigned new_word to itself + variable letter
                    return new_word  # returns the variable assigned new_word
                else:  # else statement that only gets activated if the other statements are false
                    speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
                    WORD = ""  #  initialises a variable assigned WORD indicates that it is going to be a string
            else:  # else statement that only gets activated if the other statements are false
                speech_marks = 1  # sets the variable assigned speech_marks to integer value 1


class Utils_Gaurav: # creates class Utils_Gaurav
    def __init__(self): # tells the program what to do when the Utils_Gaurav class has been initialised
        print("---GAURAV'S UTILS FUNCTION---")  # prints a string
        self.user = scratchconnect.ScratchConnect("__BIT__", "Lakshya123@")  # logs into a Scratch User to Give us access to all Scratch Features
        self.project = self.user.connect_project(project_id=778517371)  # Accesses the Project using project id
        self.Variables = self.project.connect_cloud_variables()  # Connect the project's cloud variables
        self.Event = self.Variables.create_cloud_event()  # Create a cloud  event
        self.communications_line = "Cloud"  # Sets the Communications line with the Project To the string Cloud we need an identical Cloud Variable in Scratch to interact and share data

    def INPUT(self, prompt, type, data):  # Input function with  4 parameters prompt,type and data + self
        if type == "Basic":  # an if statement that activates the tabbed code under if the statement is true
            return input(str(prompt))  # returns the answer to the question
        elif type == "MO":  # Multiple Options (else if statement)
            print(str(prompt))   # prints the answer to the question
            for i in range(len(list(data))):  # a for loop that is going to repeat length of data
                print(f"OPTION {i + 1}: {data[i]}")   # prints the Options of the question so user can answer
            return input("PICK OPTION: ")  # returns the answer to the question

    def Print(self, txt, delay):  # Print function with 3 parameters txt,delay and self
        for char in txt: # a for loop that is going to repeat length of txt
            print(char, end='', flush=True)  # prints each character on same line
            time.sleep(delay)  # uses the time function to delay in seconds

    def ChatBot(self, txt): # Chatbot function with 2 parameters txt and self
        return Gaurav.get_response(txt)  # returns response to the txt input using the get response attribute of Gaurav

    def Stream_chatbot_out_to_Scratch(self):  # A function that allows for chatbots in scratch

        @self.Event.on("connect")  # triggers the code under if true
        def connect():  # function called connect
            print("Connection established starting data sharing")  # prints to terminal a string
            encoded_string = self.Variables.encode("Server Listening...")  # Encode a string
            self.Variables.set_cloud_variable(variable_name=self.communications_line, value=encoded_string)  # Sends Encoded String

        @self.Event.on("set")  # triggers the code under if true
        def set(data):  # function called set with 1 argument data
            m = str(data["variable_name"])  # sets variable assigned m {short form for message}  to the variable name in the dictionary named data
            if str(data["user"]) != "__BIT__":  # an if statement that activates the tabbed code under if the statement is true
                encoded = data["value"]  # sets variable assigned encoded to value in the data dictionary
                message = self.Variables.decode(encoded)  # sets variable assigned message to the decoded data sent from Scratch
                function = find("function", message)  # sets variable assigned function to the return value form the find function with string "function" and message given as parameter
                if function == "stream":  # an if statement that activates the tabbed code under if the statement is true
                    new_data = find("DATA", message)  # sets variable assigned new_data to the return value form the find string "DATA" and message given as parameter
                    encoded_string = self.Variables.encode(Gaurav.get_response(new_data))  # Encode a string
                    self.Variables.set_cloud_variable(variable_name=self.communications_line, value=encoded_string)  # sets cloud Variable to encoded_String
                else:  # else statement that only gets activated if the other statements are false
                    print("NOT STREAM")  # prints string Not Streaming
                    encoded_string = self.Variables.encode("NOT Correct format")  # Encode a string
                    self.Variables.set_cloud_variable(variable_name=self.communications_line, value=encoded_string)  # sets cloud Variable to encoded_String

        self.Event.start(update_time=0.01)  # starts the cloud event

    def Gaurav(self):  # function named Gaurav with 1 parameter self
        while True:  # while statement set default to true meaning it will run infinite times
            txt = str(receive())  # sets the variable assigned txt to the string from return value from the receive() function
            if txt != "bye":  # an if statement that activates the tabbed code under if the statement is true
                SpeakText(Gaurav.get_response(txt))  # speaks the response from Gaurav the Chatbot given some text
            elif txt == "what is your name":  # else if statement
                SpeakText("Gaurav")  # speaks name Gaurav
            else:  # else statement that only gets activated if the other statements are false
                SpeakText("Bye")  # speaks text bye
                break  # breaks the infinite loop
                