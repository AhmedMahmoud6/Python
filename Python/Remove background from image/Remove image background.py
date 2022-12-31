from rembg import remove
from PIL import Image

input_path = input('enter photo name: ')
h = input_path
n = h.find('.')
output = h[:n]
output_path = f'{output}.png'

inputt = Image.open(input_path)
output = remove(inputt)
output.save(output_path)
print('Done!')