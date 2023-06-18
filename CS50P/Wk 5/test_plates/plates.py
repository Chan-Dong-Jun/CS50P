#22/01/2022
#CS50P Week 3

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    ind = 0

    while True:
        ind += 1
        if not s[ind].isalpha():
            break
        elif ind == len(s) - 1:
            return True

    if s[ind] == "0":
        return False

    while ind < len(s) - 1:
        ind += 1
        if not s[ind].isnumeric():
            return False

    return True

if __name__ == "__main__":
    main()