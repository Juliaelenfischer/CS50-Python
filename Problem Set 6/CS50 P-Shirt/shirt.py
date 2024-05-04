from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python edit_photo.py <input_image> <output_image>")

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    formats = [".jpg", ".jpeg", ".png"]
    input_extension = os.path.splitext(input_image)[1].lower()
    output_extension = os.path.splitext(output_image)[1].lower()

    if output_extension not in formats:
        sys.exit("Invalid output format")

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    edit_photo(input_image, output_image)


def edit_photo(input_image, output_image):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_image) as img:
            img_cropped = ImageOps.fit(img, shirt.size)
            img_cropped.paste(shirt, mask=shirt)
            img_cropped.save(output_image)
    except FileNotFoundError:
        sys.exit("Input image does not exist")


if __name__ == "__main__":
    main()
