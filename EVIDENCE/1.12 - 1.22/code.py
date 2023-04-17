from Class2_9 import *

obj = UtilsGaurav()
obj.Print(txt=f"The answer is {obj.INPUT('Enter a number', types='ME', data=[2, 'int'], func=obj.multiply_list)}",
          delay=0.2)

obj.Print(obj.INPUT('Enter a number', types='ME', data=[3, 'str'], func=obj.add_list), delay=0.2)
obj.Print(f'''The area of the swimming pool is {obj.INPUT("", types="Custom",
                                                          data={"type": "str"
                                                              , "1": "Please enter length of the swimming pool in metres: "
                                                              , "2": "Please enter width of the swimming pool in metres: "
                                                              , "3": "Please enter depth of the swimming pool in metres: "},
                                                          func=obj.multiply_list)} metres cubed''', 0.02)


def Get_tri_area(X):
    if len(X) == 2:
        return float((1 / 2) * int(X[0]) * int(X[1]))
    else:
        return 0


def distance_unit_converter(object, unit, X):
    if unit == "km":
        return object.Print(str(float(X) * 0.62137), 0.2)
    elif unit == "Mile":
        return object.Print(str(float(X) * 1.62137), 0.2)
    else:
        return X


def weight_unit_converter(object, unit, X):
    if unit == "pounds":
        return object.Print(str(float(X) * 0.45), 0.2)
    elif unit == "Kg":
        return object.Print(str(float(X) * 1.45), 0.2)
    else:
        return X


def sq_perimeter(x):
    if len(x) == 2:
        return (2 * int(x[0])) + (2 * int(x[1]))
    else:
        return 0

def _is_even(num):
    if num % 2 != 0:
        print("Is Odd")
    else:
        print("Is Even")
def remander_integer(num1, num2):
    print(f"number1 / number2 is {int(num1) // int(num2)} remainder {int(num1) % int(num2)}")

obj.Print(f'''The area of the triangle is {obj.INPUT('', types='Custom',
                                                     data={'type': 'int'
                                                         , '1': 'Please enter base of the triangle: '
                                                         , '2': 'Please enter height of the of the triangle: '
                                                           },
                                                     func=Get_tri_area)} units''', 0.02)

distance_unit_converter(obj, "km", input("KM TO MILES: "))

weight_unit_converter(obj, "pounds", input("Pounds to kilograms: "))

print(f"BIDMAS/BODMAS: (60-3)*(6+5) = {(60 - 3) * (6 + 5)} while 60-3*6+5 = {60 - 3 * 6 + 5}")

obj.Print(f'''The perimeter of the square  is {obj.INPUT('', types='Custom',
                                                         data={'type': 'int'
                                                             , '1': 'Please enter length of the square: '
                                                             , '2': 'Please enter width of the of the square: '
                                                               },
                                                         func=sq_perimeter)} units''', 0.02)

_is_even(int(input("Enter a number: ")))
remander_integer(num1=input("number1 is: "), num2=input("number2 is: "))

ans = obj.Money_to_Coins(obj.INPUT("Money: ", "Basic", "", obj.NONE))
obj.Print(
    f"You need {ans['20']} £20 notes {ans['10']} £10 notes {ans['5']} £5 notes {ans['2']} £2 coins and {ans['1']} £1 coins ", 0.06)
