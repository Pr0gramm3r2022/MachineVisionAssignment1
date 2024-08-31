import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import imageio

DIR = "Rose-Quantization-Prototype"

#RoseImage = imageio.v3.imread(os.path.join(DIR, "rose.jpg"))
Rose_img = Image.open("rose.jpg")
pixels = Rose_img.load()
#Rose_img.show()
num_imgs = 9
plt.imshow(Rose_img,cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
'''plt.imshow(Rose_img,cmap = 'gray', vmin = 0, vmax = 127)
plt.show()'''

'''plt.imshow(Rose_img,cmap = 'gray', vmin = 0, vmax = 127)
plt.show()'''
plt.imshow(Rose_img,cmap = 'gray', vmin = 0, vmax = 63)
plt.show()


#take vmax to n - 1
#Step 1: need to convert the image into a numpy array.

#Rose_array = np.array([imageio.v3.imread(os.path.join(DIR, f"rose.jpg")) for i in range(num_imgs)])
Rose_array = np.array("rose.jpg")
pixels_array = np.array(pixels)
print(Rose_array) #why is this printing the file name and not numbers
print("this is the pixels array" + str(pixels_array))
print(pixels_array.shape)

ImageArray = np.asarray(Rose_img)
#Type casted the array to a tuple
#newRoseArray = (tuple(ImageArray))
print(type(ImageArray)) #image array is an ndarray
#print(ImageArray.size()) neeed to get size of the imaage array

#print(newRoseArray)
#print(newRoseArray.size())
print(ImageArray.ndim) #2D Array
print(ImageArray.size) #size is 108576
print('Shape of Image Array' + str(ImageArray.shape)) #shape is 1024x1024 right now

#output image needs to be hsve 0 values for row and columns
#OutputImage = np.array()
#plt.show(OutputImage)
#will return to this.
#change the array to unsigned integer data type
#UnsignedArray = np.array([0,0,0], dtype.uint8)
#array is not unsigned
ImageArray.astype('uint8')
print(ImageArray.dtype)

#attepted to scale the array down using the asscalar function
#ScalarArray = np.asscalar(ImageArray)
'''np.reshape( ImageArray, (256, 256))

plt.show(ImageArray)

np.reshape(ImageArray(128, 128))'''

print(ImageArray[0:1024])

new_height = 256
new_width = 256

# Original Image Dimensions
original_height = ImageArray.shape, original_width = ImageArray.shape[:2]

# new array for the resized image
ResizedArray = np.zeros((new_height, new_width, ImageArray.shape), dtype=ImageArray.dtype)

#The scalars for height and width
height_scale = original_height / new_height
width_scale = original_width / new_width

# For loops to populate the array
for i in range(new_height):
    for j in range(new_width):
        # scaling original pixel sizes to the new sizes
        orig_i = int(i * height_scale)
        orig_j = int(j * width_scale)

        # Assigning pixel values
        ResizedArray[i, j] = ImageArray[orig_i, orig_j]

# show the resized image
plt.imshow(ResizedArray, cmap='gray', vmin=0, vmax=255)
plt.show()

# Print the resized array information
print("Resized image array shape ", ResizedArray.shape)

p[p]