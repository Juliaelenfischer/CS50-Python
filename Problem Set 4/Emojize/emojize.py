import emoji

user = input("Enter emoji: ")
output = emoji.emojize(user, language='alias')

print(output)
