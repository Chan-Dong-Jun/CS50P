#30/12/2022
#CS50P Week 2

def camel_converter(camel_text):
    output = ""
    for char in camel_text:
        if char.isupper():
            output = output + "_" + char.lower()
        else:
            output = output + char
    return output

def main():
    raw_text = input("camelCase: ")
    print(f"snake_case: {camel_converter(raw_text)}")

main()