import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        to_time = standardize(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {to_time}"
    else:
        raise ValueError

def standardize(hour, minute, meridiem):
    if hour == "12":
        if meridiem == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if meridiem == "AM":
            hour = f"{int(hour):02}"
        else:
            hour = f"{int(hour)+12}"
    if minute is None:
        minute = "00"
    else:
        minute = f"{int(minute):02}"
    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
