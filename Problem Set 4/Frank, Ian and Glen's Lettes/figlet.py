import sys
import random
from pyfiglet import Figlet

def print_usage_and_exit():
    print("Invalid usage")
    sys.exit(1)

def main():
    args = sys.argv[1:]
    num_args = len(args)

    # If no arguments provided or more than 2 arguments, print usage and exit
    if num_args == 0 or num_args > 2:
        print_usage_and_exit()

    # If two arguments provided, the first should be -f or --font
    if num_args == 2:
        if args[0] not in ["-f", "--font"]:
            print_usage_and_exit()
        font_name = args[1]
    else:
        # If only one argument provided, check if it's -f or --font
        if args[0] in ["-f", "--font"]:
            print_usage_and_exit()
        font_name = random.choice(Figlet().getFonts())

    # Check if the chosen font exists
    if font_name not in Figlet().getFonts():
        print("Invalid font")
        sys.exit(1)

    # If one argument is provided and it's not a font, print usage and exit
    if num_args == 1:
        print_usage_and_exit()

    # Get user input text
    user_input = input("Enter text: ")

    # Render and print text in the chosen font
    figlet = Figlet(font=font_name)
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
