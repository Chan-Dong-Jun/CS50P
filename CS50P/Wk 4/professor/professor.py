# Saturday, 26/05/2023
# CS50P Week 4

import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        res = X + Y
        tries = 3
        while tries > 0:
            user_res = input(f"{X} + {Y} = ")
            if str(res) == user_res:
                score += 1
                break
            else:
                tries -= 1
                print("EEE")
        print(res)
    print(f"Score: {score}")

def get_level():
    level = 0
    while not 1 <= level <= 3:
        try:
            level = int(input("Level: "))
        except:
            pass
    return level

def generate_integer(level):
    if not 1 <= level <= 3:
        raise ValueError()
    no_digits = {1 : [0,9], 2 : [10,99], 3 : [100,999]}
    return random.randint(no_digits[level][0], no_digits[level][1])

if __name__ == "__main__":
    main()
