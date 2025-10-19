from PIL import Image

def str_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

def hide_message(image_path, secret_message, output_path):
    img = Image.open(image_path).convert('RGB')
    binary_message = str_to_binary(secret_message) + '11111111' # Add a delimiter

    if len(binary_message) > img.width * img.height * 3:
        raise ValueError("Message is too long for this image.")

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
                print(f"Message successfully hidden in {output_path}")
                return

# --- Use the script ---
# 1. Download an image and save it as 'source_yule_ball.jpg'
# 2. Run this script
hide_message('source_yule_ball.jpg', 
             "Constant vigilance! They're all impostors, just like that fake 'Sword' in the Headmaster's Office. My only trusted contact is @QuibblerSnitch9",
             'Yule_Ball_Photo.png') # This is the file you will give to participants