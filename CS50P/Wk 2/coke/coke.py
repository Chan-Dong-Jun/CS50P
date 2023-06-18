#30/12/2022
#CS50P Week 2

def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        payment = int(input("Insert Coin: "))
        if payment in [5, 10, 25]:
            amount_due -= payment
    change = amount_due
    print(f"Change Owed: {change * -1}")

main()