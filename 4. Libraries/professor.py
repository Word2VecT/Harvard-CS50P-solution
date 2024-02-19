import random

def main():
    score = 0
    level = get_level()
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        answer = X + Y
        for i in range(3):
            try:
                calculate = int(input(f"{X} + {Y} = "))
                if calculate == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        print(f"{X} + {Y} = {answer}")
            except ValueError:
                pass
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    return random.randint(pow(10, level - 1), pow(10, level) - 1)

if __name__ == "__main__":
    main()