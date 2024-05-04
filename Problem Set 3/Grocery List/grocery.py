def main():
    grocery_list = {}

    try:
        while True:
            try:
                item = input().lower().strip()
                grocery_list[item] = grocery_list.get(item, 0) + 1  # Incrementa el valor en el diccionario
            except EOFError:
                break  # Salimos del bucle si el usuario ha terminado la entrada
    except:
        pass

    sorted_items = sorted(grocery_list.items())  # Ordena alfabéticamente

    # Imprime la lista de compras 
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
