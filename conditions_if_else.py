#syntax
#if condition
#   #code #if Conditions is true then code is execute 
#           #code

age = input("enter your age: ")
age = int(age)
if age >=14:
    print("your are above 14 ")
    print("welcome to the game")
else:
    print("you can't play the game")

#nexted_if_else
h = input("enter the number :  ")
h = int(h)
if h > 50:
    print("Greater then 50")
else:
    if h < 30:
        print("less then 30")
    else:
        print("between 30 or 50")

#by_using_elif_keyword


if h > 50:
    print("Greater then 50")
elif h < 30:
        print("less then 30")
else:
        print("between 30 or 50")
