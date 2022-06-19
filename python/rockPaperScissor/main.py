import random

options = ["R", "P", "S"]
optionsFull = {"R":"ROCK", "P":"PAPER", "S":"SCISSOR"}
scoreBoard = {"Player": 0, "AI": 0 , "TIE": 0}



print("Welcome to Rock Paper Scissor Game \n")
print("You will be playing against an formidable AI \n BEST OF LUCK")
print("SELECT BETWEEN R,P,S")
print("WHERE R STANCE FOR ROCK")
print("WHERE P STANCE FOR PAPER")
print("WHERE S STANCE FOR SCISSOR")

def main():

    mySelection = str(input("Enter your selection :")).upper()

    if ((mySelection == "R") or (mySelection == "P") or (mySelection == "S") ):
       
        aiSelection = random.choice(options)

        print("Your Selection is", optionsFull[mySelection])
        print("AI Selection is", optionsFull[aiSelection])

        if (mySelection == aiSelection):
            print("Ouch! \n lets go another round...")
            scoreBoard["TIE"] += 1
            main()
            if (scoreBoard["TIE"] == 3):
                print("It a tie! \n lets go another round...")
                exit()
        
        if ((optionsFull[mySelection] == "ROCK") and (optionsFull[aiSelection] == "SCISSOR")):
           playerpoint()
        if ((optionsFull[mySelection] == "PAPER") and (optionsFull[aiSelection] == "ROCK")):
           playerpoint()
        if ((optionsFull[mySelection] == "SCISSOR") and (optionsFull[aiSelection] == "PAPER")):
           playerpoint()

        if ((optionsFull[aiSelection] == "ROCK") and (optionsFull[mySelection] == "SCISSOR")):
           aipoint()
        if ((optionsFull[aiSelection] == "PAPER") and (optionsFull[mySelection] == "ROCK")):
           aipoint()
        if ((optionsFull[aiSelection] == "SCISSOR") and (optionsFull[mySelection] == "PAPER")):
           aipoint()


        print("present score = Player(",scoreBoard["Player"],") : CPU (",scoreBoard["AI"],")")

        main()
        

    print("Error, Please Select Between P, R, S !!!")
    main()

def playerpoint():
    scoreBoard["Player"] += 1
    if (scoreBoard["Player"] == 3):
        print("You Are the Winner")
        exit()
    print("One Point Added to you, Lets Play another round")
 
def aipoint():
    scoreBoard["AI"] += 1
    if (scoreBoard["AI"] == 3):
        print("AI is the Winner")
        exit()
    print("One Point Added to you, Lets Play another round")

main()