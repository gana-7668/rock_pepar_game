import random


def display_welcome():
   
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose either 'rock', 'paper', or 'scissors' to play.")

def get_user_choice():
    
    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input. Please enter either 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    """Display the user's choice, the computer's choice, and the result."""
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    print(result)

def play_again():
    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")

def main():
    display_welcome()
    play_again_flag = True
    user_score = 0
    computer_score = 0
    while play_again_flag:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Score: You {user_score} - Computer {computer_score}")
        play_again_flag = play_again()

if __name__ == "__main__":
    main()


