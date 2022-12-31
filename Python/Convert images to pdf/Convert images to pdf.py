from PIL import Image

image_1 = Image.open(r'C:\Users\Administrator\Desktop\assignment\1.jpg')
image_2 = Image.open(r'C:\Users\Administrator\Desktop\assignment\2.jpg')
image_3 = Image.open(r'C:\Users\Administrator\Desktop\assignment\3.jpg')


im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')
im_3 = image_3.convert('RGB')


image_list = [im_2, im_3]

im_1.save(r'C:\Users\Administrator\Desktop\assignment\Assignments.pdf', save_all=True, append_images=image_list)
