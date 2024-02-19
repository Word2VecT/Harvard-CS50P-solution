from pyfiglet import Figlet
figlet = Figlet()
from random import choice
import sys

if len(sys.argv) == 3:
    if (sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts()):
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
elif len(sys.argv) == 0:
    figlet.setFont(font=choice(figlet.getFonts()))
else:
    sys.exit("Invalid usage")
    
print("Output:\n" + figlet.renderText(input("Input: ")))