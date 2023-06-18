#22/01/2022
#CS50P Week 3


while True:
    try:
        x, y =  input("Fraction: ").split("/")
        x, y = int(x), int(y)
        percentage = round(x/y*100)
        if y >= x:
            break
    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
