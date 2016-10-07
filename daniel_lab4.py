#Lab4: rock paper scissors game
#Daniel Solus
"""This program uses functions to simulate the game rock, paper sciccors."""
import random

#Main program
def main():
    intro()
    done = False
    while not done:
        #Get computer choice
        num = get_comp_choice()
        comp = num_to_choice(num)

        #Get user choice
        user = get_user_choice()
        if user == None:
            break

        #display the choices
        display_choices(comp, user)

        #determine the winner and display results
        determine_winner(comp, user)
        done = keep_going()

#Functions
def get_comp_choice():
    choice = random.randint(1,3)
    return choice

def get_user_choice():
    choice = input("Enter your choice: rock, paper, or scissors. ")
    choice = choice.lower()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return choice
    else:
        print('Invalid choice')
        return None

def choice_to_num(choice):
    if choice == "rock":
        return 1
    elif choice == "paper":
        return 2
    elif choice == "scissors":
        return 3
    else:
         print("Invalid choice")

def num_to_choice(num):
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "scissors"

def display_choices(comp, user):
    print("The computer choose: {}".format(comp))
    print("The user choose: {}".format(user))

def determine_winner(comp, user):
    comp = choice_to_num(comp)
    user = choice_to_num(user)
    if user == comp:
        return print("It's a tie!")
    elif user == 1 and comp == 2:
        return print('paper beats rock.. You lose.')
    elif user == 1 and comp == 3:
        return print('rock beats scissors.. You win!')
    elif user == 2 and comp == 1:
        return print("paper beats rock.. You win!")
    elif user == 2 and comp == 3:
        return print("scissors beat paper.. You lose.")
    elif user == 3 and comp == 1:
        return print("rock beats scissors.. You lose.")
    elif user == 3 and comp == 2:
        return print("scissors beat paper.. You Win!")
    else:
        return True, print("I dont know who wins???")

def keep_going():
    play_game = input("Would you like to continue?(y/n) ")
    if play_game == 'y':
        return False
    elif play_game == 'n':
        return True
    else:
        return True, print("I do not understand.")

def intro():
    print("Let's play rock, paper, scissors!")

main()

