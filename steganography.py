from PIL import Image


def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary):
    chars = [
        binary[i:i + 8]
        for i in range(0, len(binary), 8)
    ]
    return ''.join(chr(int(char, 2)) for char in chars)


def encode_image(image_path, secret_message, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")

    secret_message += "####"
    binary_message = text_to_binary(secret_message)

    data_index = 0

    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            if data_index < len(binary_message):
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1

            if data_index < len(binary_message):
                g = (g & ~1) | int(binary_message[data_index])
                data_index += 1

            if data_index < len(binary_message):
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1

            pixels[x, y] = (r, g, b)

            if data_index >= len(binary_message):
                img.save(output_path)
                return

    img.save(output_path)


def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")

    binary_data = ""

    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    decoded_text = ""

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i + 8]

        if len(byte) < 8:
            break

        decoded_text += chr(int(byte, 2))

        if decoded_text.endswith("####"):
            return decoded_text[:-4]

    return decoded_text