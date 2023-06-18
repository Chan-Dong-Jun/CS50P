# Sunday, 28/05/2023
# CS50P Week 7

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return (count := len(re.findall(r"\bum\b", s, re.IGNORECASE)))


if __name__ == "__main__":
    main()
