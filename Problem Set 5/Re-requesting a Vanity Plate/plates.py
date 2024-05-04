def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Que tenga entre 2 y 6 caracteres alfanumericos
    if 2 <= len(s) <= 6 and s.isalnum():
         # Verifica que sean letras
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                if s[2].isdigit() and s[2] != '0':
                    return True
    return False


main()
