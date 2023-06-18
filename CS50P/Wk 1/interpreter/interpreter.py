# Sunday, 21 May, 2023
# CS50P Week 1

def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x, z = float(x), float(z)
    print("{:.1f}".format(calculator(x, z, y)))

def calculator(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    else:
        return operand1 / operand2

if __name__ == "__main__":
    main()
