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

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def appendNitems(file_dir,pos_of_item,n,list_l):
    for i in range(n):
        list_l.append(file_dir[pos_of_item + i])

    # might have to return pos_of_item  - SA

def normalizeImages(imagesArray):
    normalized_image_arrays = []
    for image in imagesArray:       
        normalized_image = (image-np.min(image))/(np.max(image)-np.min(image))
        normalized_image_arrays.append(normalized_image)  
    
    fig, ax = plt.subplots()
    ax.imshow(normalized_image_arrays[5], cmap='gray')
    ax.set_title("Normalized Image")
    ax.axis('off')
    plt.show()

baseline1_image_numbers = [0,1,2]
stimulus1_image_numbers = [3,4,5]
baseline2_image_numbers = [6,7,8]
stimulus2_image_numbers = [9,10,11]



folder_path = "images"

all_files = os.listdir(folder_path)

image_files = [file for file in all_files if file.lower().endswith('.tiff')]

norm_image_Array =[]
# Iterate over the tiff img files
for file in image_files:
    # Construct the full file path
    file_path = os.path.join(folder_path, file)
    
    # Open the TIFF image using PIL
    image = Image.open(file_path)
    image = np.array(image)
    print(image.dtype)
    # normalize here

    norm_image_Array.append(image)

normalizeImages(norm_image_Array)

# parameter -> images per stimulus 

# make how many preceding images to use for normalization, parametrized

# normalize stimulus 1 images with the average of preceding baseline
# take average of stimulus 1 images and assigning into a bucket

# normalize stimulus 2 images with the average of preceding baseline
# take average of stimulus 2 images and assigning into a bucket

# an average of the stimulus repetitions in a bucket

# subtract 


i = 0
baseLine_SC1 = []
SC1 = []
baseLine_SC2 = []
SC2 = []
node = baseLine_SC1

while i<8:
    #print(node)
    if node == baseLine_SC1:
        node = SC1
    elif node == SC1:
        node = baseLine_SC2
    elif node == baseLine_SC2:
        node = SC2
    elif node == SC2:
        node = baseLine_SC1

    i+=1

