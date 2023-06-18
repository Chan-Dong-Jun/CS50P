#30/12/2022
#CS50P Week 2

def main():
    twitter_text = input("Input: ")
    print(f"Output: {shorten(twitter_text)}")


def shorten(word):
    for char in word:
        if char.lower() in ("a", "e", "i", "o", "u"):
            word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()