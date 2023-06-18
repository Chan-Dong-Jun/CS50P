# Sunday, 28/05/2023
# CS50P Week 7

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        time = re.search(r"(\d+)(:)?([0-6][0-9])? (AM|PM) to (\d+)(:)?([0-1][0-9])? (AM|PM)", s).groups()
    except:
         raise ValueError


    hr_start, hr_end = int(time[0]), int(time[4])
    if not 1 <= hr_start <= 12 or not 1 <= hr_end <= 12:
            raise ValueError
    hr_start = hr_start % 12 + 12 if time[3] == "PM" else hr_start % 12
    hr_end = hr_end % 12 + 12 if time[7] == "PM" else hr_end % 12

    if time[1]:
        min_start, min_end = int(time[2]), int(time[6])
        if not 0 <= min_start <= 60 or not 0 <= min_end <= 60:
            raise ValueError

        return f"{hr_start:02}:{min_start:02} to {hr_end:02}:{min_end:02}"
    return f"{hr_start:02}:00 to {hr_end:02}:00"

if __name__ == "__main__":
    main()
