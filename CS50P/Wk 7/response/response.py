# Sunday, 28/05/2023
# CS50P Week 7

from validator_collection import validators

def main():
    try:
        if validators.email(input("What's your email address? ")):
            print("Valid")
    except:
        print("Invalid")


if __name__ == "__main__":
    main()