grocery = {}

while True:
    try:
        item = input().upper()
        if item not in grocery:
            grocery[item] = 0
        grocery[item] += 1
    except EOFError:
        break

for item in sorted(grocery):
    print(grocery[item], item)