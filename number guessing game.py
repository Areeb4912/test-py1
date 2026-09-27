import random
secret = random.randint(1,50)
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret:
        print("You got the correct number")

        break
    elif guess >secret:
        print("Your guess is too high.")
    else:
        print("your guess is too low")

    difference = abs(guess- secret)
    if difference<=5:
        print("hot")
    elif difference<=10:
        print("warm")
    elif difference<=15:
        print("cold")
    else:
        print("ice cold")
    print("lives remaining:", 5 - attempts)
    if attempts ==5:
        print("live ended")
        print("the correct number was:",secret)