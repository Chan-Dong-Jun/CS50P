#02/06/2023
#CS50P Week 6

import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    file = sys.argv[1]
    res = 0

    try:
        with open(file, "r") as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                if not line.strip():
                    continue
                res += 1
    except:
        sys.exit("File does not exist")

    print(res)

if __name__ == "__main__":
    main()