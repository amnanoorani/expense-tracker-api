import random

def guessing_game():
    print("\nWelcome to the number guessing game!")
    print("You have maximum 7 tries to guess the number between 50 to 150")
    
    number = random.randint(50, 150)
    max_tries = 7
    tries = 0
    guess = None
    
    while tries < max_tries:
        try:
            guess = float(input("Enter the number between 50 and 150: "))
            
            if guess < 50 or guess > 150:
                print("Please enter a number between 50 and 150 only!")
                continue
            
            tries = tries + 1
            
            if guess > number:
                print(f"Your guess is above the target number. Try again. (Tries left: {max_tries - tries})")
            elif guess < number:
                print(f"Your guess is below the target number. Try again. (Tries left: {max_tries - tries})")
            else:
                print(f"Congratulations! You guessed the correct number in {tries} tries!")
                break
                
        except ValueError:
            print("Invalid input! Please enter a valid number (like 75 or 100.5)")
    
    if guess != number:
        print("\nGame over! You have reached your maximum tries.")
        print(f"The correct number was {number}")

def main():
    while True:
        
        print("NUMBER GUESSING GAME")
        
        print("1. Play game")
        print("2. Exit game")
    
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            guessing_game()
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print("\nGoodbye! Thanks for playing!")
            break
            
        else:
            print("\nInvalid input! Please enter 1 or 2 only.")
            continue

main()
 