import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number greater than zero next time.')
else:
    print('Please type a number next time.')
    quit()
random_number = random.randint(0,top_of_range)

#print(random_number)


""" #this gives the multiline comments
r = random.randrange(11) #random.randrange(11) is 0 to 10 for other number to define the range 
#(5,11) 11 is not shown; it only shows from 5 to 10. 
print(r)
"""

#to calculate in how many times the guess is correct 
guesses = 0
while True:
    guesses +=1 #it will be incremented if the guesses will be run. 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
         user_guess = int(user_guess)

    else:
        print('Please type a number next time.')
        continue
    if user_guess ==random_number:
        print("You got it!")
        break   #It will stop the guess after the correct guessing 
    #else:
       # print("You got it wrong!")
    elif user_guess > random_number:
            print("You were above the number !")
    else:
            print("You are below the number ")



print("You got it in", guesses, "guesses.")
   
