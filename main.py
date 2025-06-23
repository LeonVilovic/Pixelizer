# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from PIL import Image

if __name__ == "__main__":

    from PIL import Image
    import numpy as np
    import random

    image_path = r'input.png'
    input_image = Image.open(image_path).convert('RGB')  # Convert to RGB
    # input_image.show()

    # Convert to NumPy array for easy pixel access
    input_pixels = np.array(input_image)

    height, width, _ = input_pixels.shape
    output_size = (width, height)
    output_image = Image.new('RGB', output_size)

    # adjust n for more or less pixely effect
    n = 5

    for y in range(0, height - n, n):
        for x in range(0, width - n, n):
            rand_x = random.randint(x, x + n)
            rand_y = random.randint(y, y + n)
            pixel = tuple(input_pixels[rand_y, rand_x])
            for i in range(0, n, 1):
                for j in range(0, n, 1):
                    output_image.putpixel((x + i, y + j), pixel)

    output_image.save('output.png')
    output_image.show()
