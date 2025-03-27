import sys
from PIL import Image


def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = list(image.getpixel((col, row)))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':
            break
        message += char
    return message


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        sys.exit(1)
    encoded_image_path = sys.argv[1]
    message = decode_image(encoded_image_path)
    print("Decoded message:", message)
