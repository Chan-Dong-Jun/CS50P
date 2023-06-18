#29/12/2022
#CS50P Week 0 

raw_text = input("")

def convert(text):
    return raw_text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    print(convert(raw_text))

main()