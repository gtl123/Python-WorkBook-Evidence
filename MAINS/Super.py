##############################################
#              Ultis_Gaurav                  #
#          ALL code by Gaurav.Shukla         #
#               v:3.0(15/03/2023)            #
#              CC0 license applies           #
##############################################

import time  # imports the time module
import speech_recognition as sr  # imports the speech recognition module and renames it to sr
import pyttsx3  # imports the pyttsx3 module
from chatterbot import ChatBot  # imports the ChatBot class from the chatterbot module
from chatterbot.trainers import ChatterBotCorpusTrainer  # imports the ChatterBotCorpusTrainer class from the chatterbot.trainers module
from random import *  # imports all functions from the random module
from MAINS.country_info import countries  # imports countries from country_info module
from MAINS.items import items  # imports items from items module

class UtilsGaurav:  # defines a new class called UtilsGaurav
    def __init__(self, ai, scratch):  # defines an __init__ method that takes in two arguments: AI and scratch
        if ai == True:  # checks if Ai is True
            self.Ai_Enabled = True  # sets Ai_Enabled attribute to True
            self.r = sr.Recognizer()  # creates a new instance of Recognizer and assigns it to r attribute
            self.Gaurav = ChatBot("Gaurav")  # creates a new instance of ChatBot with name "Gaurav" and assigns it to Gaurav attribute
            self.trainer = ChatterBotCorpusTrainer(self.Gaurav)  # creates a new instance of ChatterBotCorpusTrainer with Gaurav as argument and assigns it to trainer attribute
            self.trainer.train("chatterbot.corpus.english")  # trains trainer with "chatterbot.corpus.english" corpus
        if scratch == True:  # checks if scratch is True
            self.Scratch_Enabled = True  # sets Scratch_Enabled attribute to True
            import scratchconnect   # gives access to the Scratch Connect module by importing it locally within this block of code only.
            self.user = scratchconnect.ScratchConnect("Insert user", "insert password")   ## creates an instance of ScratchConnect class with username and password as arguments and assigns it to user attribute.
            self.project = self.user.connect_project(project_id=778517371)   ## connects project with id=778517371 using connect_project method on user object and assigns returned value to project attribute.
            self.Variables = self.project.connect_cloud_variables()   ## connects cloud variables using connect_cloud_variables method on project object and assigns returned value to Variables attribute.
            self.Event = self.Variables.create_cloud_event()   ## creates cloud event using create_cloud_event method on Variables object and assigns returned value to Event attribute.
            self.communications_line = "Cloud"   ## sets communications_line attribute value as "Cloud".
        else:
            self.Scratch_Enabled = False   ## sets Scratch_Enabled attribute value as False when scratch argument is not true.
         #print("---GAURAV'S UTILS FUNCTION---")   ## prints string "---GAURAV'S UTILS FUNCTION---".

    def Roll(self, d):   ## defines Roll method that takes in one argument d.
        import random    ## gives access to random module by importing it locally within this block of code only.
        return random.randint(1, int(d))    ## returns a random integer between 1 and d (inclusive) using randint function from random module.

    def SpeakText(self, command):  # defines a method called SpeakText that takes in one argument: command
        if self.Ai_Enabled == True:  # checks if Ai_Enabled attribute is True
            engine = pyttsx3.init()  # creates a new instance of pyttsx3 engine and assigns it to engine variable
            engine.say(command)  # calls say method on engine object with command as argument to queue up the text to be spoken
            engine.runAndWait()  # calls runAndWait method on engine object to process the command queue and speak the text
        else:
            raise IOError("Function_Disabled")  # raises an IOError with message "Function_Disabled" if Ai_Enabled attribute is not True

    def find(self, word, var):  # defines a method called find that takes in two arguments: word and var
        WORD = ""  # initializes an empty string and assigns it to WORD variable
        ret = 0  # initializes ret variable with value 0
        new_word = ""  # initializes an empty string and assigns it to new_word variable
        speech_marks = 0   ## initializes speech_marks variable with value 0.
        for i in range(len(var)):   ## iterates over each character index in var string.
            item = var[i]   ## gets character at index i from var string and assigns it to item variable.
            WORD = WORD + item   ## concatenates item character to WORD string.
            if item == "'":   ## checks if item character is single quote (').
                if speech_marks == 1:   ## checks if speech_marks value is equal to one.
                    if WORD == "'" + word + "'":   ## checks if WORD value is equal to single quote concatenated with word concatenated with single quote.
                        speech_marks = 0   ## sets speech_marks value as zero when above condition is true.
                        WORD = ""    ## sets WORD value as empty string when above condition is true.
                        ret = 1    ## sets ret value as one when above condition is true.
                    elif ret == 1:    ## checks if ret value is equal to one when above condition was false but previous conditions were true.
                        for i2 in range(len(WORD)):    ## iterates over each character index in WORD string.
                            letter = WORD[i2]    ## gets character at index i2 from WORD string and assigns it to letter variable.
                            if letter != "'":    ## checks if letter character is not single quote (').
                                new_word = new_word + letter    ## concatenates letter character to new_word string when above condition was true.
                        return new_word     ### returns new_word value after processing all characters of current iteration of outer loop.
                    else:
                        speech_marks = 0     ### sets speech_marks value as zero when all previous conditions were false.
                        WORD = ""     ### sets WORD value as empty string when all previous conditions were false.
                else:
                    speech_marks = 1   ## sets speech_marks value as one when first inner condition was false but second inner condition was true.

    def receive(self):  # defines a method called receive that takes no arguments
        if self.Ai_Enabled == True:  # checks if Ai_Enabled attribute is True
            try:  # starts a try block to catch exceptions
                with sr.Microphone() as source2:  # creates a new instance of Microphone and assigns it to source2 variable using context manager
                    self.r.adjust_for_ambient_noise(source2, duration=0.2)  # calls adjust_for_ambient_noise method on r attribute object with source2 and duration=0.2 as arguments to calibrate the energy threshold for ambient noise levels
                    audio2 = self.r.listen(source2)  # calls listen method on r attribute object with source2 as argument to capture audio data from the microphone and assigns returned AudioData object to audio2 variable
                    MyText = self.r.recognize_google(audio2)  # calls recognize_google method on r attribute object with audio2 as argument to perform speech recognition on audio data using Google Web Speech API and assigns returned text to MyText variable
                    MyText = MyText.lower()  # converts all characters in MyText string to lowercase using lower method and assigns returned string back to MyText variable
                    return MyText  # returns MyText value

            except sr.RequestError:   ## catches RequestError exception raised by speech_recognition module.
                return "NO INPUT"   ## returns string "NO INPUT" when above exception was caught.

            except sr.UnknownValueError:   ## catches UnknownValueError exception raised by speech_recognition module.
                return "NO INPUT"   ## returns string "NO INPUT" when above exception was caught.
        else:
            raise IOError("Function_Disabled")   ## raises IOError with message "Function_Disabled" when Ai_Enabled attribute value was not true.

    def INPUT(self, prompt, types, data, func):  # defines a method called INPUT that takes in four arguments: prompt, types, data and func
        if types == "Basic":  # checks if types argument value is equal to string "Basic"
            return input(str(prompt))  # calls input function with prompt argument converted to string as argument and returns its value
        elif types == "MO":  # checks if types argument value is equal to string "MO"
            print(str(prompt))  # prints prompt argument converted to string
            for i in range(len(list(data))):   ## iterates over each index of data list.
                print(f"OPTION {i + 1}: {data[i]}")   ## prints formatted string with index plus one and corresponding element from data list.
            return input("PICK OPTION: ")   ## calls input function with string "PICK OPTION: " as argument and returns its value.
        elif types == "ME":   ## checks if types argument value is equal to string "ME".
            print(str(prompt))   ## prints prompt argument converted to string.
            count = 0   ## initializes count variable with zero.
            answers = []   ## initializes an empty list and assigns it to answers variable.
            result = 0    ### initializes result variable with zero.
            while count != int(data[0]):    ### iterates until count value is not equal to first element of data list converted to integer.
                answers.append(input(":"))    ### calls input function with colon (:) as argument and appends its returned value to answers list.
                result = func(answers)    ### calls func function with answers list as argument and assigns its returned value to result variable.
                count += 1    ### increments count variable by one after each iteration.
            OUT = []     #### initializes an empty list and assigns it to OUT variable.
            if data[1] == "str":     #### checks if second element of data list is equal to string "str".
                for obj in answers:     #### iterates over each element in answers list.
                    OUT.append(str(obj))     #### converts current element from answers list into a string using str function and appends it into OUT list.
                result = str(result)     #### converts result variable into a string using str function and assigns it back into result variable when above condition was true.
            elif data[1] == "int":     #### checks if second element of data list is equal to string "int".
                for obj in answers:     #### iterates over each element in answers list when above condition was true.
                    OUT.append(int(obj))     #### converts current element from answers list into an integer using int function and appends it into OUT list when above condition was true.
                result = int(result)     #### converts result variable into an integer using int function and assigns it back into result variable when above condition was true.
            elif data[1] == "float":     ##### checks if second element of data list is equal to string "float".
                for obj in answers:      ##### iterates over each element in answers list when above condition was true.
                    OUT.append(float(obj))      ##### converts current element from answers list into a float using float function and appends it into OUT list when above condition was true.
                result = float(result)      ##### converts result variable into a float using float function and assigns it back into result variable when above condition was true.
            if func == self.NONE:      ##### checks if func argument value is equal self.NONE attribute value.
                return OUT      ##### returns OUT value when above condition was true.
            else:  # if func argument value is not equal to self.NONE attribute value
                return result  # returns result value
        elif types == "Custom":  # checks if types argument value is equal to string "Custom"
            count = 1  # initializes count variable with value 1
            answers = []  # initializes an empty list and assigns it to answers variable
            result = 0  ## initializes result variable with zero.
            while count != int(
                    len(data)):  ## iterates until count value is not equal to length of data dictionary converted to integer.
                answers.append(input(data[str(count)]))  ## calls input function with value from data dictionary at key equal to count variable converted into a string as argument and appends its returned value into answers list.
                result = func(answers)  ## calls func function with answers list as argument and assigns its returned value into result variable.
                count += 1  ## increments count variable by one after each iteration.
            OUT = []  ### initializes an empty list and assigns it to OUT variable.
            if data["type"] == "str":  ### checks if value from data dictionary at key "type" is equal to string "str".
                for obj in answers:  ### iterates over each element in answers list when above condition was true.
                    OUT.append(str(obj))  ### converts current element from answers list into a string using str function and appends it into OUT list when above condition was true.
                result = str(result)  ### converts result variable into a string using str function and assigns it back into result variable when above condition was true.
            elif data["type"] == "int":  #### checks if value from data dictionary at key "type" is equal to string "int".
                for obj in answers:  #### iterates over each element in answers list when above condition was true.
                    OUT.append(int(obj))  #### converts current element from answers list into an integer using int function and appends it into OUT list when above condition was true.
                result = int(result)  #### converts result variable into an integer using int function and assigns it back into result variable when above condition was true.
            elif data["type"] == "float":  ##### checks if value from data dictionary at key "type" is equal to string "float".
                for obj in answers:  ##### iterates over each element in answers list when above condition was true.
                    OUT.append(float(obj))  ##### converts current element from answers list into a float using float function and appends it into OUT list when above condition was true.
                result = float(result)  ##### converts result variable into a float using float function and assigns it back into result variable when above condition was true.
            if func == self.NONE:  # checks if func argument value is equal to self.NONE attribute value
                return OUT  # returns OUT value when above condition was true
            else:  # if func argument value is not equal to self.NONE attribute value
                return result  # returns result value

    def multiply_list(self,answers):  # defines a method called multiply_list that takes in two arguments: self and answers
        result = 1  # initializes result variable with value 1
        for answer in answers:  # iterates over each element in answers list
            result *= int(answer)  # multiplies result variable by current element from answers list converted into an integer using int function and assigns it back into result variable
        return result  # returns result value

    def add_list(self,answers):   ## defines a method called add_list that takes in two arguments: self and answers.
        result = 0   ## initializes result variable with zero.
        for answer in answers:   ## iterates over each element in answers list.
            result += int(answer)   ## adds current element from answers list converted into an integer using int function to the value of result variable and assigns it back into result variable.
        return result   ## returns the final value of the result variable.

    def minus_list(self,answers):    ### defines a method called minus_list that takes in two arguments: self and answers.
        result = 0    ### initializes the value of the local variable named 'result' to zero.
        if len(answers) > 1:    ### checks if length of 'answers' list is greater than one.
            result = int(answers[0])    ### converts first element from 'answers' list into an integer using int function and assigns its value to 'result' when above condition was true.
            for answer in answers:     #### iterates over each element from 'answers' list when above condition was true.
                if answers.index(answer) != 0:     #### checks if index of current element from 'answers' list is not equal to zero when above condition was true.
                    result -= int(answer)     #### subtracts current element from 'answers' list converted into an integer using int function from the value of 'result' variable and assigns it back into 'result' variable when above condition was true.
        return result     ##### returns final value of the local variable named 'result'.

    def NONE(self,*txt):      ##### defines a method called NONE that takes in at least one argument (self) and any number of additional arguments (*txt).
        return 0      ##### returns zero as output.

    def Print(self, txt, delay):  # defines a method called Print that takes in three arguments: self, txt and delay
        for char in txt:  # iterates over each character in txt string
            print(char, end='', flush=True)  # prints current character from txt string on same line without adding a newline character at the end and flushes the output buffer immediately
            time.sleep(delay)  # calls sleep function from time module with delay argument value as argument to pause execution for specified number of seconds
        print("", end="\n", flush=False)  # prints an empty string followed by a newline character without flushing the output buffer immediately

    def ChatBot(self, txt):   ## defines a method called ChatBot that takes in two arguments: self and txt.
        if self.Ai_Enabled == True:   ## checks if Ai_Enabled attribute value is equal to boolean True.
            return self.Gaurav.get_response(txt)   ## calls get_response method from Gaurav attribute with txt argument value as argument and returns its returned value when above condition was true.
        else:   ### executes when above condition was false.
            raise IOError("Function_Disabled")   ### raises an IOError exception with message "Function_Disabled" when above condition was false.

    def Stream_chatbot_out_to_Scratch(self):  # defines a method called Stream_chatbot_out_to_Scratch that takes in one argument: self
        if self.Ai_Enabled == True and self.Scratch_Enabled == True:  # checks if both Ai_Enabled and Scratch_Enabled attribute values are equal to boolean True
            @self.Event.on("connect")  # registers an event handler for "connect" event using on method from Event attribute
            def connect():  # defines a nested function called connect that takes in no arguments
                print("Connection established starting data sharing")  # prints a string to standard output
                encoded_string = self.Variables.encode("Server Listening...")  # calls encode method from Variables attribute with string "Server Listening..." as argument and assigns its returned value into encoded_string variable
                self.Variables.set_cloud_variable(variable_name=self.communications_line, value=encoded_string)  # calls set_cloud_variable method from Variables attribute with variable_name argument value equal to communications_line attribute value and value argument value equal to encoded_string variable value
            @self.Event.on("set")  # registers an event handler for "set" event using on method from Event attribute
            def set(data):  # defines a nested function called set that takes in one argument: data
                if str(data["user"]) != "__BIT__":  # checks if value associated with "user" key in data dictionary converted into a string using str function is not equal to string "__BIT__"
                    encoded = data["value"]  # assigns value associated with "value" key in data dictionary into encoded variable
                    message = self.Variables.decode(encoded)  # calls decode method from Variables attribute with encoded variable value as argument and assigns its returned value into message variable
                    function = self.find("function", message)  # calls find method with string "function" and message variable value as arguments and assigns its returned value into function variable
                    if function == "stream":   ## checks if function variable value is equal to string "stream".
                        new_data = self.find("DATA", message)   ## calls find method with string "DATA" and message variable value as arguments and assigns its returned value into new_data variable when above condition was true.
                        encoded_string = self.Variables.encode(self.Gaurav.get_response(new_data))   ## calls get_response method from Gaurav attribute with new_data variable value as argument, then calls encode method from Variables attribute with above returned value as argument and assigns its returned value into encoded_string variable when above condition was true.
                        self.Variables.set_cloud_variable(variable_name=self.communications_line, value=encoded_string)   ## calls set_cloud_variable method from Variables attribute with variable_name argument value equal to communications_line attribute value and value argument equal to encoded_string variable when above condition was true.
                    else:   ### executes when above condition was false.
                        print("NOT STREAM")   ### prints string "NOT STREAM" to standard output when above condition was false.
                        encoded_string = self.Variables.encode("NOT Correct format")   ### calls encode method from Variables attribute with string "NOT Correct format" as argument and assigns its returned value into encoded_string variable when above condition was false.
                        self.Variables.set_cloud_variable(variable_name=self.communications_line, value=encoded_string)   ### calls set_cloud_variable method from Variables attribute with variable_name argument equal to communications_line attribute and the 'value' argument equal to the 'encoded_string' local variable.

                self.Event.start(update_time=0.01)  #### starts the cloud event by calling start() on Event object passing update_time parameter.

        else:    ##### executes when first if statement (if Ai_Enabled == True && Scratch_Enabled == True) is false.
            raise IOError("Function_Disabled Hint:Maybe Forgot to Set Ai to True")    ##### raises an IOError exception with a custom error message.

    def Gaurav(self):  # defines a method called Gaurav that takes in one argument: self
        if self.Ai_Enabled == True:  # checks if Ai_Enabled attribute value is equal to boolean True
            while True:  # enters an infinite loop
                txt = str(self.receive())  # calls receive method and converts its returned value into a string using str function and assigns it into txt variable
                if txt != "bye":  # checks if txt variable value is not equal to string "bye"
                    self.SpeakText(self.Gaurav.get_response(txt))  # calls get_response method from Gaurav attribute with txt variable value as argument and passes its returned value as argument into SpeakText method when above condition was true
                elif txt == "what is your name":   ## checks if txt variable value is equal to string "what is your name".
                    self.SpeakText("Gaurav")   ## calls SpeakText method with string "Gaurav" as argument when above condition was true.
                else:   ### executes when above conditions were false.
                    self.SpeakText("Bye")   ### calls SpeakText method with string "Bye" as argument when above conditions were false.
                    break   ### breaks out of the infinite loop when above conditions were false.

        else:    #### executes when first if statement (if Ai_Enabled == True) was false.
            raise IOError("Function_Disabled")    #### raises an IOError exception with message "Function_Disabled" when first if statement was false.

    def Money_to_Coins(self, *money):    ##### defines a method called Money_to_Coins that takes in one or more arguments using *money syntax.
        total_amount = 0    ##### initializes total_amount local variable to zero.
        for i in money:    ##### iterates over each element in money tuple.
            total_amount = total_amount + int(i)    ##### adds current element converted into an integer using int function into total_amount local variable and assigns the result back into total_amount local variable.
        T1 = total_amount // 20    ##### performs integer division of total_amount local variable by integer literal 20 and assigns the result into T1 local variable.
        total_amount = total_amount - (20 * T1)    ##### subtracts product of integer literals 20 and T1 from total_amount local variable and assigns the result back into total_amount local variable.
        T2 = total_amount // 10    ##### performs integer division of updated total_amount local variable by integer literal 10 and assigns the result into T2 local variable.
        total_amount = total_amount - (10 * T2)    ##### subtracts product of integer literals 10 and T2 from updated total_amount local variable and assigns the result back into it again.
        T3 = total_amount // 5     ###### performs integer division of updated again 'total amount' by integer literal '5' assigning result to 'T3'.
        total_amount = total_amount - (5 * T3)     ###### subtracts product of '5' times 'T3' from updated again 'total amount', assigning result back to itself again.
        T4 = total_amount // 2     ####### performs integer division on updated again 'total amount' by int literal '2', assigning result to 'T4'.
        return {"20": T1,
                "10": T2,
                "5": T3,
                "2": T4,
                "1": total_amount}      ######## returns dictionary object containing key-value pairs representing coin denominations mapped to their respective counts.

    def Country_Guessing_game(self):  # defines a method called Country_Guessing_game that takes in one argument: self
        selected_countries = []  # initializes an empty list and assigns it into selected_countries variable
        selected_capitals = []  # initializes an empty list and assigns it into selected_capitals variable
        for i in range(3):  # iterates over a range object that generates integers from 0 to 2 (inclusive)
            index = randint(0, len(countries)-1)  # calls randint function with arguments 0 and length of countries list minus one and assigns its returned value into index variable
            selected_countries.append(countries[index]["name"])  # appends value associated with "name" key in dictionary element at index position in countries list into selected_countries list
            selected_capitals.append(countries[index]["capital"])   ## appends value associated with "capital" key in dictionary element at index position in countries list into selected_capitals list.
        idx = randint(0, 2)   ### calls randint function with arguments '0' and '2' assigning its returned value to 'idx'.
        while True:   ### enters infinite loop.
            answer = self.INPUT(f"What is {selected_countries[idx]}'s capital ?: ", "MO", selected_capitals,self.NONE)   ### This line of code calls the INPUT method on the self object and passes four arguments to it. The first argument is a formatted string that displays a question to the user asking for the capital of a country. The country name is obtained from the selected_countries list at index idx. The second argument is a string "MO", which  represents an input mode . The third argument is the selected_capitals list, which could be used to validate user input or provide options for selection. The fourth argument is self.NONE, which represents a default value The returned value from calling the INPUT method is then assigned to the variable answer.
            try:   #### attempts to execute indented block of code.
                int(answer)   #### converts 'answer' to integer using int function.
            except ValueError:   ##### executes when above block raises ValueError exception.
                if answer == "Exit" or "exit":   ##### checks if answer is equal to string literal "Exit" or if string literal "exit" is truthy (always true).
                    break   ##### breaks out of infinite loop when above condition was true.
            if selected_capitals[int(answer)-1] == selected_capitals[idx]:    ###### checks if element at position obtained by converting answer to integer minus one from 'selected_capitals' is equal to element at idx position from same list.
                self.Print("Well Done that is correct!", 0.2)    ###### calls Print method passing string literal "Well Done that is correct!" as first argument and float literal '0.2' as second argument when above condition was true.
                break    ###### breaks out of infinite loop when above condition was true.

            else:    ####### executes when above condition was false.
                self.Print("Incorrect :( try again !!", 0.2)    ####### calls Print method passing string literal "Incorrect :( try again !!" as first argument and float literal '0.2' as second argument when above condition was false.

        replay = self.INPUT("Do you want to play again?: ", "MO", ["Yes", "No"],self.NONE)     ######## calls INPUT method passing string literal "Do you want to play again?: ", string literal "MO" and a new list containing two elements ["Yes"," No"] respectively as arguments then assigns its returned value into replay local variable.
        if replay == "1":     ######### checks if replay local variable value is equal to string literal '1'.
            self.Country_Guessing_game()     ######### recursively calls Country_Guessing_game method on itself when above condition was true.

class Player(UtilsGaurav):
    # Define a new class called Player that inherits from the UtilsGaurav class.

    def __init__(self):
        # Define the __init__ method for the Player class.
        super().__init__(ai=False, scratch=False)
        # Call the __init__ method of the parent class (UtilsGaurav) with AI and scratch set to False.

        self.Headshot_Multi = 1.75
        # Set the Headshot_Multi attribute to 1.75.
        self.Torso_Multi = 1.2
        # Set the Torso_Multi attribute to 1.2.
        self.Legs_Multi = 0.7
        # Set the Legs_Multi attribute to 0.7.

        self.strength = self.Roll(20)
        # Set the strength attribute by calling the Roll method with an argument of 20.
        self.Agility = self.Roll(20)
        # Set the Agility attribute by calling the Roll method with an argument of 20.
        self.intelligence = self.Roll(20)
        # Set the intelligence attribute by calling the Roll method with an argument of 20.
        self.wisdom = self.Roll(20)
        # Set the wisdom attribute by calling the Roll method with an argument of 20.
        self.charisma = self.Roll(20)
        # Set the charisma attribute by calling the Roll method with an argument of 20.

        self.HP = 100
        # Set the HP attribute to 100.

        self.Inventory = []
        # Initialize an empty list for the Inventory attribute.
        self.Item_Type = []
        # Initialize an empty list for the Item_Type attribute.
        self.Item_Damage = []
        # Initialize an empty list for the Item_Damage attribute.
        self.Item_Description = []
        # Initialize an empty list for the Item_Description attribute.
        self.Item_quantity = []
        # Initialize an empty list for the Item_quantity attribute.

        for item in items:
            # Iterate over each item in the items list.
            for i, data in enumerate(item):
                # Enumerate over each element (data) and its index (i) in the current item.

                if i == 0:
                    # If the index is 0:
                    self.Inventory.append(data)
                    # Append the data to the Inventory attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                elif i == 1:
                    # If the index is 1:
                    self.Item_Damage.append(data)
                    # Append the data to the Item_Damage attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                elif i == 2:
                    # If the index is 2:
                    self.Item_Type.append(data)
                    # Append the data to the Item_Type attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                elif i == 3:
                    # If the index is 3:
                    self.Item_Description.append(data)
                    # Append the data to the Item_Description attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                else:
                    # If none of the above conditions are met:
                    raise IOError("Unknown data")
                    # Raise an IOError with a message of "Unknown data".

    def attack(self, attacker_name, attacker_HP):
        Weapons = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "weapon":
                Weapons.append(item)
        option2 = int(self.INPUT("What Weapon do you want to use?", "MO", Weapons, self.NONE))
        idx = self.Inventory.index(Weapons[option2 - 1])
        Weapon_damage = self.Item_Damage[idx]
        Multipliers = [self.Headshot_Multi, self.Torso_Multi, self.Legs_Multi]
        Multi = Multipliers[randint(0, 2)]
        if float(Weapon_damage) * float(Multi) > attacker_HP:
            if Multi == self.Legs_Multi:
                self.Print(f"You use the {Weapons[option2]} and manage to  hit his legs ", 0.2)
                self.Print(f"The {attacker_name} collapsed to the ground, clutching his legs. ", 0.03)
                self.Print(f"The pain was unbearable, like a thousand knives stabbing him at once. ", 0.03)
                self.Print(f"He felt blood gushing from his wounds, soaking his clothes and the dirt beneath him. ",
                           0.03)
                self.Print(f"He tried to scream, but no sound came out. ", 0.03)
                self.Print(f"His vision blurred and he felt dizzy. ", 0.03)
                self.Print(f"He knew he was dying, but he couldn’t accept it. ", 0.03)
                self.Print(f"He had so much to live for, so much to do. ", 0.03)
                self.Print(f"He wanted to see his family again, to tell them he loved them. ", 0.03)
                self.Print(f"He wanted to fight for his cause, to make a difference in the world. ", 0.03)
                self.Print(
                    f"He wanted to live. But all he could do was lie there, helpless and hopeless, waiting for the end.",
                    0.03)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "legs"}
            elif Multi == self.Torso_Multi:
                self.Print(f"You use the {Weapons[option2]} and manage to  hit his body ", 0.2)
                self.Print(
                    "He felt a sudden impact in his chest, followed by a sharp pain that spread throughout his body. ",
                    0.03)
                self.Print("He gasped for air, but it felt like he was breathing fire. ", 0.03)
                self.Print("He looked down and saw blood pouring from his shirt. He realized he had been Hit.", 0.03)
                self.Print(
                    "he staggered backwards, trying to reach for his secret weapon. But his arms were numb and heavy. ",
                    0.03)
                self.Print(
                    "He fell to his knees, feeling weak and cold. He heard voices around him, shouting and shooting. ",
                    0.03)
                self.Print("But they sounded distant and muffled. He closed his eyes, hoping it was all a nightmare. ",
                           0.03)
                self.Print("But he knew it was real. He knew he was dying. And he was afraid.", 0.03)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "torso"}
            elif Multi == self.Headshot_Multi:
                self.Print(f"You use the {Weapons[option2]} and manage to  hit his head ", 0.2)
                self.Print("He heard a loud bang, and then everything went black. ", 0.03)
                self.Print("He felt a brief flash of pain in his head, like a hammer smashing his skull. ", 0.03)
                self.Print("He didn’t have time to react or think. He was dead before he hit the ground.", 0.03)
                self.Print(" His brain was shattered by the bullet that pierced his temple. ", 0.03)
                self.Print("His life was over in an instant. He had no memories, no regrets, no dreams.", 0.03)
                self.Print(" He had nothing. He was nothing.", 0.03)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "head"}
            else:
                raise IOError("UNKNOWN body HIT")
        else:
            self.Print(f"The {attacker_name} has taken {float(Weapon_damage) * float(Multi)} damage", 0.2)
            return {"status": "engaged", "HP": attacker_HP - (float(Weapon_damage) * float(Multi)),
                    "Total_Damage": (float(Weapon_damage) * float(Multi)), "Weapon_Damage": Weapon_damage,
                    "Multi": Multi, "loc": "body"}

    def Declare_truce(self, attacker_Emotional_attachment, attacker_name, attacker_HP):
        Probability_of_acceptance = (1 * (attacker_Emotional_attachment / 20))
        if Probability_of_acceptance == 1:
            print(f"The {attacker_name} Looks Down at you and admires your attachment to his kind")
            print(f"I guess i will find food some where else ")
            print(f"The {attacker_name} walks away util you cannot see him ")
            print(f"Your Intelligence{self.intelligence} increase by one ")
            self.intelligence += 1
            return {"status": "Declared Truce", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}
        else:
            print("Ha Ha Ha did you really think your sadness will affect me !!")
            print("DIEEE DIEEE!!")
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}

    def Run(self, attacker_strengh, attacker_name, attacker_HP):
        if attacker_strengh > self.strength:
            Metres = self.strength * self.Agility
            self.Print(
                f"you Run for your life as the {attacker_name} chases you sadly after {Metres} metres your energy depletes and the {attacker_name} is behind you ",
                0.01)
            self.Print(f"Ha HA HA where will you go now ?? says the {attacker_name}", 0.01)
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}
        else:
            self.Print(f"You manage to escape the {attacker_name}", 0.01)
            return {"status": "escaped", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}

    def consume(self):
        consumable = []
        options = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "consumable":
                consumable.append(item)
        for item in consumable:
            if self.Item_quantity[consumable.index(item)] >= 1:
                options.append(item)
        option2 = int(self.INPUT("What food do you want to consume?", "MO", options,self.NONE))
        self.Print(f"Did u know that the {consumable[option2-1]} is {self.Item_Description[self.Inventory.index(consumable[option2-1])]} ?", 0.02)
        self.Item_quantity[self.Inventory.index(consumable[option2-1])] -= 1
        self.HP += 10
        if self.Item_quantity[self.Inventory.index(consumable[option2-1])] <= 1:
            self.Print(f"you have {self.Item_quantity[self.Inventory.index(consumable[option2-1])]} {consumable[option2 - 1]} left .", 0.02)
        else:
            self.Print(f"you have {self.Item_quantity[self.Inventory.index(consumable[option2-1])]} {consumable[option2-1]}s left .", 0.02)

    def Wear(self):
        wearable = []
        options = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "armor":
                wearable.append(item)
        for item in wearable:
            if self.Item_quantity[wearable.index(item)] >= 1:
                options.append(item)
        option2 = int(self.INPUT("What items do you want to equip?", "MO", options,self.NONE))
        self.Print(f"Did u know that the {wearable[option2 - 1]} is {self.Item_Description[self.Inventory.index(wearable[option2 - 1])]} ?", 0.02)

    def options(self, attacker_name, attacker_HP, attacker_strengh, attacker_Emotional_attachment):
        option = self.INPUT("What do you want to do?", "MO", ["RUN", "FIGHT", "Declare Truce", "Consume", "wear"],self.NONE)
        if option == "1":
            return self.Run(attacker_strengh, attacker_name, attacker_HP)
        elif option == "2":
            return self.attack(attacker_name=attacker_name, attacker_HP=attacker_HP)
        elif option == "3":
            return self.Declare_truce(attacker_HP=attacker_HP, attacker_name=attacker_name, attacker_Emotional_attachment=attacker_Emotional_attachment)
        elif option == "4":
            self.consume()
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0, "loc": "NONE"}
        elif option == "5":
            self.Wear()
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0, "loc": "NONE"}

        else:
            raise IOError("Not an Option")


class Enemy(UtilsGaurav):

    def __init__(self, _name, HP, EM, Strength):
        super().__init__(ai=False, scratch=False)
        self.HP = HP
        self.Headshot_Multi = 1.7
        self.Torso_Multi = 1.2
        self.Legs_Multi = 0.7
        self.name = _name
        self.Emotional_Attachment = EM
        self.Strength = Strength
        self.Inventory = []
        # Initialize an empty list for the Inventory attribute.
        self.Item_Type = []
        # Initialize an empty list for the Item_Type attribute.
        self.Item_Damage = []
        # Initialize an empty list for the Item_Damage attribute.
        self.Item_quantity = []
        # Initialize an empty list for the Item_quantity attribute.

        for item in items:
            # Iterate over each item in the items list.
            for i, data in enumerate(item):
                # Enumerate over each element (data) and its index (i) in the current item.

                if i == 0:
                    # If the index is 0:
                    self.Inventory.append(data)
                    # Append the data to the Inventory attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                elif i == 1:
                    # If the index is 1:
                    self.Item_Damage.append(data)
                    # Append the data to the Item_Damage attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                elif i == 2:
                    # If the index is 2:
                    self.Item_Type.append(data)
                    # Append the data to the Item_Type attribute.
                    self.Item_quantity.append(2)
                    # Append 2 to the Item_quantity attribute.

                else:
                    # If none of the above conditions are met:
                    raise IOError("Unknown data")
                    # Raise an IOError with a message of "Unknown data".


def process(self, player_HP):
        option2 = randint(1, len(self.Inventory) - 1)
        idx = self.Inventory.index(self.Inventory[option2])
        Weapon_damage = self.Item_Damage[idx]
        Multipliers = [self.Headshot_Multi, self.Torso_Multi, self.Legs_Multi]
        Multi = Multipliers[randint(0, 2)]
        if float(Weapon_damage) * float(Multi) > player_HP:
            if Multi == self.Legs_Multi:
                self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your legs ", 0.2)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "legs"}

            elif Multi == self.Torso_Multi:
                self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your body ", 0.2)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "torso"}

            elif Multi == self.Headshot_Multi:
                self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your head ", 0.2)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "head"}

            else:
                raise IOError("UNKNOWN body HIT")
        else:
            self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your body ", 0.2)
            self.Print(f"YOU have taken {float(Weapon_damage) * float(Multi)} damage", 0.2)
            return {"status": "engaged", "HP": player_HP - (float(Weapon_damage) * float(Multi)),
                    "Total_Damage": (float(Weapon_damage) * float(Multi)), "Weapon_Damage": Weapon_damage,
                    "Multi": Multi, "loc": "body"}
