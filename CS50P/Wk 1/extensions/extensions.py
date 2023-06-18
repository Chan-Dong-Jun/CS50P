# Sunday, 21 May, 2023
# CS50P Week 1

def main():
    text = input("File name: ")
    text = text.split(".")[-1].lower().strip()
    print(convert(text))


def convert(input):
    hashmap = {"gif": "image/gif", "jpg": "image/jpeg" ,"jpeg": "image/jpeg" ,"png": "image/png" ,"pdf":"application/pdf","txt":"text/plain","zip":"application/zip"}
    if input in hashmap:
        return hashmap[input]
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()