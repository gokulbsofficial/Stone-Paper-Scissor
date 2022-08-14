# STONE PAPER SCISSOR GAME IN PYTHON

import random

playerName = input("Enter your name : ")
totalRounds = int(input("Enter the rounds for this game : "))
currentRound = 1

possibleActions = ["stone", "paper", "scissor"]
playerScore = 0;
computerScore = 0;

print("\nPOSSIBLE ACTIONS ARE stone paper and scissor")
print(f"\nHii {playerName}, LETS START THE GAME\n");

# Start Game
while(currentRound <= totalRounds):
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    print("                ROUND " + str(currentRound))
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    
    userAction = input("Enter a choice (stone, paper, scissor): ")
    computerAction = random.choice(possibleActions)
    
    print(f"\nYou chose {userAction}, computer chose {computerAction}.\n")
    
    if userAction in possibleActions:
        currentRound += 1
        
        # Finding the result for the given choice
        if userAction == computerAction:
            print("\n-------------------TIE-------------------\n")
            print(f"      Both players selected {userAction}   ")
            print("\n-----------------------------------------\n")
        elif userAction == "stone":
            if computerAction == "scissor":
                computerScore+=1
                print("\n---------------WON------------------")
                print("          Stone smashes scissor!       ")
                print("-------------------------------------  ")
            else:
                playerScore+=1
                print("\n--------------WON---------------")
                print("        Paper covers Stone!       ")
                print("--------------------------------  ")
        elif userAction == "paper":
            if computerAction == "stone":
                playerScore+=1
                print("\n--------------WON----------------")
                print("        Paper covers Stone !       ")
                print("---------------------------------  ")
            else:
                computerScore+=1    
                print("\n--------------LOSE---------------")
                print("       Scissor cuts Paper!         ")
                print("---------------------------------  ")
        elif userAction == "scissor":
            if computerAction == "paper":
                playerScore+=1
                print("\n--------------WON----------------")
                print("       Scissor cuts Paper!         ")
                print("---------------------------------  ")
            else:
                computerScore+=1
                print("\n--------------LOSE---------------")
                print("       Stone smashes Scissor!      ")
                print("---------------------------------  ")
    else:
        print("\n---------------WRONG-------------------")
        print("       YOUR ACTION IS WRONG! TRY AGAIN   ")
        print("---------------------------------------  ")
	    

# Final Result 
print("\n*************************************************\n")
print("                    FINAL RESULT                     ")
print("\n*************************************************\n")

if playerScore == computerScore:
    print("\n--------------TIE--------------\n")
    print("           MATCH WAS TIE           ");
    print("\n----------------------------------\n")
elif playerScore > computerScore:
    print("\n----------------------------WINNER-------------------------\n")
    print(f"      The Winner is {playerName} and the score is " + str(playerScore));
    print("\n-----------------------------------------------------------\n")
else:
    print("\n----------------------------WINNER-------------------------\n")
    print("       The Winner is computer and the score is " + str(computerScore))
    print("\n-----------------------------------------------------------\n")
    
print("Thank you! by @GokulSreejith")
