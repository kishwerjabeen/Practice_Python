name = "Kishwar"
age = 24
broAge = 18
number = 3

print("hello " + name + " your age is " + str(age)) #bad practice

#basic formating 
print("hello {} your age is {} ".format(name, age + 2)) # this is use in python 3

print(f"hellow {name} your ager is {age + 2}") #best Pratice python 3.6 

#working with position 
print("my age is {1} and my bro age is {0} , {2}". format(broAge, age, number))

#type conversion into float 
print("number is {}".format(number)) #show int number 
print("number is {0:f}".format(number)) #:f means show in float 
print("number is {0:.3f}".format(number)) #if we want only 3 digit after . 

#type conversion (double to float)

print("number divide by 3 is {0}".format(number)) #double format 
print("number divide by 3 is {0:f}".format(number))  #flot format

#spacing using 'd'
print("my age is {0:3d}". format(age)) #just 1 space
print("my age is {0:4d}". format(age)) # 2 spaces 

#spacing by using left (<) and right (>) // using in all string int etc
print("my name is{0:>8} ".format("Kishwar"))
print("my name is{0:>10} ".format("Kishwar"))

print("my name is {0:<8} ....".format("Kishwar")) #right shveror or padding

#caret symbol(^) for center of the text
print("{0:*^8s}".format("Kishwar"))
print("{0:*^9s}".format("Kishwar"))
print("{0:*^11s}".format("Kishwar"))

print("{0:*^}".format(name))

#example of formatting inside loop 
for i in range(10): 
    print(" {0} {1} {2}".format(i, i**2, i**3))

for i in range(1,10):  
     print("{} {} {}".format(i, i**2 , i**3))

