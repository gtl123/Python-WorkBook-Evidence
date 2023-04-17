#############################################################################################################
#                                              Ultis_Gaurav                                                 #
#                                         ALL code by Gaurav.Shukla                                         #
#                                            v:CS1.0(17/03/2023)                                            #
#                                            CC0 license applies                                            #
#           THIS CODE HAS BEEN SHORTENED TO RUN ON MACHINES WHICH DON'T HAVE THE NECESSARY MODULES          #
#############################################################################################################

# Version == custom 1.0 {the newest version can be found @ https://github.com/gtl123/Python-WorkBook-Evidence}
# Code Comments by ChatGTP-4.0

import time  # imports the time module
from random import *  # imports all functions from the random module
from country_info import countries  # imports countries from country_info module


class UtilsGaurav:  # defines a new class called UtilsGaurav
    def __init__(self):  # defines an __init__ method
        print("---GAURAV'S UTILS FUNCTION---")   ## prints string "---GAURAV'S UTILS FUNCTION---".

    def Roll(self, d):   ## defines Roll method that takes in one argument d.
        import random    ## gives access to random module by importing it locally within this block of code only.
        return random.randint(1, int(d))    ## returns a random integer between 1 and d (inclusive) using randint function from random module.

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