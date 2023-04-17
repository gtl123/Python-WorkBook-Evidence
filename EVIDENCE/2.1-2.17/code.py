from Class_short import *

obj = UtilsGaurav()


# 2.1
def comparelist(L):
    if len(L) == 2:
        if L[0] == L[1]:
            print("Values are equal")
        elif L[0] < L[1]:
            print(f"{L[1]} is greater than {L[0]}")
            print(f"{L[1]} is the biggest")
        else:
            print(f"{L[1]} is less than {L[0]}")
            print(f"{L[0]} is the biggest")
    return 0


obj.INPUT('Enter a Number!', types='ME', data=[2, 'int'], func=comparelist)
# 2.2
while True:
    marks = obj.INPUT('Enter the result !', types='ME', data=[1, 'int'], func=obj.NONE)
    if int(marks[0]) >= 50:
        print("You have passed")
        break
    else:
        print("you have failed try again")
# 2.3
counter = 1
while True:
    state = obj.INPUT('TO Continue press key (Y) to exit press key (N) ', types='ME', data=[1, 'str'], func=obj.NONE)
    if state[0].upper() == "N":
        print("Exiting")
        break
    else:
        print("Continuing", end="", flush=True)
        for dot in range(counter):
            print(".", end="", flush=True)
        print("", end="\n", flush=False)
        counter += 1


# 2.4 done>basically 2.1<:)
# 2.5 done>already had features requested <:)
# 2.6
def find_largest_integer(lst):
    max_value = None
    for value in lst:
        if isinstance(value, int):
            if max_value is None or value > max_value:
                max_value = value
    return max_value


print(f"{find_largest_integer(obj.INPUT('Enter a number', types='ME', data=[3, 'int'], func=obj.NONE))} is the largest ")
# 2.7
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to drive.")
else:
    print("Sorry, you are not eligible to drive.")