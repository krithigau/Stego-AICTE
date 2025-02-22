import cv2
import numpy as np

def decrypt(image_path, passcode):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    binary_msg = ""
    found_end = False  # Flag to stop unnecessary iterations

    for row in img:
        for pixel in row:
            for channel in range(3):  # Extract from R, G, B channels
                binary_msg += str(pixel[channel] & 1)

                # Stop early if we detect the '~' character (end of message)
                if len(binary_msg) % 8 == 0:
                    char = chr(int(binary_msg[-8:], 2))
                    if char == "~":
                        found_end = True
                        break
            if found_end:
                break
        if found_end:
            break

    # Convert binary to text
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    extracted_msg = "".join([chr(int(char, 2)) for char in chars])

    # Extract actual message before '~' delimiter
    if "~" in extracted_msg:
        extracted_msg = extracted_msg[:extracted_msg.index("~")]

    # Separate stored passcode and secret message
    stored_passcode, secret_message = extracted_msg.split(":", 1)

    if passcode == stored_passcode:
        print("Decryption Successful! Secret Message:", secret_message)
    else:
        print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    image_path = input("Enter the encrypted image path: ")
    passcode = input("Enter the passcode: ")
    decrypt(image_path, passcode)
