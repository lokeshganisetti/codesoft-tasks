import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        user_input = input("Enter your choice (stone, paper, scissors): ").strip().lower()
        if user_input in ['stone', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please choose 'stone', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Stone, Paper, Scissors!")
    
    while True:
       
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
       
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
