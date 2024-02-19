months = [
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
    date = input("Date: ").strip()

    M = D = Y = 0

    if (date[0].isdigit()):
        date = date.split('/')
        try:
            [M, D, Y] = [int(num) for num in date]
        except ValueError:
            continue
    else:
        date = date.split()
        try:
            if (len(date) != 3 or date[1][-1] != ','):
                continue
            M = months.index(date[0]) + 1
            [D, Y] = [int(date[1][:-1]), int(date[2])]
        except ValueError:
            continue

    if (D > 31 or M > 12):
        continue
    print(f"{Y:04}-{M:02}-{D:02}")
    break