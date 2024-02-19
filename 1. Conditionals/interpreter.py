exp = input("Expression: ").strip()

for y in ["+", "-", "*", "/"]:
    pos = exp.find(y)
    if (pos != -1):
        break

x = int(exp[: pos - 1])
z = int(exp[pos + 2:])

match y:
    case "+": ans = x + z
    case "-": ans = x - z
    case "*": ans = x * z
    case "/": ans = x / z

print(f"{ans:.1f}")