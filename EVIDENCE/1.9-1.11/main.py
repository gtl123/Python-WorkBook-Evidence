##############################################
#                    Main                    #
#          ALL code by Gaurav.Shukla         #
#               v:0.1(01/03/2023)            #
#              CC0 license applies           #
##############################################
from Class import *

utils = UtilsGaurav()

Questions = ["Surname? "
    , "Forename? "
    , "Enter address line?: "
    , "Enter area?: "
    , "Enter town?: "
    , "Enter county?: "
    , "Enter postcode?: "
    , "Favourite Colour ?: "
    , "Age?: "
    , "height in metres?: "
    , "Gender?: "
    , "year group?: "]
Answers = []

for i in range(len(Questions)):
    Answers.append(utils.INPUT(Questions[i], "Basic", "", utils.NONE))  # asks user for input turns into string and stores in List called Answers

utils.Print(f'Hello {Answers[Questions.index("Surname? ")].capitalize()}, {Answers[Questions.index("Forename? ")].capitalize()}', 0.06)  # prints to the terminal
utils.Print("How are you?", 0.3)  # prints to the terminal
utils.Print("______________________________", 0)  # prints to the terminal
utils.Print(Answers[Questions.index("Enter address line?: ")], 0.06)  # prints to the terminal
utils.Print(Answers[Questions.index("Enter area?: ")], 0.06)  # prints to the terminal
utils.Print(Answers[Questions.index("Enter town?: ")], 0.06)  # prints to the terminal
utils.Print(Answers[Questions.index("Enter county?: ")], 0.06)  # prints to the terminal
utils.Print(Answers[Questions.index("Enter postcode?: ")], 0.06)  # prints to the terminal
utils.Print(f"Hello, {Answers[Questions.index('Forename? ')]} ", 0.3)  # prints to the terminal
utils.Print(f"You are {Answers[Questions.index('Age?: ')]} years old, your favourite colour is {Answers[Questions.index('Favourite Colour ?: ')]}", 0.06)  # prints to the terminal
utils.Print(f"You are {Answers[Questions.index('height in metres?: ')]} metres tall and you are a {Answers[Questions.index('Gender?: ')]}", 0.06)  # prints to the terminal
utils.Print(f"You are in year {Answers[Questions.index('year group?: ')]}", 0.06)  # prints to the terminal

