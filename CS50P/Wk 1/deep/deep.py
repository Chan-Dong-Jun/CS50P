#29/12/2022
#CS50P Week 1

def main():
    
    user_ans = input("What is the Answer to the Greatest Question of Life, the Universe and Everything? ")

    accepted_response = ["42", "forty-two", "forty two"]
    if user_ans.lower().strip() in accepted_response:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
