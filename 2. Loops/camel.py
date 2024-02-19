camel_word = input("camelCase: ")

print("snake_case: ", end="")
for c in camel_word:
    if c.islower():
        print(c, end="")
    else:
        print(f"_{c.lower()}", end="")