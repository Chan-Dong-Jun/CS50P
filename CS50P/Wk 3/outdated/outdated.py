#23/01/2022
#CS50P Week 3

calendar = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            m, d, y = date.split("/")
        if " " in date and "," in date:
            m, d, y = date.split(" ")
            m = calendar.index(m) + 1
            d = d.rstrip(",")
        d, m, y = int(d), int(m), int(y)
        if d <= 31 and m <= 12:
            break
    except (ValueError, NameError):
        pass

print(f"{y}-{m:02}-{d:02}")