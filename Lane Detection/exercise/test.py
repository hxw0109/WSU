import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
np.set_printoptions(threshold=np.nan)
x = np.asarray([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# print ((x > 4) & (x < 8))

# image = mpimg.imread('test.jpg')
# gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# plt.imshow(gray)
# plt.show()
# b = np.stack(x)
# print(np.dstack(b))

a = np.asarray([1,2,3,4])
b = np.asarray([4,5,6,7])
c=np.where(abs(a-np.mean(a))<np.std(a))
a = np.asarray([])
print(a)