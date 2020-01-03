import random
import time



def displayIntro():
    print("Our story takes place in a grim mansion on a rainy day...\n")
    #time.sleep(3)
    print("You are an twelve-year old girl, whose parents have sent you out of the city to live with your unlce and aunt on their remote estate for the summer.\n")
    #time.sleep(3)
    print("Today your aunt and uncle are heading out into town to a dinner party, leaving you alone in the mansion.\n")
    #time.sleep(3)
    print("You hear on the radio that a violent psychopath has escaped from the insane asylum two miles away.\n")
    #time.sleep(3)
    print("All of a sudden...\n")
    #time.sleep(3)
    print("Someone knocks on your door...\n")
    #time.sleep(3)
    print("Then nothing...\n")
    print("You decide to not answer and hide somewhere safe in the mansion.\n")
    #time.sleep(3)
    print("You must choose between going upstairs or downstairs.\n")
    #time.sleep(3)
    
    
    
    
# starting path 
def choosePath1():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")
    return path

def checkPath1(chosenPath):
    print("You have chosen...\n")
    #time.sleep(2)
    if chosenPath == "1":
        print("to go upstairs.\n")
        return checkPath2a(choosePath2a())
    elif chosenPath =="2":
        print("to go downstairs. \n")

# choose upstairs 
def choosePath2a():
    print("You walk up the stairs.\n")
    #time.sleep(2)
    print("You hear a loud crash below.\n")
    #time.sleep(2)
    print("Foot steps are following...\n")
    #time.sleep(2)
    print("There are two doors: one leads to your bedroom, the other to a dead end.\n")
    print("But you don't know which one.\n")
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")
    return path

def checkPath2a(chosenPath):
    print("You have chosen...\n")
    #time.sleep(2)
    correctPath = random.randint(1,2)
    
    if chosenPath == correctPath:
        print("You are in the bedroom.\n")
    else:
        print("You have reached the end of a path. \n")    

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice1 = choosePath1()
    checkPath1(choice1)
    #choice2 = choosePath2a()
    #checkPath2a(choice2)
    playAgain = input("Do you want to play again? (yes or y)")
