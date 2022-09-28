import random

print("Welcome to the guessing game!")

bound1 = input("Enter the LEFT BOUND (smallest int that can be generated): ")
bound2 = input("Enter the RIGHT BOUND (largest int that can be generated): ")

print("\nGenerating random number...\n")

numToGuess = random.randrange(int(bound1), int(bound2)+1)  # generates random number

print("Start guessing.\n")

guess = 0  # start at 0 guesses
guessedNum = None  # the guessed num that will input

while (guessedNum != numToGuess) :
    guess = guess + 1
    guessedNum = int(input("Guess " + str(guess) + " : "))
    if (guessedNum > numToGuess) :
        print("Too high. Try again.")
    if (guessedNum < numToGuess) :
        print("Too low. Try again.")
    if (guessedNum == numToGuess) :
        print("You got the number right in " + str(guess) + " tries!!")