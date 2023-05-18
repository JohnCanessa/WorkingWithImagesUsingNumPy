# **** Open folder using VS Code:
#      cd C:\Documents\_Image Processing\scikit-image-building-image-processing-applications\02\demos
#      Run: 
#      python WorkingWithImagesUsingNumPy.py ****

# **** imports ****
import skimage                          # skimage is a collection of algorithms for image processing
from skimage import data                # skimage.data is a module that contains a collection of test images

# **** display skimage version ****
print(f"skimage version: {skimage.__version__}")

# **** import numpy ****
import numpy as np                      # NumPy is the fundamental package for scientific computing with Python
import matplotlib.pyplot as plt         # matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB

# used by Jupyter notebook (not needed in VSCode)
# %matplotlib inline

# **** sample_image of 300 x 300 random numbers ****
sample_image = np.random.random((300, 300))

# **** dump sample_image ****
print(f"sample_image: {sample_image}")

# **** display shape of sample_image ****
print(f"sample_image.shape: {sample_image.shape}")

# **** plot sample_image ****
plt.imshow( sample_image, 
            cmap='gray',                # to display gray images
            interpolation='nearest')    # to fill in unknown values using nearest neighbor interpolation
plt.title("sample_image - gray")        # set image title
#plt.xticks([])                         # remove x ticks
#plt.yticks([])                         # remove y ticks

# **** plt. show() starts an event loop, looks for all currently active figure objects, 
#      and opens one or more interactive windows that display your figure or figures ****
plt.show()                             # display the plot

# ???? img1.png ????


# **** display sample_image using a different colormap ****
plt.imshow( sample_image,
            cmap='Spectral',            # to display spectral images
            interpolation='nearest')    # to fill in unknown values using nearest neighbor interpolation
plt.title("sample_image - Spectral")    # set image title       
plt.show()                              # display the plot

# ???? img2.png ????


# **** ****
camera = data.camera()                  # load the camera image

# **** display camera image ****
plt.figure(figsize=(8, 6))              # set the figure width and height in inches
plt.imshow( camera,                     # display the camera image
            cmap='gray',                # to display gray images
            interpolation='nearest')    # to fill in unknown values using nearest neighbor interpolation
plt.title("camera - gray")              # set the title
plt.show()                              # display the plot

# ???? img3.png ????


# **** display shape of camera ****
print(f"camera.shape: {camera.shape}")

# **** display contents of camera ****
print(f"camera: {camera}")

# **** display camera type ****
print(f"camera type: {type(camera)}")

# **** display camera size ****
print(f"camera size: {camera.size}")

# **** display camera min, max, and mean ****
print(f"camera min: {camera.min()}")    # min of all pixels
print(f"camera max: {camera.max()}")    # max of all pixels
print(f"camera mean: {camera.mean()}")  # mean (or average) of all pixels


# **** load the tree image ****
tree = skimage.io.imread("./images/pexels-tree.jpg", as_gray=True)

# ***** display tree image ****
plt.imshow( tree,
            cmap='gray',
            interpolation='nearest')    # display the tree image
plt.title("tree - gray")                # set the title
plt.show()                              # display the plot

# ???? img4.png ????


# **** display shape of tree ****
print(f"tree.shape: {tree.shape}")


# **** generate tree_copy ****
tree_copy = tree.copy()

# **** display pixel at specified location ****
print(f"tree_copy[100, 200]: {tree_copy[100, 200]}")

# **** set pixel at specified location ****
tree_copy[100, 200] = 0

# **** display pixel at specified location ****
print(f"tree_copy[100, 200]: {tree_copy[100, 200]}")


# **** use index slicing operations to set first 100 rows to 0 ****
tree_copy[:100] = 0

# **** print the first 101 rows of tree_copy ****
print(f"tree_copy[:101]: {tree_copy[:101]}")

# **** display tree_copy ****
plt.imshow( tree_copy,
            cmap='gray',
            interpolation='nearest')    # display the tree image
plt.title("tree_copy - gray")           # set the title
plt.show()                              # display the plot

# ???? img5.png ????


# **** make a new copy of tree_copy ****
tree_copy = tree.copy()

# **** generate a boolean mask of tree_copy ****
mask = tree_copy < 0.5

# **** print mask ****
print(f"mask: {mask}")


# **** set tree_copy to 255 when mask is true ****
tree_copy[mask] = 255                   # set tree_copy to 255 when mask is true

# **** ****
plt.figure(figsize=(8, 6))              # set the figure width and height in inches

# **** display tree_copy ****
plt.imshow(tree_copy,                   # display the tree image
           cmap='gray',                 # to display gray images
           interpolation='nearest')     # to fill in unknown values using nearest neighbor interpolation
plt.title("tree_copy - mask == 255")    # set the title
plt.show()                              # display the plot

# ???? img6.png ????


# **** make a new copy of tree_copy ****
tree_copy = tree.copy()
mask = tree_copy < 0.5
tree_copy[mask] = 0

# **** display tree_copy ****
plt.imshow( tree_copy,                  # display the tree image
            cmap='gray',                # to display gray images
            interpolation='nearest')    # to fill in unknown values using nearest neighbor interpolation
plt.title("tree_copy - mask == 0")      # set the title
plt.show()                              # display the plot

# ???? img7.png ????


# **** read parrot image ****
parrot = skimage.io.imread("./images/pexels-parrot.jpg")

# **** set figure size ****
plt.figure(figsize=(6, 6))              # set the figure width and height in inches

# **** display parrot ****
plt.imshow( parrot,                     # display the parrot image
            interpolation='nearest')    # to fill in unknown values using nearest neighbor interpolation
plt.title("parrot")                     # set the title
plt.show()                              # display the plot

# ???? img8.png ????


# **** display shape of parrot (width, height, channels) ****
print(f"parrot.shape: {parrot.shape}")

# **** display parrot array (R, G, B) ****
print(f"parrot: {parrot}")


# **** RGB, channel at index 2 is the blue channel,
#      the mask finds those pixels where B < 15 ****
blue_mask = parrot[:, :, 2] < 15

# **** print blue_mask ****
print(f"blue_mask: {blue_mask}")


# **** generate parrot_copy ****
parrot_copy = parrot.copy()

# **** set pixels where blue_mask is true to 255 ****
parrot_copy[blue_mask] = [0, 0, 255]

# **** set plot figure size ****
plt.figure(figsize=(8, 8))              # set the figure width and height in inches

# **** display parrot_copy ****
plt.imshow( parrot_copy)                # display the parrot image
plt.title("parrot_copy - blue_mask")    # set the title
plt.show()                              # display the plot

# ???? img9.png ????


# **** RGB, channel at index 0 is the red channel,
#      the mask finds those pixels where R < 15 ****
red_mask = parrot[:, :, 0] < 15

# **** print red_mask ****
print(f"red_mask: {red_mask}")


# **** generate parrot_copy ****
parrot_copy = parrot.copy()

# **** set pixels where red_mask is true to 255 ****
parrot_copy[red_mask] = [255, 0, 0]

# **** set plot figure size ****
plt.figure(figsize=(8, 8))              # set the figure width and height in inches

# **** display parrot_copy ****
plt.imshow(parrot_copy)                 # display the parrot image
plt.title("parrot_copy - red_mask")     # set the title
plt.show()                              # display the plot

# ???? img10.png ????


# **** zoom on parrot's eye using array slicing operations ****
parrot_zoom = parrot[900:1100, 450:900] # zoom on parrot

# **** display parrot_zoom ****
plt.imshow(parrot_zoom)                 # display the parrot image
plt.title("parrot_zoom")                # set the title
plt.show()                              # display the plot

# ???? img11.png ????


# **** list of images ****
many_trees = np.array([tree.copy(), tree.copy(), tree.copy(), tree.copy()])

# **** display shape of many_trees (batch_size, height, width) ****
print(f"many_trees.shape: {many_trees.shape}")


# **** generate many parrots ****
many_parrots = np.array([parrot.copy(), parrot.copy(), parrot.copy(), parrot.copy()])

# **** display shape of many_parrots (batch_size, height, width, channels) ****
print(f"many_parrots.shape: {many_parrots.shape}")
