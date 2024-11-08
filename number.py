import random
n = random.randint(1, 10)
while True:
    guess = int(input("Enter any number:"))
    if guess < n:
        print("Too Low")
    elif guess > n:
        print("Too high!")
    else:
        print("you guessed it right !!")
        break
