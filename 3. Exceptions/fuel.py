while True:
    try:
        [X, Y] = input("Fraction: ").split('/')
        X = int(X)
        Y = int(Y)
        percentage = X / Y
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if X > Y:
            continue
        if percentage <= 0.01:
            print('E')
        elif percentage >= 0.99:
            print('F')
        else:
            print('{:.0%}'.format(percentage))
        break
