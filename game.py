import random

def match_check(user, computer):
    if user == computer:
        print("DRAW")

    elif user == 1: 
        if computer == 2:
            print("Computer WIN")

        elif computer == 3:
            print("User WIN")

    elif user == 2:
        if computer == 1:
            print("User WIN")
        elif computer == 3:
            print("Computer WIN")

    elif user == 3:
        if computer == 1:
            print("Computer WIN")
        elif computer == 2:
            print("User WIN")


print("Welcome to Rock, Paper, Scissor Game")

while True:
    userInput = int(input("1: Rock\n2: Paper\n3: Scissor\nEnter your selection: "))
    computerInput = random.randint(1,3)

    if userInput != -1:
        match_check(userInput, computerInput)
    else:
        break


    