import random


top_of_range = input("Enter a top of range number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Enter number larger than 0 next time!")
else:
    print("Please enter number next time")
    quit()

random_number = random.randrange(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue
    if user_guess == random_number:
        print("Correct!")
        break
    else:
        print("Incorrect")

print("You got it in", guess, "guesses!")