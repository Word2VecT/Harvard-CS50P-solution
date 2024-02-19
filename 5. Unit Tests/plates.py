def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.strip()
    l = len(s)
    if l >= 2 and l <= 6 and s[:2].isalpha():
        for i in range(l):
            if (not s[i].isalpha()) and (not s[i].isdigit()):
                return False
            if i < l - 1:
                if s[i].isdigit() and s[i + 1].isalpha():
                    return False
                if s[i].isalpha() and s[i + 1].isdigit() and s[i + 1] == '0':
                    return False
        return True
    return False


if __name__ == "__main__":
    main()