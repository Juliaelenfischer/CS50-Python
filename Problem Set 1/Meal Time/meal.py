def main():
    hour = input("What the time? ")
    hour = convert(hour)
    if 7 <= hour <= 8:
        print("Breakfast time")
    elif 12 <= hour <= 13:
        print("Lunch time")
    elif 18 <= hour <= 19:
        print("Dinner time")
    else:
        print("No time to eat")


def convert(time):
    hours, minutes = time.split(":")
    return int (hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
