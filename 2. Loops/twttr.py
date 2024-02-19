str = input("Input: ")

for c in str:
    if c not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        print(c, end="")