# 26/05/2023
# CS50P Week 4

import inflect

def main():
    p = inflect.engine()
    namelist = []
    while True:
        try:
            namelist.append(input("Input: "))
        except EOFError:
            print()
            break
 
    print(f"\nAdieu, adieu, to {p.join(namelist)}")

if __name__ == "__main__":
    main()