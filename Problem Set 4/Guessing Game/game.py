from random import randint
from sys import exit

def input_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if n <= 0:
                pass
            else:
                return n

def generate_random_number(n):
    return randint(1, n)

def input_guess():
    while True:
        try:
            g = int(input("Guess: "))
        except ValueError:
            pass
        else:
            return g

def evaluate_guess(g, x):
    if g > x:
        print("Too large!")
    elif g < x:
        print("Too small!")
    else:
        exit("Just right!")

def main():
    n = input_level()
    x = generate_random_number(n)

    while True:
        g = input_guess()
        evaluate_guess(g, x)

if __name__ == "__main__":
    main()

