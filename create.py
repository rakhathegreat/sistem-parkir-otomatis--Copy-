import uuid
import qrcode

def generate_random_id():
    # Generate a random UUID
    random_id = uuid.uuid4()
    return str(random_id)

# Generate a random ID
random_id = generate_random_id()
print("Random ID:", random_id)

def generate_qr_code(text, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1-40, 1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border (default is 4)
    )
    
    # Add data to the QR code
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(filename)

# Example usage
filename = "qrcode.png"
generate_qr_code(random_id, filename)
print(f"QR code saved as {filename}")
