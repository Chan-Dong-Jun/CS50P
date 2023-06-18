# Saturday, 27/05/2023
# CS50P Week 7

import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        if not (extracted_ip := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip).groups()):
            return False
    except:
        return False

    for sub_ip in extracted_ip:
        if not 0 <= int(sub_ip) <= 255:
            return False
    return True

if __name__ == "__main__":
    main()
