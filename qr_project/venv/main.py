import qrcode  # Import the QR code library

def generate_qr_code(url, filename="qrcode.png"):
    """
    Generate a QR code from a URL and save it as an image file.
    
    Parameters:
    - url (str): The URL to encode in the QR code
    - filename (str): Name of the output image file (default: "qrcode.png")
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1-40, higher means bigger)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes (4 is minimum recommended)
    )
    
    # Add the URL data to the QR code
    qr.add_data(url)
    
    # Generate the QR code
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)
    
    print(f"QR code generated successfully! Saved as {filename}")

# Example usage
if __name__ == "__main__":
    # Get URL input from user
    url = input("Enter the URL you want to convert to QR code: ")
    
    # Get filename input (optional)
    filename = input("Enter output filename (default is qrcode.png): ") or "qrcode.png"
    
    # Generate the QR code
    generate_qr_code(url, filename)