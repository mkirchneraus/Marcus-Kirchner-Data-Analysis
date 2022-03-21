import random
from statistics import median, mean, mode

attempt_number = []

print("Welcome to the game!")
name = input("Hello, what is your name?: ")
print("Welcome {}!".format(name))

def start_game():
    attempts = 1
    correct_number = random.randint(1,10)
    guessed_number = 0 
    while correct_number != guessed_number:
        try:
            guessed_number = int(input("Choose a number between 1 and 10: "))
            if guessed_number < 1 or guessed_number > 10: 
                attempts.append(guessed_number)
                print("Sorry your number must be between 1 and 10, please try again.")
                continue
        except ValueError:
                print("The number must be between 1 and 10 - try again!") 
        else:
            if guessed_number > correct_number:
                attempts += 1
                print("Too high! Try again: ")
                continue
            elif guessed_number < correct_number:
                attempts += 1
                print("Too low! Try again: ")
                continue 
    else: 
            attempt_number.append(attempts)
            print("You guessed it, {}! The number was {} and it took you {} tries.".format(name, guessed_number, attempts))
    return attempts

start_game()


choice = "yes"
while choice == "yes":
    choice = input("\nWant to play again? (Yes/No): ").lower()
    if choice == "yes":
        new_game = start_game() 
else:    
    print("\nGoodbye for now, {}!\n".format(name))

        
mean_attempts = mean(attempt_number)
mode_attempts = mode(attempt_number)
median_attempts = median(attempt_number)
print(f"Your average score is {mean_attempts}, your median value is {median_attempts} and your mode value is {mode_attempts}.")    