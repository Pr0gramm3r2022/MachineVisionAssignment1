import os
from PIL import Image
import numpy as np

import imageio

DIR = "Rose-Quantization-Prototype"

#RoseImage = imageio.v3.imread(os.path.join(DIR, "rose.jpg"))
Rose_img = Image.open("rose.jpg")
pixels = Rose_img.load()
#Rose_img.show()
num_imgs = 9

#Step 1: need to convert the image into a numpy array.

#Rose_array = np.array([imageio.v3.imread(os.path.join(DIR, f"rose.jpg")) for i in range(num_imgs)])
Rose_array = np.array("rose.jpg")
pixels_array = np.array(pixels)
print(Rose_array) #why is this printing the file name and not numbers
print("this is the pixels array" + str(pixels_array))
print(pixels_array.shape)