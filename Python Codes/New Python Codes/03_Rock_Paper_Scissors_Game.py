import random, sys      #Importing the necessary modules

print ("######################\nROCK, PAPER, SCISSORS\n######################")

#Declaring the variabels
tie=0
win=0
lose=0

for i in range(3):
    print ("Enter your move : (r)ock (p)aper (s)cissors or (q)uit" )

############### This the First and a simple logic to pull out random characters for the CPU move ################################# 

    # cpu_move = random.randint(1,3) #CPU take/generate input

    # if cpu_move == 1:
    #     cpu_move = "r"
    # elif cpu_move == 2:
    #     cpu_move = "p"
    # elif cpu_move == 3:
    #     cpu_move = "s"

#####################################################################################################################    

############### This the second logic to pull out random characters for the CPU move ################################# 

    mylist = ["p","r","s"]
    cpu_move = random.choice(mylist)

######################################################################################################################

    player_move = str(input()) #Player provide input

    #Display what player have chosen
    if player_move == "r":
        print ("ROCK versus ....")
    elif player_move == "p":
        print ("PAPER versus ....")
    elif player_move == "s":
        print ("SCISSORS versus ....")
    elif player_move == "q":
        print ("Quitting the game.")
        sys.exit()                       #Quit the Game.
    else:
        print("Kindly enter a valid entry.")
        break
    
    #Display what CPU have chosen
    if cpu_move == "r":
        print ("ROCK")
    elif cpu_move == "p":
        print ("PAPER")
    elif cpu_move == "s":
        print ("SCISSORS")
    else:
        print("Kindly enter a valid entry.")
    

    #Core-logic and here we compae the Player value with that of the CPU value
    if player_move == cpu_move :
        print ("It is a tie")
        tie=tie+1

    elif player_move == "p" and cpu_move == "r":
        print("You win!")  
        win=win+1

    elif player_move == "p" and cpu_move == "s":
        print("You lose!")  
        lose=lose+1

    elif player_move == "r" and cpu_move == "p":
        print("You lose!")  
        lose=lose+1    

    elif player_move == "r" and cpu_move == "s":
        print("You win!") 
        win=win+1

    elif player_move == "s" and cpu_move == "p":
        print("You win!")
        win=win+1

    elif player_move == "s" and cpu_move == "r":
        print("You lose!")
        lose=lose+1

    else :
        print("You lose!")
        lose=lose+1

    #Prints the Game Score
    print("Score Updates are as below:\nWins={0}  Loss={1}  Tie={2}\n\n ".format(win,lose,tie) )    