#22/01/2022
#CS50P Week 3

def main():
    text = input("Fraction: ")
    gauge(convert(text))


def convert(fraction):
    while True:
        try:
            x, y =  fraction.split("/")
            x, y = int(x), int(y)
            percentage = round(x/y*100)
            if y >= x:
                return percentage
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)


if __name__ == "__main__":
    main()