# Steganography-Based Secure Data Hiding
This project implements image steganography to securely hide messages within an image using pixel manipulation. The message is protected with a passcode and can only be retrieved using the correct credentials.

## Problem Statement
With growing concerns over data security, traditional encryption methods may attract unwanted attention. This project provides a covert communication method by embedding secret messages into images, ensuring privacy without raising suspicion.

## Technology Used
   1. Language: Python
   2. Libraries:
        OpenCV (cv2) – Image processing
        NumPy – Data manipulation
   3. Platform: Windows, Linux, macOS
   
## Key Features

1.  Passcode Protection – Ensures only authorized users can decrypt the message.
2.  Minimal Image Distortion – Uses Least Significant Bit (LSB) encoding for seamless data embedding.
3.  Efficient & Lightweight – Works with standard images without significant storage overhead.
4.  End Marker (~) for Extraction – Prevents unnecessary processing.

## Target Users
1. Cybersecurity Enthusiasts – For secure communication.
2. Researchers & Students – Learning steganography techniques.
3. Journalists & Activists – Sending confidential messages discreetly.

## How It Works
### I. Encryption (Hiding a Message)
```
python encrypt.py
```
1. Input an image file, message, and passcode.
2. The script modifies pixel values and saves encryptedImage.png.
   
### II.  Decryption (Extracting the Message)
```
python decrypt.py
```
1. Enter the encrypted image and passcode.
2. If correct, the secret message is revealed; otherwise, access is denied.

### File Descriptions
- **encrypt.py** – Hides a secret message inside an image.
- **decrypt.py** – Extracts the hidden message from the image.
- **encryptedImage.png** – The output image containing the secret message.
- **mypic.jpg** – Sample input image used for testing encryption.

## Example Output
## Encryption:
```
Enter the image path: mypic.jpg  
Enter the secret message: HiddenMessage123  
Enter a passcode: mysecurepass  
Encryption Successful! Encrypted image saved as encryptedImage.png
```
## Decryption:
```
Enter the encrypted image path: encryptedImage.png  
Enter the passcode: mysecurepass  
Decryption Successful! Secret Message: HiddenMessage123
#If the wrong passcode is entered:
YOU ARE NOT AUTHORIZED  
```

## Things to Avoid
1. Using large messages – Ensure the message size doesn’t exceed the image capacity.
2. Wrong passcode during decryption – If forgotten, the message cannot be recovered.
3. Modifying the encrypted image – Any edits to encryptedImage.png may corrupt the hidden message.
4. Using highly compressed images (JPEG) – Lossy compression may alter pixel values, affecting decryption.

## Future Enhancements
- 🚀 Support for More Image Formats (PNG, BMP)
- 🚀 Stronger Encryption (AES + Steganography)
- 🚀 Web/Mobile App Integration for user-friendly access

## Conclusion
This project offers a secure and discreet way to hide sensitive information in images. With passcode authentication and LSB encoding, it enhances covert data transmission while keeping the image visually unchanged.

## License
This project is open-source and available under the MIT License.

## Author
Krithiga U
