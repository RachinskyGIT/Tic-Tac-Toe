######################### Beginning of the game code ######################### 
######################### The game code is completely written by RachinskyGIT ######################### 
#########################           https://github.com/RachinskyGIT           ######################### 

import os
import time
import random

def comp_game(turn,gamedict,comp):
    gameend=False
    if gamedict=="start":
        os.system('cls') #clear the screen before game initilization
        turn=True #by default the "X"-player start the game (if False -> "O"-player start)
        fielddict = {"1":".","2":".","3":".","4":".","5":".","6":".","7":".","8":".","9":"."}
        #fielddict - Main dictionary, field values are stored in this variable, the dictionary is transferred by recursion
        
        print("Do you want to play with each other, or with the computer?\n") 
        inp=None
        while ((inp!="C") and (inp!="P")):  #Choice of the opponent
            inp=input('Choose C for Computer, P for Player: ')
            if type(inp)==str:
                inp=inp.upper()
                if ((inp=="P") or (inp=="C")):
                        continue
                else:
                    print('Please, insert P or insert C letter')
                    continue
            else:
                print('Please, insert P or insert C letter')
                continue
        if inp=="C":            #Choice of the side
            print('\nWho do you want to play? For "X" or for "O"?')
            while ((inp!="X") and (inp!="O")):  
                inp=input('Choose X\O: ')
                if type(inp)==str:
                    inp=inp.upper()
                    if ((inp=="X") or (inp=="O")):
                        comp=inp
                        continue
                    else:
                        print('Please, insert X or insert O letter')
                        continue
                else:
                    print('Please, insert X or insert O letter')
                    continue
        del inp
    else:#For all subsequent recursive iterations except the initial iteration. Passing dictionary value -> values on grid.
        fielddict=gamedict

    os.system('cls') #clear the screen every turn

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


    #Computer step (it chooses an area randomly)
    if ((comp=="O") and (turn==True)) or ((comp=="X") and (turn==False)):
        print("Computer's turn")
        time.sleep(random.uniform(1.5, 2.5))
        complist = []
        for key in fielddict:
            if fielddict.get(key)==".":
                complist.append(key)
        random.shuffle(complist)
        choice=complist[0]
        if turn==True:
            fielddict[choice]="X"
        else:
            fielddict[choice]="O"
        del complist
        turn = not turn
        comp_game(turn,fielddict,comp)


    #Player step    
    else:
        goodchoice = ["1","2","3","4","5","6","7","8","9"]
        flag=True
        while flag==True:
            choice = input("Choice area (1-9): ")
            if choice == "stop":
                print("You choosed to end the game.\nGame will close in 3 seconds.")
                time.sleep(3)
                os.system('cls')
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
        comp_game(turn,fielddict,comp)
######################### End of game code ######################### 
######################### The game code is completely written by RachinskyGIT ######################### 
#########################           https://github.com/RachinskyGIT           ######################### 


        
comp_game(0,"start",0)





