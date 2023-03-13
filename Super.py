##############################################
#              Ultis_Gaurav                  #
#          ALL code by Gaurav.Shukla         #
#               v:0.1(01/03/2023)            #
#              CC0 license applies           #
##############################################
import time  # gives access to the time module
import speech_recognition as sr  # gives access to the Speech recognition module
import pyttsx3  # gives access to the Pyttsx3 module
from chatterbot import ChatBot  # gives access to the Chatterbot module
from chatterbot.trainers import ChatterBotCorpusTrainer  # gives access to the chatterbot trainer dataset
from random import *
from countries_info import countries
from items import items






class UtilsGaurav:  # creates class Utils_Gaurav
    def __init__(self, ai, scratch):  # tells the program what to do when the Utils_Gaurav class has been initialised
        if ai == True:
            self.Ai_Enabled = True
            self.r = sr.Recognizer()  # initialises the Recogniser Function (no arguments) in the sr(Speech Recognition) Class
            self.Gaurav = ChatBot(
                "Gaurav")  # initialises the ChatBot Class with 1 parameter/argument name which is set to the string Gaurav and  this is set to the variable assigned Gaurav
            self.trainer = ChatterBotCorpusTrainer(
                self.Gaurav)  # initialises the ChatterBotCorpustrainer Class with 1 parameter/argument -the Chatbot class- this is set to the variable assigned Trainer
            self.trainer.train(
                "chatterbot.corpus.english")  # trainer(a variable) which has an attribute of train which is a function in the ChatterBotCorpusTrainer Class with 1 argument type string
        else:
            self.Ai_Enabled = False
        if scratch == True:
            self.Scratch_Enabled = True
            import scratchconnect  # gives access to the Scratch Connect module
            self.user = scratchconnect.ScratchConnect("__BIT__",
                                                      "Lakshya123@")  # logs into a Scratch User to Give us access to all Scratch Features
            self.project = self.user.connect_project(project_id=778517371)  # Accesses the Project using project id
            self.Variables = self.project.connect_cloud_variables()  # Connect the project's cloud variables
            self.Event = self.Variables.create_cloud_event()  # Create a cloud  event
            self.communications_line = "Cloud"  # Sets the Communications line with the Project To the string Cloud we need an identical Cloud Variable in Scratch to interact and share data
        else:
            self.Scratch_Enabled = False
        print("---GAURAV'S UTILS FUNCTION---")  # prints a string

    def Roll(self, d):
        import random
        return random.randint(1, int(d))

    def SpeakText(self,
                  command):  # a function/Subroutine named SpeakText with 1 argument command the def keyword is used to define the function
        if self.Ai_Enabled == True:
            engine = pyttsx3.init()  # initialises the init()subroutine and sets it to the variable assigned as engine
            engine.say(
                command)  # engine(a variable) which has an attribute of say which is a function in the pyttsx3 module with 1 argument type string command
            engine.runAndWait()  # engine(a variable) which has an attribute of runAndWait which is a function in the pyttsx3 module with 1 argument self
        else:
            raise IOError("Function_Disabled")

    def find(self, word,
             var):  # a function/Subroutine named find  def keyword is used to define the function with 2 parameters word and var standing for keyword and data set
        WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
        ret = 0  # initialises a variable assigned ret indicates that it is going to be an integer
        new_word = ""  # initialises a variable assigned new_word indicates that it is going to be a string
        speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
        for i in range(len(var)):  # a for loop that is going to repeat length of var
            item = var[i]  # sets variable assigned item to the  i character of var
            WORD = WORD + item  # sets variable assigned WORD to itself + variable item
            if item == "'":  # an if statement that activates the tabbed code under if the statement is true
                if speech_marks == 1:  # an if statement that activates the tabbed code under if the statement is true
                    if WORD == "'" + word + "'":  # an if statement that activates the tabbed code under if the statement is true
                        speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
                        WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
                        ret = 1  # sets variable assigned ret to  1
                    elif ret == 1:  # else if statement
                        for i2 in range(len(WORD)):  # a for loop that is going to repeat length of WORD
                            letter = WORD[i2]  # sets variable assigned letter to the  i character of WORD
                            if letter != "'":  # an if statement that activates the tabbed code under if the statement is true
                                new_word = new_word + letter  # sets variable assigned new_word to itself + variable letter
                        return new_word  # returns the variable assigned new_word
                    else:  # else statement that only gets activated if the other statements are false
                        speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
                        WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
                else:  # else statement that only gets activated if the other statements are false
                    speech_marks = 1  # sets the variable assigned speech_marks to integer value 1

    def receive(self):  # a function/Subroutine named SpeakText  def keyword is used to define the function
        if self.Ai_Enabled == True:
            try:  # Tries the following code check for errors that might be raised
                with sr.Microphone() as source2:  # calls the Microphone() function /attribute as keyword used to give a temporary name for example source2
                    self.r.adjust_for_ambient_noise(source2,
                                                    duration=0.2)  # calls the adjust_for_ambient_noise function with 2 arguments microphone source ,duration
                    audio2 = self.r.listen(
                        source2)  # calls the listen function with 1 argument microphone also known as source2 and is set to the variable assigned audio2
                    MyText = self.r.recognize_google(
                        audio2)  # calls the recognize_google function with one argument which is the sound input this function coverts the sound input into text using the Google Ai model and sets the variable assigned Mytext
                    MyText = MyText.lower()  # first the Mytext has an  attribute lower which makes it lower case, and then it is set to the variable assigned Mytext
                    return MyText  # returns the Mytext Variable

            except sr.RequestError:  # the except keyword tells the computer how to handle a RequestError only used with the try function
                return "NO INPUT"  # Returns a string called NO INPUT

            except sr.UnknownValueError:  # the except keyword tells the computer how to handle a UnknownValueError only used with the try function
                return "NO INPUT"  # Returns a string called NO INPUT
        else:
            raise IOError("Function_Disabled")

    def INPUT(self, prompt, types, data):  # Input function with  4 parameters prompt,type and data + self
        if types == "Basic":  # an if statement that activates the tabbed code under if the statement is true
            return input(str(prompt))  # returns the answer to the question
        elif types == "MO":  # Multiple Options (else if statement)
                print(str(prompt))  # prints the answer to the question
                for i in range(len(list(data))):  # a for loop that is going to repeat length of data
                    print(f"OPTION {i + 1}: {data[i]}")  # prints the Options of the question so user can answer
                out = input("PICK OPTION: ")  # returns the answer to the question
                if out != "":
                    if out > str(len(data)):
                        print("NOT an option")
                        return self.INPUT(prompt=prompt, types=types, data=data)
                    else:
                        return out
                else:
                    print("cannot except keys given ")
                    return self.INPUT(prompt=prompt, types=types, data=data)

    def Print(self, txt, delay):  # Print function with 3 parameters txt,delay and self
        for char in txt:  # a for loop that is going to repeat length of txt
            print(char, end='', flush=True)  # prints each character on same line
            time.sleep(delay)  # uses the time function to delay in seconds
        print("", end="\n", flush=False)

    def ChatBot(self, txt):  # Chatbot function with 2 parameters txt and self
        if self.Ai_Enabled == True:
            return self.Gaurav.get_response(
                txt)  # returns response to the txt input using the get response attribute of Gaurav
        else:
            raise IOError("Function_Disabled")

    def Stream_chatbot_out_to_Scratch(self):  # A function that allows for chatbots in scratch
        if self.Ai_Enabled == True and self.Scratch_Enabled == True:
            @self.Event.on("connect")  # triggers the code under if true
            def connect():  # function called connect
                print("Connection established starting data sharing")  # prints to terminal a string
                encoded_string = self.Variables.encode("Server Listening...")  # Encode a string
                self.Variables.set_cloud_variable(variable_name=self.communications_line,
                                                  value=encoded_string)  # Sends Encoded String

            @self.Event.on("set")  # triggers the code under if true
            def set(data):  # function called set with 1 argument data
                if str(data[
                           "user"]) != "__BIT__":  # an if statement that activates the tabbed code under if the statement is true
                    encoded = data["value"]  # sets variable assigned encoded to value in the data dictionary
                    message = self.Variables.decode(
                        encoded)  # sets variable assigned message to the decoded data sent from Scratch
                    function = self.find("function",
                                         message)  # sets variable assigned function to the return value form the find function with string "function" and message given as parameter
                    if function == "stream":  # an if statement that activates the tabbed code under if the statement is true
                        new_data = self.find("DATA",
                                             message)  # sets variable assigned new_data to the return value form the find string "DATA" and message given as parameter
                        encoded_string = self.Variables.encode(self.Gaurav.get_response(new_data))  # Encode a string
                        self.Variables.set_cloud_variable(variable_name=self.communications_line,
                                                          value=encoded_string)  # sets cloud Variable to encoded_String
                    else:  # else statement that only gets activated if the other statements are false
                        print("NOT STREAM")  # prints string Not Streaming
                        encoded_string = self.Variables.encode("NOT Correct format")  # Encode a string
                        self.Variables.set_cloud_variable(variable_name=self.communications_line,
                                                          value=encoded_string)  # sets cloud Variable to encoded_String

                self.Event.start(update_time=0.01)  # starts the cloud event
        else:
            raise IOError("Function_Disabled Hint:Maybe Forgot to Set Ai to True")

    def Gaurav(self):  # function named Gaurav with 1 parameter self
        if self.Ai_Enabled == True:
            while True:  # while statement set default to true meaning it will run infinite times
                txt = str(
                    self.receive())  # sets the variable assigned txt to the string from return value from the receive() function
                if txt != "bye":  # an if statement that activates the tabbed code under if the statement is true
                    self.SpeakText(
                        self.Gaurav.get_response(txt))  # speaks the response from Gaurav the Chatbot given some text
                elif txt == "what is your name":  # else if statement
                    self.SpeakText("Gaurav")  # speaks name Gaurav
                else:  # else statement that only gets activated if the other statements are false
                    self.SpeakText("Bye")  # speaks text bye
                    break  # breaks the infinite loop
        else:
            raise IOError("Function_Disabled")

    def Money_to_Coins(self, *money):
        total_amount = 0
        for i in money:
            total_amount = total_amount + int(i)
        T1 = total_amount // 20
        total_amount = total_amount - (20 * T1)
        T2 = total_amount // 10
        total_amount = total_amount - (10 * T2)
        T3 = total_amount // 5
        total_amount = total_amount - (5 * T3)
        T4 = total_amount // 2
        total_amount = total_amount - (2 * T4)
        return {"20": T1,
                "10": T2,
                "5": T3,
                "2": T4,
                "1": total_amount}

    def Country_Guessing_game(self):
        selected_countries = []
        selected_capitals = []
        for i in range(3):
            index = randint(0, len(countries) - 1)
            selected_countries.append(countries[index]["name"])
            selected_capitals.append(countries[index]["capital"])
        idx = randint(0, 2)
        while True:
            answer = self.INPUT(f"What is {selected_countries[idx]}'s capital ?: ", "MO", selected_capitals)
            try:
                int(answer)
            except ValueError:
                if answer == "Exit" or "exit":
                    break
            if selected_capitals[int(answer) - 1] == selected_capitals[idx]:
                self.Print("Well Done that is correct!", 0.2)
                break

            else:
                self.Print("Incorrect :( try again !!", 0.2)

        replay = self.INPUT("Do you want to play again?: ", "MO", ["Yes", "No"])
        if replay == "1":
            self.Country_Guessing_game()

    def Text_based_Games(self):
        pass


class Player(UtilsGaurav):

    def __init__(self):
        super().__init__(ai=False, scratch=False)
        self.Headshot_Multi = 1.75
        self.Torso_Multi = 1.2
        self.Legs_Multi = 0.7
        self.strength = self.Roll(20)
        self.Agility = self.Roll(20)
        self.intelligence = self.Roll(20)
        self.wisdom = self.Roll(20)
        self.charisma = self.Roll(20)
        self.HP = 100
        self.Inventory = []
        self.Item_Type = []
        self.Item_Damage = []
        self.Item_Description = []
        self.Item_quantity = []
        for item in items:
            for i, data in enumerate(item):
                if i == 0:
                    self.Inventory.append(data)
                    self.Item_quantity.append(2)
                elif i == 1:
                    self.Item_Damage.append(data)
                    self.Item_quantity.append(2)
                elif i == 2:
                    self.Item_Type.append(data)
                    self.Item_quantity.append(2)
                elif i == 3:
                    self.Item_Description.append(data)
                    self.Item_quantity.append(2)
                else:
                    raise IOError("Unknown data")

    def attack(self, attacker_name, attacker_HP):
        Weapons = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "weapon":
                Weapons.append(item)
        option2 = int(self.INPUT("What Weapon do you want to use?", "MO", Weapons))
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
        option2 = int(self.INPUT("What food do you want to consume?", "MO", options))
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
        option2 = int(self.INPUT("What items do you want to equip?", "MO", options))
        self.Print(f"Did u know that the {wearable[option2 - 1]} is {self.Item_Description[self.Inventory.index(wearable[option2 - 1])]} ?", 0.02)

    def options(self, attacker_name, attacker_HP, attacker_strengh, attacker_Emotional_attachment):
        option = self.INPUT("What do you want to do?", "MO", ["RUN", "FIGHT", "Declare Truce", "Consume", "wear"])
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
        self.Inventory = ["dagger", "sword", "wand"]
        self.Item_Damage = ["10", "35", "60", "0"]

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
            self.Print(f"YOU have taken {float(Weapon_damage) * float(Multi)} damage", 0.2)
            return {"status": "engaged", "HP": player_HP - (float(Weapon_damage) * float(Multi)),
                    "Total_Damage": (float(Weapon_damage) * float(Multi)), "Weapon_Damage": Weapon_damage,
                    "Multi": Multi, "loc": "body"}
