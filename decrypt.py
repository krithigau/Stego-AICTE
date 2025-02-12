import cv2

def decrypt(image_path, password):
    img = cv2.imread("Mee.jpg")  # Read the encrypted image
    if img is None:
        print("Error: Image not found!")
        return

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    message = ""

    user_password = input("Enter passcode for decryption: ")
    if user_password != password:
        print("YOU ARE NOT AUTHORIZED")
        return

    for _ in range(img.shape[0] * img.shape[1]):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    print("Decrypted message:", message)

if __name__ == "__main__":
    image_path = input("Enter the encrypted image path: ")
    password = input("Enter the passcode: ")
    decrypt(image_path, password)
