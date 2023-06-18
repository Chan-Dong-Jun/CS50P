#30/12/2022
#CS50P Week 2

def main():
    twitter_text = input("Input: ")
    for char in twitter_text:
        if char.lower() in ("a", "e", "i", "o", "u"):
            twitter_text = twitter_text.replace(char, "")
    print(f"Output: {twitter_text}")

main()