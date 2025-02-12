import cv2

def encrypt(image_path, message, password, output_path="encryptedImage.jpg"):
    img = cv2.imread("Mee.jpg")  # Read the input image
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0
    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    print("Encryption complete. Image saved as", output_path)

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    message = input("Enter the secret message: ")
    password = input("Enter a passcode: ")
    encrypt(image_path, message, password)
