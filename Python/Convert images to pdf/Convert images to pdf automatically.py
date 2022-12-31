import os
from PIL import Image

folder_path = input(r"enter folder location: ")
folder_files = os.listdir(folder_path)
pdf_name = input("Enter pdf file name")
images = []
for file in folder_files:
    image_path = os.path.join(folder_path, file)
    print(image_path)
    image = Image.open(image_path)
    converted_image = image.convert("RGB")
    images.append(converted_image)

first_image = images[0]
del images[0]
first_image.save(fr'{folder_path}\{pdf_name}.pdf', save_all=True, append_images=images)
