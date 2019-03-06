from MNIST import load_data
import numpy as np
from matplotlib import pyplot as plt
import os
import struct
# 003.01
# 003.02
train_images, train_labels, test_images, test_labels = load_data()
with open('02.bmp', 'wb') as f:
	f.write(train_images[0].tobytes())
# 003.03
out_img = np.zeros((28, 28))
for image in train_images[:10]:
	out_img += image
out_img /= len(train_images[:10])
out_img = np.array(out_img, np.int32)
#plt.axis('off')
#plt.imshow(out_img, cmap=plt.cm.gray)
#plt.show()
print (out_img)

# 003.04
out_lab = np.sum(train_labels[:10]) / len(train_labels[:10])
print (f"{out_lab:.2f}")

# 003.05
img = train_images[0]
print (img.shape)
new_img = np.zeros((32,32))
for i in range(new_img.shape[0]):
	for j in range(new_img.shape[1]):
		if i > 1 and j > 1:
			if i < img.shape[0] + int((new_img.shape[0] - img.shape[0]) / 2) and j < img.shape[1] + int((new_img.shape[1] - img.shape[1]) / 2):
				new_img[i,j] = img[i - int((new_img.shape[0] - img.shape[0]) / 2), j - int((new_img.shape[1] - img.shape[1]) / 2)]
			else:
				new_img[i,j] = 0
		else:
			new_img[i,j] = 0
print (new_img.shape)
#plt.imshow(new_img, cmap=plt.cm.gray)
#plt.show()