import sys
from PIL import Image


def encode_image(image_path, message):
    image = Image.open(image_path)
    width, height = image.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '00000000'  # End of message delimiter
    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(image.getpixel((col, row)))
            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[
                        color_channel], '08b')[:-1] +
                                               binary_message[data_index], 2)
                    data_index += 1
            image.putpixel((col, row), tuple(pixel))
            if data_index >= len(binary_message):
                break
    encode_image_path = image_path.split('.')[0] + '_encoded.png'
    image.save(encode_image_path)
    print("Steganography complete. Encoded image saved as:", encode_image_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        sys.exit(1)
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)
