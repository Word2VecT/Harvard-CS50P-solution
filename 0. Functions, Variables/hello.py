# Ask the user for their name
def main():
    name = input("What's your name?").strip().title()
    hello(name)
    hello()

def hello(to = "World"):
    print("Hello,", to)
    
main()