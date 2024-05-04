text = input("Write a text: ")
vocals = ["a", "e", "i", "o", "u"]

for vocal_text in text:
    if vocal_text.casefold() not in vocals:
        print(vocal_text, end="")
