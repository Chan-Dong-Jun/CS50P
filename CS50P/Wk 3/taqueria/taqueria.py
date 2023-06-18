#23/01/2022
#CS50P Week 3

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        selection = input("Item: ").title()
        if selection in menu:
            total += menu[selection]
            print(f"Total: ${total:.2f}")
    except (ValueError, KeyError):
        pass
    except EOFError:
        print("\n")
        break
