from matplotlib import pyplot as plt

plt.rcParams.update({'font.size': 22})


# install pillow using:
# pip3 install pillow
# if above does not work and you are on windows, try:-
# py -m pip3 install pillow

# importing Image and ImageOps from PIL
from PIL import Image, ImageOps

# creating image object:
imInp = Image.open('C:\\Users\\hp\Desktop\\b22144_assignment8\\b22144_assignment8\problem3cInput.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
import numpy as np
pixels2D = np.array(imGrayscale)
print(pixels2D.shape)


# showing/saving image
imGrayscale.show()
#imGrayscale.save('problem3cOutput.jpg')

# Write code for finding histogram here:
fig, ax = plt.subplots(1,1)
ax.hist(pixels2D.flatten(), bins = 1000)
ax.set_xlabel('Gray Scale Value')
ax.set_ylabel('No. of Pixels')
plt.savefig('C:\\Users\\hp\\Desktop\\b22144_assignment8\\b22144_assignment8\\problem2ci.png')

# Write code for finding histogram of difference of pixel's intensity
# with its left neighbour here:

rows = 662
cols = 960
diffpixels = []
pixels2D=pixels2D.astype('int32')

for row in range (rows):
    diff_row = []
    for col in range (1, cols):
        diff = (pixels2D[row][col] - pixels2D[row][col - 1])
        diff_row.append(diff)
    diffpixels.append(diff_row)

diff_pixels = np.array(diffpixels)



fig, ax = plt.subplots(1,1)
ax.hist(diff_pixels.flatten(), bins = 1000)
ax.set_xlabel('Diffrence of Gray Scale Values')
ax.set_ylabel('No. of Pixels')
plt.savefig('C:\\Users\\hp\\Desktop\\b22144_assignment8\\b22144_assignment8\\problem2cii.png')


