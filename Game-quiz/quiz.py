print("Hello")
print("Welcome to my Quiz project")


playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()
print ("Okay, Let's play")

score = 0
answer = input("What does CPU stand for?")

if answer.lower() =="central processing unit":
        print("Correct")
        score += 1
else:
      print("Incorrect")

answer = input("What is the capital city of Kenya?")

if answer.lower() == "nairobi":
        print("Correct")
        score +=1
else:
      print("Incorrect")

answer = input("How many airports are there in Nairobi?")

if answer == "three":
        print("Correct")
        score +=1

else:
      print("Incorrect")


print ("You got " + str(score) + " questions correct")

print ("You got " + str((score / 3) *100) +"%")

