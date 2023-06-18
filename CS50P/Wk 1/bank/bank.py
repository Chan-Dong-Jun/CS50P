#29/12/2022
#CS50P Week 1

text = input("Greeting: ").lower().lstrip()

def main():
    if text[0:5] == "hello":
        return "$0"
    if text[0] == "h":
        return "$20"
    return "$100"

print(main())