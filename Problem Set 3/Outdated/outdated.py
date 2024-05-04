month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    user_date = input("Date: ")
    try:
        if "/" in user_date:
            mm, dd, yyyy = user_date.split("/")
        elif "," in user_date:
            mmdd, yyyy = user_date.split(", ")
            mm, dd = mmdd.split(" ")
            mm = (month.index(mm)) + 1
        if int(mm) > 12 or int (dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break

