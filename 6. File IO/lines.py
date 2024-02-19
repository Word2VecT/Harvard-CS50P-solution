import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif (len(sys.argv)) == 1:
    sys.exit("Too few command-line arguments")
else:
    if (not sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")
    try:
        cnt = 0
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if (line.startswith("#") or line == ""):
                    continue
                cnt += 1
        print(cnt)
    except FileNotFoundError:
        sys.exit("File does not exist")