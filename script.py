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


# Open the TIFF image
image = Image.open('images/0015.tiff')

# Convert the image to a NumPy array
image_np = np.array(image)

# View the image
#Image.fromarray(image_np).show()
#print(image_np)

i = 0
baseLine_SC1 = []
SC1 = []
baseLine_SC2 = []
SC2 = []
node = baseLine_SC1

while i<8:
    print(node)
    if node == baseLine_SC1:
        node = SC1
    elif node == SC1:
        node = baseLine_SC2
    elif node == baseLine_SC2:
        node = SC2
    elif node == SC2:
        node = baseLine_SC1

    i+=1

def appendNitems(file_dir,pos_of_item,n,list_l):
    for i in range(n):
        list_l.append(file_dir[pos_of_item + i])

    # might have to return pos_of_item  - SA
