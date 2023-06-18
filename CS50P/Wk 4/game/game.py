# Saturday, 26/05/2023
# CS50P Week 4

import random

def main():
    level = -1
    user_guess = -1
    while level <= 0:
        try:
            level = int(input("Level: "))
        except:
            pass

    res = random.randint(1, level)

    while True:
        try:
            user_guess = int(input("Guess: "))
            if user_guess < 0:
                continue
            if user_guess == res:
                print("Just right!")
                break
            elif user_guess > res:
                print("Too large!")
            else:
                print("Too small!")
        except:
            pass

if __name__ == "__main__":
    main()