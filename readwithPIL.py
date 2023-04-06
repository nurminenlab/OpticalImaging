
# using PIL

from PIL import Image
import numpy as np

# Open the TIFF image
image = Image.open('images/0015.tiff')

# Convert the image to a NumPy array
image_np = np.array(image)

# View the image
Image.fromarray(image_np).show()
print(image_np)

# using OpenCV

'''import cv2
import numpy as np

# Read the TIFF image
image = cv2.imread('images/0016.tiff', cv2.IMREAD_UNCHANGED)

# Convert the image to a NumPy array
image_np = np.array(image)

# View the image
cv2.imshow('image', image_np)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

# using tifffile

'''import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt

# Read the TIFF image
image = tiff.imread('images/0016.tiff')

# Convert the image to a NumPy array
image_np = np.array(image)

# View the image
tiff.imshow(image_np)
plt.show()
print(image_np)'''

# using imageIO library

'''import  imageio
import numpy as np

# Read the TIFF image
image = imageio.v2.imread('images/0016.tiff')

# Convert the image to a NumPy array
image_np = np.array(image)

# View the image
imageio.imshow(image_np)'''