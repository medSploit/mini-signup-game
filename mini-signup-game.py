import getpass
import random
succ = False

def signup():
    name = input("Enter username: ")
    passw = getpass.getpass("Enter password: ")
    with open('passwd.txt', 'a') as x:
        x.write(name + "|" + passw + "\n")

def login():
    name = input("Enter username: ")
    passw = getpass.getpass("Enter password: ")
    global succ
    found = False
    with open('passwd.txt', 'r') as x:
        for line in x.readlines():
            data = line.strip()
            user, passw_d = data.split('|')
            if user == name and passw_d == passw:
                succ = True
                found = True
                print("Login Successful")
                break
    if not found:
        print("Login Failed")

def prc_game():
    user_wins = 0
    computer_wins = 0
    options_list = ["r", "p", "s"]
    rules = {("r", "s"): "win",
             ("s", "p"): "win",
             ("p", "r"): "win"}
    
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice not in options_list:
            print("Invalid choice, try again")
            continue
        computer_choice = random.choice(options_list)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Draw")
        elif (user_choice, computer_choice) in rules:
            print("You win this round!")
            user_wins += 1
        else:
            print("You lose this round!")
            computer_wins += 1

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("\n--- Game Over ---")
    if user_wins > computer_wins:
        print("Bravo! You win overall!")
    elif user_wins == computer_wins:
        print("It's a draw overall!")
    else:
        print("Sorry, you lost overall!")

    print("Your score:", user_wins)
    print("Computer score:", computer_wins)

def num_guess():
    random_num = random.randint(1, 100)
    while True:
        try:
            choice = int(input("Guess the number between 1 and 100:\n"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == random_num:
            print("Congratulations! You guessed the number!")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == "y":
                random_num = random.randint(1, 100)
                continue
            elif play_again == "n":
                print("Bye bye!")
                break
            else:
                print("Invalid input. Exiting the game.")
                break
        elif choice > random_num:
            print("Too high!")
        else:
            print("Too low!")

print("Welcome to the Mini Sign-In and Sign-Up System")
while True:
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Exit")    
    try:
        choice = int(input('>> '))
        if choice == 1:
            signup()
        elif choice == 2:
            login()
            break
        elif choice == 3:
            break
        else:
            print("Invalid choice! Try again.\n")
    except ValueError:
        print("Invalid input! Try again.\n")
if succ:
    while True:
        print("Choose a game or exit:")
        print("1. Rock Paper Scissors")
        print("2. Number Guessing")
        print("3. Exit")
        try:
            choice = int(input('>> '))
            if choice == 1:
                prc_game()
            elif choice == 2:
                num_guess()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Try again.\n")
        except ValueError:
            print("Invalid input! Try again.\n")
