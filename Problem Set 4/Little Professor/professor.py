import random

def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x, y = generate_problem(level)
        if solve_problem(x, y):
            score += 1

    print("Number of problems correct:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level

def generate_problem(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

def solve_problem(x, y):
    attempts = 0
    while attempts < 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
        else:
            if user_answer == x + y:
                return True
            else:
                print("EEE")
                attempts += 1
    print(f"Solution: {x} + {y} = {x + y}")
    return False

if __name__ == "__main__":
    main()
