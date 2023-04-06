'''import numpy as np
from PIL import Image
   
from tifffile import imread

# List of paths to the TIFF files
tiff_paths = ['path/to/file1.tif', 'path/to/file2.tif', ..., 'path/to/file10.tif']

# Load the TIFF files as NumPy arrays and stack them along the first axis
images = np.stack([imread(path) for path in tiff_paths], axis=0)

# Compute the average of the pixel values in the array along the first axis
average = np.mean(images, axis=0)

print("Average:", average)'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# parameter -> images per stimulus 


baseline1_image_numbers = [0,1,2]
stimulus1_image_numbers = [3,4,5]
baseline2_image_numbers = [6,7,8]
stimulus2_image_numbers = [9,10,11]

# make how many preceding images to use for normalization, parametrized

# normalize stimulus 1 images with the average of preceding baseline
# take average of stimulus 1 images and assigning into a bucket



# normalize stimulus 2 images with the average of preceding baseline
# take average of stimulus 2 images and assigning into a bucket



# an average of the stimulus repetitions in a bucket

# subtract 


# Open the TIFF image file
tiff_img = Image.open("images/0016.tiff")

# Get information about the image
print("Image format:", tiff_img.format)
print("Image size:", tiff_img.size)
print("Image mode:", tiff_img.mode)

# Show the image
#tiff_img.show()

# Access the pixel values of the image
pixel_values = list(tiff_img.getdata())
ar_values = np.array(pixel_values, 'uint16')
I = np.reshape(ar_values,(tiff_img.size[1],tiff_img.size[0]))
plt.figure()
plt.imshow(I)
plt.show()
print(ar_values)

#print("Pixel values:", ar_values)