#02/06/2023
#CS50P Week 2

item = input("Item: ").lower()
hashmap = {"apple":130,
           "avocado":50,
           "banana":110,
           "cantaloupe":50,
           "grapefruit":50,
           "grapes":90,
           "honeydew melon":50,
           "kiwifruit":90,
           "lemon":15,
           "lime":20,
           "nectarine":60,
           "orange":80,
           "peach":60,
           "pear":100,
           "pineapple":50,
           "plums":70,
           "strawberries":50,
           "sweet cherries":100,
           "tangerine":50,
           "watermelon":80}

if item in hashmap:
    print(f"Calories: {hashmap[item]}")