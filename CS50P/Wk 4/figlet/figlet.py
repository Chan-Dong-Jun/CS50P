#26/02/2022
#CS50P Week 4
# need touch up logic not guarded properly

from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    ascii_fonts = figlet.getFonts()
    if len(sys.argv) == 3 and sys.argv[2] not in ascii_fonts:
            sys.exit("Please input a valid font.")
    if len(sys.argv) == 2:
        sys.exit("Please input the correct number of command-line argument.")
    if len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
        sys.exit('Please input "-f" or "--font" as the first command-line argument.')

    text = input("Input: ")

    if len(sys.argv) == 3:
        print(ascii(text, font = sys.argv[2]))
    else:
        print(ascii(text))

def ascii(raw_text, font = "random"):
    figlet = Figlet()
    ascii_fonts = figlet.getFonts()
    if font == "random":
        figlet.setFont(font= random.choice(ascii_fonts))
        return figlet.renderText(raw_text)
    else:
        figlet.setFont(font= font)
        return figlet.renderText(raw_text)


if __name__ == "__main__":
    main()