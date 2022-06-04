import random

options = ["R", "P", "S"]
optionsFull = {"R":"ROCK", "P":"PAPER", "S":"SCISSOR"}
# global game
# global mySelectionNumber
# global aiSelectionNumber
# game = 0
# mySelectionNumber = 0
# aiSelectionNumber = 0

print("Welcome to Rock Paper Scissor Game \n")
print("You will be playing against an formidable AI \n BEST OF LUCK")
print("SELECT BETWEEN R,P,S")
print("WHERE R STANCE FOR ROCK")
print("WHERE P STANCE FOR PAPER")
print("WHERE S STANCE FOR SCISSOR")

def main():

    game = 0
    mySelectionNumber = 0
    aiSelectionNumber = 0
    mySelection = str(input("Enter your selection :")).upper()

    if ((mySelection == "R") or (mySelection == "P") or (mySelection == "S") ):
       
        aiSelection = random.choice(options)

        print("Your Selection is", optionsFull[mySelection])
        print("AI Selection is", optionsFull[aiSelection])
        print("present score = Player(",optionsFull[mySelection],") : CPU (",optionsFull[aiSelection],")")

        if (mySelection == aiSelection):
            print("Ouch! \n lets go another round...")
            game = game + 1
            if (game == 3):
                print("It a tie! \n lets go another round...")
                exit()
        
        if (((optionsFull[mySelection]) == "Rock") and ((optionsFull[aiSelection]) == "Scissor")):
           playerpoint()
        if (((optionsFull[mySelection]) == "Paper") and ((optionsFull[aiSelection]) == "Rock")):
           playerpoint()
        if (((optionsFull[mySelection]) == "Scissor") and ((optionsFull[aiSelection]) == "Paper")):
           playerpoint()

        if (((optionsFull[aiSelection]) == "Rock") and ((optionsFull[mySelection]) == "Scissor")):
           aipoint()
        if (((optionsFull[aiSelection]) == "Paper") and ((optionsFull[mySelection]) == "Rock")):
           aipoint()
        if (((optionsFull[aiSelection]) == "Scissor") and ((optionsFull[mySelection]) == "Paper")):
           aipoint()
        

        print("Finally you made a selection !!!")
        exit()
        

    print("Error, Please Select Between P, R, S !!!")
    main()
    # print(mySelection)
    # print(aiSelection)

def playerpoint():
    mySelectionNumber += 1
    if (mySelectionNumber == 3):
        print("You Are the Winner")
        exit()
    print("One Point Added to you, Lets Play another round")
    main()
 
def aipoint():
    aiSelectionNumber += 1
    if (aiSelectionNumber == 3):
        print("AI is the Winner")
        exit()
    print("One Point Added to you, Lets Play another round")
    main()

main()