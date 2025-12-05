print("\n === Welcome to the Number Guessing Game 🎯 === ")

import random    #This lets us pick a random number

secret_number=random.randint(1,100)    #picks a number from 1 to 100
attempts=0    #This will count how many guesses the player makes

while True:    #Repeat forever until the player guesses correctly.
    user_input = input("Guess a number between 1 and 100 (or 'q' to quit): ") #Ask the player for a number and convert it to integer.

    if user_input.lower() in ("q", "quit", "exit"):    #player can quit anytime by typing q
        print("Goodbye - Thanks for playing!")
        break

    try:     #prevents the program from crashing if input isn’t a number
        guess = int(user_input)
    except ValueError:
        print("Please enter a Valid number (or 'q' to quit).")
        continue    #if input is invalid, go back to the start of the loop.


    attempts += 1    #Add 1 to the attempts counter each time the player guesses.

    if guess < secret_number:    #If guess is smaller than secret → tell "Too low"
        print("Too low! Try again.")

    elif guess > secret_number:    #If guess is bigger → tell "Too high"
        print("Too high! Try agian")

    else:    #Player guessed correctly → show success message and break the loop
        print(f"🎉 Corrected! you guessed it in {attempts} attempts")

        break


