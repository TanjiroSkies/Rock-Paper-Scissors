import random

def RPSvalue():

 RPSvalue = random.ranint(1,9)
 return RPSvalue


while True:
 
 choice = input("Choose from Rock, Paper, Scissors: ")

 if choice in ('Rock', 'Paper', 'Scissors'):

    
    
    if choice == 'Rock':
        
        options = ["1", "2","3"]
        choice = random.choice(options) 

        if choice == '1':
            print("Rock! Welp, its a tie!")

        elif choice == '2':
            print("Paper! I win!")

        elif choice == '3':
            print("Scissors! Aw no! I lose!") 


    if choice == 'Paper':

        options = ['1', '2','3']
        choice = random.choice(options)

        if choice == '1':
            print("Rock! Aw no I lose!")

        elif choice == '2':
            print("Paper! Welp, its a tie!")

        elif choice == '3':
            print("Scissors! I win!")


    if choice == 'Scissors':

        options = ['1', '2','3']
        choice = random.choice(options)

        if choice == '1':
            print("Rock! I win!")

        elif choice == '2':
            print("Paper! Aw, i lose!")

        elif choice == '3':
            print("Scissors! Welp, its a tie!")
                             

 NewGame = input("What you just said was either an invalid input or that you already played. Do you want to play again? (Y/N)")     
 if NewGame == "N":
     break