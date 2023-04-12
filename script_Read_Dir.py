import os
import time
import keyboard
from ordered_set import OrderedSet

existing_files = set()
images_folder = []
baseLine_SC1 = [] #a
SC1 = []          #b
baseLine_SC2 = [] #c
SC2 = []          #d

# iterate over the folder to monitor the newly created files
while True:
    files = os.listdir('images')
    tiff_files = [file for file in files if file.endswith('.tiff')]
    
    # save only new file
    new_files = list(set(tiff_files) - existing_files)    


    # print only new file
    for tiff_file in new_files:
        print(f"New file created: {tiff_file}")
        images_folder.append(tiff_file)
        for i, num in enumerate(images_folder):   
            if i % 12 < 3:
                baseLine_SC1.append(num)
                baseLine_SC1 = list(OrderedSet(baseLine_SC1))

            elif i % 12 < 6:
                SC1.append(num)
                SC1 = list(OrderedSet(SC1))

            elif i % 12 < 9:
                baseLine_SC2.append(num)
                baseLine_SC2 = list(OrderedSet(baseLine_SC2))

            else:
                SC2.append(num)
                SC2 = list(OrderedSet(SC2))

    # old files update
    existing_files.update(tiff_files)

    if keyboard.is_pressed('x'):
        print("Exiting loop.")
        print(baseLine_SC1 ,SC1 ,baseLine_SC2 ,SC2 )
        break
    
    time.sleep(0.2)