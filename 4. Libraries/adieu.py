import inflect
p = inflect.engine()

words = []
while True:
    word = input("Name: ")
    try:
        words.append(word)
    except EOFError:
        break
    
print("Adieu, adieu, to", p.join(words))