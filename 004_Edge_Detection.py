from MNIST import load_data
import numpy as np
from matplotlib import pyplot as plt

train_images, train_labels, test_images, test_labels = load_data()

new_images = []
for i in range(len(train_images[:5])):
	img = train_images[i]
	new_img = np.zeros((30,30))
	for i in range(new_img.shape[0]):
		for j in range(new_img.shape[1]):
			if i > 1 and j > 1:
				if i < img.shape[0] + int((new_img.shape[0] - img.shape[0]) / 2) and j < img.shape[1] + int((new_img.shape[1] - img.shape[1]) / 2):
					new_img[i,j] = img[i - int((new_img.shape[0] - img.shape[0]) / 2), j - int((new_img.shape[1] - img.shape[1]) / 2)]
				else:
					new_img[i,j] = 0
			else:
				new_img[i,j] = 0
	new_images.append(new_img)

Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

fig = plt.figure()
L = len(new_images)
for ind in range(len(new_images)):
	img = new_images[ind]
	new_img = np.zeros((28, 28))
	new_img_list = []
	ax = fig.add_subplot(1, L, ind + 1)
	for i in range(img.shape[0] - 3):
		for j in range(img.shape[1] - 3):
			new_img[i, j] = sum(sum(np.multiply(img[i:i+3, j:j+3], Gx))) / (3 * 3)
	ax.imshow(new_img, cmap=plt.cm.Greys)
plt.show()