print("Welcome to my Computer Quiz.!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":  
    quit()
print("Okay let's begin the play :)")

score = 0 #for the score calculation, first the score is 0 then it will be incremented after the correct answer


answer = input("What does CPU stand for? ")
 #anywhere .lower can make the alphabet lowercase for the variable answer that should be
if answer.lower()  == "central processing unit":
    print('Correct!')
    score +=1   #Score will be incremented by 1 if correct answer 
else:
    print("Your answer is  incorrect!")


    answer = input("What does GPU stand for? ")
if answer.lower()  == "graphics processing unit": 
     #anywhere .lower can make the alphabet lowercase for the variable answer that should be
    print('Correct!')
    score +=1 
else:
    print("Your answer is  incorrect!")


    answer = input("What does RAM stand for? ")
if answer.lower()  == "random access memory":
    print('Correct!')
    score +=1 
else:
    print("Your answer is  incorrect!")


    answer = input("What does ROM stand for? ")
if answer.lower  == "read only memory":
    print('Correct!')
    score +=1 
else:
    print("Your answer is  incorrect!")

print("You got "  + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")