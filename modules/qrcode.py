import qrcode
import PIL
import io

def image_to_binary(image):
    # Create a BytesIO object
    img_byte_arr = io.BytesIO()
    
    # Save the image to the BytesIO object in the desired format
    image.save(img_byte_arr, format='PNG')  # You can change 'PNG' to another format if needed
    
    # Get the binary data
    img_byte_arr = img_byte_arr
    
    return img_byte_arr

def generate_qr_code(url: str, output_file="qrcode.png") -> PIL.Image.Image:
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code, 1 is for a small size
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in the QR code grid
        border=4,  # thickness of the border
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    # img.save(output_file)

    print(f"QR code generated and saved as {output_file}")
    return img.get_image() 


