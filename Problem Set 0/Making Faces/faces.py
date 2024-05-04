def convert(faces):
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    return faces

#Get an input from the user
def main():
    user = input ("Write something with a face: ")
#Get and print the result
    result = convert(user)
    print(result)

main()
