#23/01/2022
#CS50P Week 3

hashmap = {}

while True:
    try:
        item = input("").upper()
        hashmap[item] = hashmap.get(item, 0) + 1
    except ValueError:
        pass
    except EOFError:
        print("\n")
        break

for key, val in sorted(hashmap.items()):
    print(f"{val} {key}")