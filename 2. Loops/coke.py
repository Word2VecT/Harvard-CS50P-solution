due = amount_due = 50
coin = 0

while coin <= due:
    print(f"Amount Due: {amount_due}")
    temp = int(input("Insert Coin: "))
    temp = 0 if temp not in [25, 10, 5] else temp
    coin += temp
    amount_due -= temp

print(f"Change Owed: {coin - 50}")