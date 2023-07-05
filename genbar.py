import barcode
from barcode.writer import ImageWriter

def generate_barcode(text, barcode_type='code128'):
    # Create a barcode object
    barcode_class = barcode.get_barcode_class(barcode_type)

    # Disable the text option in the writer
    writer_options = {'text': None}
    barcode_object = barcode_class(text, writer=ImageWriter(), writer_options=writer_options)

    # Set the filename for the barcode image
    filename = f'barcode_{text}'

    # Save the barcode image
    barcode_object.save(filename)
    return filename
