
# parameter -> images per stimulus 

# make how many preceding images to use for normalization, parametrized

# normalize stimulus 1 images with the average of preceding baseline
# take average of stimulus 1 images and assigning into a bucket

# normalize stimulus 2 images with the average of preceding baseline
# take average of stimulus 2 images and assigning into a bucket

# an average of the stimulus repetitions in a bucket

# subtract 

import os
import time
import keyboard
from PIL import Image
import time
from ordered_set import OrderedSet
import numpy as np
import matplotlib.pyplot as plt


def imageFiles_to_npArray(image_files): # array of img files to np array values
    image_files_array = []
    for file in image_files: #loop over tiff files

        file_path = os.path.join("images", file)    
        #image = Image.open(file_path)
        image = np.array(Image.open(file_path))
        image_files_array.append(image)    

    image_files_npArray = np.array(image_files_array)

    return image_files_npArray

def normalize(baselineMean, SC_npArray):

    eps = 0.000000001
    normArray = SC_npArray/(baselineMean+eps)
    
    return normArray

def subt_normalize(baselineMean, SC_npArray):

    normArray = SC_npArray - baselineMean
    
    return normArray


existing_files = set()
images_folder = []
baseLine_SC1_images = [] 
SC1_images = []          
baseLine_SC2_images = [] 
SC2_images = []          

SC1_bin = []
SC2_bin = []
pointer1 = 1
pointer2 = 1

plt.ion()
fig1, ax1 = plt.subplots(1,2)
fig1.suptitle('SC1 bin mean')
# iterate over the folder to monitor the newly created files
while True:
    files = os.listdir('images')
    tiff_files = [file for file in files if file.endswith('.tiff')]
    
    # save only new file
    new_files = list(set(tiff_files) - existing_files)    
    parameter = 3 # change other 3's to parameter

    # print only new file
    for tiff_file in new_files:
        print(f"New file created: {tiff_file}")
        
        images_folder.append(tiff_file)
        for i, num in enumerate(images_folder):   
            if i % (parameter*4) < parameter:         # if i % 12 < 3
                baseLine_SC1_images.append(num)
                baseLine_SC1_images = list(OrderedSet(baseLine_SC1_images))         

            elif i % (parameter*4) < parameter*2 :     #i % 12 < 6:
                SC1_images.append(num)
                SC1_images = list(OrderedSet(SC1_images))
                  

            elif i % (parameter*4) < parameter*3 :     #i % 12 < 9
                baseLine_SC2_images.append(num)
                baseLine_SC2_images = list(OrderedSet(baseLine_SC2_images))

            else:
                SC2_images.append(num)
                SC2_images = list(OrderedSet(SC2_images))
        
        if len(SC1_images)  == parameter*pointer1 : # every 3 images - calculate mean of baseline , normalize , overall mean , push to SC1 bin
            #print(baseLine_SC1_images[-3:])    
            #print(SC1_images[-3:])

            baseline1_Mean = np.mean(imageFiles_to_npArray(baseLine_SC1_images[-3:]),axis=0)

            SC1_npArray = imageFiles_to_npArray(SC1_images[-3:])
            #normalize and overAll mean
            BaseLn_SC1_mean = np.mean(normalize(baseline1_Mean,SC1_npArray),axis=0)
            
            SC1_bin.append(baseline1_Mean)


            # calculate the mean of the bin here
            SC1_bin_mean = np.mean(np.array(SC1_bin),axis=0)
            ax1[0].cla()
            ax1[0].imshow(SC1_bin_mean)

            # plot the image here
            
                  
            pointer1 = pointer1 +1

        
        if len(SC2_images)  == parameter*pointer2 : 
            #print(baseLine_SC2_images[-3:])
            #print(SC2_images[-3:])
    
            baseline2_Mean = np.mean(imageFiles_to_npArray(baseLine_SC2_images[-3:]),axis=0)

            SC2_npArray = imageFiles_to_npArray(SC2_images[-3:])
            #normalize and overAll mean
            BaseLn_SC2_mean = np.mean(normalize(baseline2_Mean,SC2_npArray),axis=0)
            
            SC2_bin.append(baseline2_Mean)


            # calculate the mean of the bin here
            # plot the image here     
            pointer2 = pointer2 +1 
            

    # old files update
    existing_files.update(tiff_files)
    if keyboard.is_pressed('x'):
        print("Exiting loop.")
        print(baseLine_SC1_images ,"\n",SC1_images,"\n" ,baseLine_SC2_images,"\n" ,SC2_images )
        print(np.array(SC1_bin).shape,np.array(SC2_bin).shape)
        break
    
