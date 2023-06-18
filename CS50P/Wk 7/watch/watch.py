# Sunday, 28/05/2023
# CS50P Week 7

import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if not (url := re.search(r'src="https?://(?:www\.)?youtube.com/embed/(\w+)"', s)):
        return None

    return f"https://youtu.be/{url.group(1)}"

if __name__ == "__main__":
    main()
