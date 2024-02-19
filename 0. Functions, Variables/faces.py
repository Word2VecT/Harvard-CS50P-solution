def main():
    res = convert(input());
    print(res)

def convert(to):
    return to.replace(":)", "🙂").replace(":(", "🙁")

main()