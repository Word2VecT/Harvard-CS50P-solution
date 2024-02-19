def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    [X, Y] = fraction.split('/')
    if not X.isdigit() or not Y.isdigit():
        raise ValueError

    X, Y = int(X), int(Y)
    if Y == 0:
        raise ZeroDivisionError
    elif X > Y:
        raise ValueError 
    else:
        return round(X / Y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()