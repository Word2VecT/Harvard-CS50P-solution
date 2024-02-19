import sys, requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
        print(f"${rate * n:,.4f}")
    except requests.RequestException:
        pass
    