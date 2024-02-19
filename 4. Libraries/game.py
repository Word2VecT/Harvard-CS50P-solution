import random

answer = 0

while True:
    try:
        n = int(input("Level: "))
        answer = random.randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0 or guess > n:
            continue
        if guess == answer:
            print("Just right!")
            break
        elif guess > answer:
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        pass