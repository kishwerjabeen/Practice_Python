# user input
# input function
name = input("Type your name ")
print("hello " + name)
# string 
age = input("what is your age ? ")
#24 , "24"
print("your age is " + age)
number_one = input("enter first number : ")
number_two = input("enter second number : ")
totals = number_one + number_two
print("total is " + totals) 

#if int input 
number_one = int(input("enter first number : "))
number_two = int(input("enter second number : "))
totals = number_one + number_two
print("total is " + str(totals)) 

#you can add int or float 
number2 = float("44")
number3 = int("33")
print("after adding int or float" +  str(number2+number3))

#how to take more then one variable initialize

name, age = "Kishwer", "24"
print("hello " + name + " your age is " + age)
x=y=z=1
print(x+y+z)

#two or more input in one line by using "split()"

# name = input("enter your name : ")
# age = input("enter you age : ")

name, age = input("enter your name & age  ").split()
print(name)
print(age)
