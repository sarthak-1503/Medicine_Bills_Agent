from PIL import Image


def resize_bill(image_path: str, output_path: str):
    image = Image.open(image_path)
    max_dimension = 2000
    image.thumbnail((max_dimension, max_dimension))
    image.save(output_path)
    return output_path