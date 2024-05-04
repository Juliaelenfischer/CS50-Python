coins = [25, 10, 5]
price = 50

def paid_coke():
    person_paid = 0
    while person_paid < price:
        print(f"Amount Due: {price - person_paid}")
        inserted_coin = input("Insert Coin: ")
        if inserted_coin.isdigit():
            inserted_coin = int(inserted_coin)
            if inserted_coin in coins:
                person_paid += inserted_coin
            else:
                print("Invalid coin. Try again")
        else:
            print("Invalid input. Try again")
    return person_paid

def main():
    print ("Insert Coin")
    amount_paid = paid_coke()
    change = amount_paid - price
    if change > 0:
        print(f"Change Owed: {change}")
    elif change == 0:
        print("Change Owed: 0")

main()
