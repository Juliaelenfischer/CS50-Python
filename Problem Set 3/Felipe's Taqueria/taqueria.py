def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    cost = 0

    while True:
        try:
            user = input("Item: ").title()
            if user in menu:
                cost += menu[user]
                print (f"${cost:.2f}")
            else:
                print("Invalid Item")
        except EOFError:
            print(f"Total cost: ${cost:.2f}")
            return

if __name__ == "__main__":
    main()

