import random

print("Winning rule are: \n"
      + "rock V/S paper --> paper wins"
      + "rock V/S Scissors --> rock wins"
      + "paper V/S Scissors --> Scissors wins")

while True:
    print("Please enter your choice \n 1- rock \n 2- paper \n 3-Scissors")
    choice=int(input("Enter your choice:"))

    while choice > 3 or choice < 1:
        print("Invalid number please choose between 1,2 and 3!!")

    if choice ==1:
        choice_name='rock'
    elif choice == 2:
        choice_name='paper'
    else :
        choice_name='Scissors'   

    print("User's choice is: \n",choice_name)
    print("\n Now it's computer's turn:")


    comp_choice =  random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3) 

    if comp_choice == 1:
        comp_choice_name='rock'

    elif comp_choice == 2:
        comp_choice_name='paper'

    else :
        comp_choice_name='Scissors'  

    print("Computer's choice is:\n",comp_choice_name)
    print(choice_name, "V/S", comp_choice_name) 

    #condition for a draw
    if choice == comp_choice:
        print("It's a draw", end="")
        result="DRAW!!"

    if (choice==1 and comp_choice==2):
        print("paper wins=>", end="")
        result="paper"
    elif (choice==2 and comp_choice==1):
        print("paper wins=>", end="")
        result="paper"

    if (choice==1 and comp_choice==3):
        print("rock wins=>", end="")
        result="rock" 
    elif (choice==3 and comp_choice==1):
        print("rock wins=>", end="")
        result="rock"  

    if (choice==2 and comp_choice==3):
        print("Scissors wins=>", end="")
        result="Scissors"  
    elif (choice==3 and comp_choice==2):
        print("Scissors wins=>", end="")
        result="Scissors"   

    if result=="DRAW!!":
        print("IT IS A TIE !!")  
    if result == choice_name:
        print(" <== USER WINS ==>!!")
    else:
        print(" <== COMPUTER WINS ==>!!")  

    print("Do you want to play again? (Y/N)")
    #if user inputs n or N then condition is true
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")                               
