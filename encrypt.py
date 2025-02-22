import cv2
import numpy as np

def encrypt(image_path, secret_message, passcode):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    max_bytes = img.shape[0] * img.shape[1] * 3 // 8  # Max bytes available for storage
    secret_message = passcode + ":" + secret_message  # Embed passcode into the message
    secret_message += "~"  # Adding a delimiter to mark the end

    if len(secret_message) > max_bytes:
        print("Error: Message too large for the image.")
        return

    binary_msg = ''.join(format(ord(i), '08b') for i in secret_message)  # Convert to binary
    data_index = 0

    for row in img:
        for pixel in row:
            for channel in range(3):  # Modify R, G, B channels
                if data_index < len(binary_msg):
                    pixel[channel] = (pixel[channel] & 0xFE) | int(binary_msg[data_index])
                    data_index += 1

    cv2.imwrite("encryptedImage.png", img)
    print("Encryption Successful! Encrypted image saved as encryptedImage.png")

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    secret_message = input("Enter the secret message: ")
    passcode = input("Enter a passcode: ")
    encrypt(image_path, secret_message, passcode)

