def main():
    x = get_input()
    print(f"{x}") #imprime el resultado en porcentaje

def get_input():
    while True:
        try:
            input_user = input("Fraction: ")
            y, x = input_user.split("/")
            y = int(y)
            x = int(x)

            if x == 0:
                raise ZeroDivisionError("Can't be 0")

            percentage = (y / x) * 100  #calcular el porcentaje

            if y <= x:
                if percentage >= 99:
                    return "F"
                elif percentage <= 1:
                    return "E"
                else:
                    return f"{round(percentage)}%"
            else:
                print("Denominator must be greater or equal than nominator")
        except ValueError:
            print ("Enter valid numbers")
        except ZeroDivisionError:
            print ("Denominator can't be 0")

main()
