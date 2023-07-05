import barcode
from barcode.writer import ImageWriter
from PIL import Image
def generate_barcode(text, barcode_type='code128'):
    # Create a barcode object
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_object = barcode_class(text, writer=ImageWriter())

    # Set the filename for the barcode image
    filename = f'barcode_{text}'

    # Save the barcode image
    barcode_object.save(filename)
    image = Image.open(filename+".png")

    # Crop the image to the desired size
    width, height = image.size
    desired_width = 256
    desired_height = 186
    x = (width - desired_width) // 2
    y = (height - desired_height) // 2
    
    image.thumbnail((desired_width, desired_height), Image.ANTIALIAS)

    # Save the cropped image
    image.save(filename+".png")
    return filename