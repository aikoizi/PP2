import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print("Well, {}, I am thinking of a number between 1 and 20.".format(name))

    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses_taken))
            break
guess_the_number()
