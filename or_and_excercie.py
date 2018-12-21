# EXERCISE - WATCH COCO
# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print 'you can watch coco movie'
# Else print 'sorry, you cannot watch coco'


name = input("enter your name : ")
age = int(input("Enter the age : "))

if age >= 10 and (name[0] == 'a' or name[0] == 'A'):
    print("you can watch coco movie")
else:
    print("sorry, you cannot watch coco")
