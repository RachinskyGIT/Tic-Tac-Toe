######################### Beginning of the game code ######################### 
######################### The game code is completely written by RachinskyGIT ######################### 
#########################           https://github.com/RachinskyGIT           ######################### 

import os
import time

def game(turn, gamedict):
    os.system('cls') #clear the screen every turn
    gameend=False
    if gamedict=="start":
        turn=True #"X"-player start the game (if False -> "O"-player start)
        fielddict = {"1":".","2":".","3":".","4":".","5":".","6":".","7":".","8":".","9":"."}
    else:
        fielddict=gamedict

    #n's transfer cell value from dictionary to grid
    n1,n2,n3,n4,n5,n6,n7,n8,n9 = [list(fielddict.items())[0][1],list(fielddict.items())[1][1]\
                              ,list(fielddict.items())[2][1],list(fielddict.items())[3][1]\
                                ,list(fielddict.items())[4][1],list(fielddict.items())[5][1]\
                                    ,list(fielddict.items())[6][1],list(fielddict.items())[7][1]\
                                        ,list(fielddict.items())[8][1]]
    
    #The Grid
    line = f'\n\n\n\
    \u269E \u2655 \u2655  \u2655 \u2654 \u2655 \u2655 \u2655 \u269F\n\
    |1    |2    |3    |\n\
    |  {n1}  |  {n2}  |  {n3}  |\n\
    |_____|_____|_____|\n\
    |4    |5    |6    |\n\
    |  {n4}  |  {n5}  |  {n6}  |\n\
    |_____|_____|_____|\n\
    |7    |8    |9    |\n\
    |  {n7}  |  {n8}  |  {n9}  |\n\
    |_____|_____|_____|\n    "stop" for endgame\n'

    print(line)
    # print('Choose "stop" to interrupt the game')

    if turn==True:
        print('Player "X" turn\n')
    else:
        print('Player "O" turn\n')

    #Victory condition
    if (n1==n2==n3!=".") or (n4==n5==n6!=".") or (n7==n8==n9!=".") or\
       (n1==n4==n7!=".") or (n2==n5==n8!=".") or (n3==n6==n9!=".") or\
       (n1==n5==n9!=".") or (n3==n5==n7!="."):
        gameend=True 

    #Draw condition and action
    if (n1!=".") and (n2!=".") and (n3!=".") and (n4!=".") and (n5!=".") \
        and (n6!=".") and (n7!=".") and (n8!=".") and (n9!=".") and (gameend!=True):
        print("The Game ended in a Draw -_-'\nGame will close in 5 seconds.")
        time.sleep(5)
        quit()

    #Victory action  
    if gameend==True:
        print("End of the Game")
        time.sleep(0.5)
        if turn==True:
            print('The "O"-player is a winner! Congratulations ^_^')
        else:
            print('The "X"-player is a winner! Congratulations ^_^')
        time.sleep(1.5)
        quit()

    goodchoice = ["1","2","3","4","5","6","7","8","9"]
    flag=True
    while flag==True:
        choice = input("Choice area (1-9): ")
        if choice == "stop":
            print("You choosed to end the game.\nGame will close in 5 seconds.")
            time.sleep(5)
            quit()
        if not choice in goodchoice:
            print("Please, insert number between 1 and 9")
            continue
        if (fielddict[choice]=="X") or (fielddict[choice]=="O"):
            print("This area is already taken. Please choose another area :)")
            continue           
        if choice in goodchoice:
            flag=False
            if turn==True:
                fielddict[choice]="X"
            else:
                fielddict[choice]="O"
            turn = not turn
            break
    game(turn, fielddict)
######################### End of game code ######################### 
######################### The game code is completely written by RachinskyGIT ######################### 
#########################           https://github.com/RachinskyGIT           ######################### 


        
game(0,"start")





