from PIL import Image
import numpy as np
import random

def pixely_effect(n, input_path, output_path):
    input_image = Image.open(input_path).convert('RGB')
    input_pixels = np.array(input_image)

    height, width, _ = input_pixels.shape
    output_image = Image.new('RGB', (width, height))

    for y in range(0, height - n, n):
        for x in range(0, width - n, n):
            rand_x = random.randint(x, x + n - 1)
            rand_y = random.randint(y, y + n - 1)
            pixel = tuple(input_pixels[rand_y, rand_x])
            for i in range(n):
                for j in range(n):
                    if x + i < width and y + j < height:
                        output_image.putpixel((x + i, y + j), pixel)

    output_image.save(output_path)
    #output_image.show()

if __name__ == "__main__":
    for i in range(0, 10, 1):
        output_filename = f'output{i}.png'
        pixely_effect(4, 'input.png', output_filename)


