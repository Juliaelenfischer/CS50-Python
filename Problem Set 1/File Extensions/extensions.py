#prompts the user for the name of a file
#outputs that file’s media type if the file’s name ends

#el usuario pone cat.gif ---> el programa tiene que devolver image/gif

#- gif - image/gif
 #- jpeg - image / jpeg
 #- jpg - image /jpeg
 #- png - image / png
 #- pdf - application/ pdf
 #- txt - text / plain
 #- zip - aplication / zip




file = input ("Type the file: ").split('.')[-1].lower().strip()
file = '.' + file.split('.')[-1]
match file:
    case ".gif":
        print("image/gif")
    case ".jpeg" | ".jpg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


