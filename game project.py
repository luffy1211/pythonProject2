print("Welcome to my guessing game!")

playing = input("would you like to play? ")
if playing != "yes":
    quit()
print("okay lets play")
score = 0
answer = input("what does cpu stand for? ")
if answer == "central procesing unit":
    print("You are correct! ")
    score += 1
else:
    print("try again! ")

answer = input("what does gpu stands for? ")
if answer == "graphic procesing unit":
    print("You are correct! ")
    score += 1

else:
    print("try again! ")

answer = input("what does RAM stand for? ")
if answer == "random access memory":
    print("You are correct! ")
    score += 1

else:
    print("try again! ")

answer = input("what does psu stand for? ")
if answer == "power supply unit":
    print("You are correct! ")
    score += 1

else:
    print("try again! ")


print("you got" + str(score)+ "questions correct")
print("you got " + str((score/4)*100) +  "%")

