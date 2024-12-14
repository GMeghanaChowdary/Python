from PIL import Image
def image_compression():
    img = Image.open("image.jpg")
    img = img.resize((int(img.width / 2), int(img.height / 2)))
    img.save("compressed_image.jpg")
image_compression()
