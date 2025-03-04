#Task 5 
#Create a simple number guessing game where the user has to guess a randomly generated number.

import random 
print("Welcome to the Number Guessing Game!")  
print("I have selected a number between 1 and 100. Try to guess it!")  
number = random.randint(1, 100)  
maximum_attempts = 7 
while maximum_attempts > 0:  
    print(f"Attempts left: {maximum_attempts}") 
    user_guess = int(input("Enter your guess (1-100): "))  

    if user_guess < number:  
        print("Your guess is too low. Try again! \n")  
    elif user_guess > number:  
        print("Your guess is too high. Try again! \n")  
    else:  
        print("Congratulations! You guessed the correct number. ")
        break  

    maximum_attempts -= 1  

if maximum_attempts == 0:  
    print(f"Game over! The correct number was {number}. Better luck next time!")
