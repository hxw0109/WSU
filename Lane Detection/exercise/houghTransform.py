import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
# Read in and grayscale the image
image = mpimg.imread('solidYellowLeft.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# 1. Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size),0)

# Define our parameters for Canny and apply
low_threshold = 60
high_threshold = 180
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Next we'll create a masked edges image using cv2.fillPoly()
mask = np.zeros_like(edges)
ignore_mask_color = 255
# This time we are defining a four sided polygon to mask
imshape = image.shape
print(imshape[0])
# vertices = np.array([[(0,imshape[0]),(imshape[1]/2-10, imshape[0]/2), (imshape[1]/2+10, imshape[0]/2), (imshape[1],imshape[0])]], dtype=np.int32)
vertices = np.array([[(0,imshape[0]),(430,340), (530,340), (imshape[1],imshape[0])]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)


# Define the Hough transform parameters
# Make a blank the same size as our image to draw on

rho = 2
theta = np.pi/180
threshold = 30
min_line_length = 10
max_line_gap = 10
line_image = np.copy(image)*0 #creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

print(lines)
# Iterate over the output "lines" and draw lines on the blank

for line in lines:
	for x1,y1,x2,y2 in line:
		cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),2)


# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges,edges,edges))


# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges,0.8,line_image,1,0)

# Display the image
plt.imshow(combo)
# plt.imshow(lines)
plt.show()