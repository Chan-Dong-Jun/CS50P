#13/02/2022
#01/06/2023
#CS50P Week 8

from datetime import date
import sys
import inflect

def main():
    print(convert_mins(input("Date of Birth: ")))


def convert_mins(DOB):
    p = inflect.engine()
    date_today = date.today()

    try:
        DOB = date.fromisoformat(DOB)

    except:
        sys.exit("Invalid Date")

    time = (date_today - DOB).days * 1440
    return p.number_to_words(time).capitalize().replace("and ", "") + " minutes"


if __name__ == "__main__":
    main()