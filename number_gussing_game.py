# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number . 
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then :
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"
 


win_number = 5
user_number = int(input("Enter the number : "))

if win_number == user_number:
    print("you win")
elif user_number < win_number:
        print("too low")
else:
        print("too higher")
