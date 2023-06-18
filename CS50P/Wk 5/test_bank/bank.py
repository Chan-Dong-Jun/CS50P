#29/12/2022
#CS50P Week 1

def main():
    text = input("Greeting: ")
    print(f"${value(text)}")

def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting[0:5] == "hello":
        return 0
    if greeting[0] == "h":
        return 20
    return 100

if __name__ == "__main__":
    main()

