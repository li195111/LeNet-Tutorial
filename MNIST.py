import os
import struct
import numpy as np

def idx3(path):
	f = open(path, 'rb')
	data = f.read()
	f.close()
	offset = 0
	format_header = ">iiii"
	magic_num, images_num, rows_num, cols_num = struct.unpack_from(format_header, data, offset= offset)
	images_size = rows_num * cols_num
	offset += struct.calcsize(format_header)
	fmt_img = ">" + str(images_size) + "B"
	images = np.empty((images_num, rows_num, cols_num))
	for i in range(images_num):
		image = np.array(struct.unpack_from(fmt_img, data, offset)).reshape((rows_num, cols_num))
		images[i] = image
		offset += struct.calcsize(fmt_img)
		pass
	
	return images

def idx1(path):
	f = open(path, 'rb')
	data = f.read()
	f.close()
	offset = 0
	format_header = ">ii"
	magic_num, images_num = struct.unpack_from(format_header, data, offset= offset)
	offset += struct.calcsize(format_header)
	fmt_img = ">B"
	labels = np.empty((images_num,))
	for i in range(images_num):
		labels[i] = struct.unpack_from(fmt_img, data, offset)[0]
		offset += struct.calcsize(fmt_img)
		pass
	return labels


def load_data():
	cur_dir = os.getcwd()
	mnist_dir = os.path.join(cur_dir, "MNIST")
	datas_list = os.listdir(mnist_dir)
	datas_path = [os.path.join(mnist_dir, data) for data in datas_list]
	for path in datas_path:
		data_name = path.split("\\")[-1].split("-")[0]
		data_type = path.split('.')[-1]
		if 'idx1' in data_type:
			if data_name == "t10k":
				test_labels = idx1(path)
				pass
			else:
				train_labels = idx1(path)
				pass
			pass
		if 'idx3' in data_type:
			if data_name == "t10k":
				test_images = idx3(path)
				pass
			else:
				train_images = idx3(path)
				pass
			pass
		pass
	return train_images, train_labels, test_images, test_labels

#imgs_10k, labs_10k, imgs, labs = load_data()

#fig = plt.figure()
#num = 5
#for i, img in enumerate(imgs_10k[:num]):
#	rimg = cv2.resize(img, (28, 28))
#	ax = fig.add_subplot(3, num, i + 1)
#	plt.axis('off')
#	plt.imshow(rimg, cmap=plt.cm.gray)
#Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
#Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

#def Conv(img, kernel):
#	cimg = img.copy()
#	for r in range(img.shape[0] - kernel.shape[0]):
#		for c in range(img.shape[1] - kernel.shape[1]):
#			cimg[r:r + kernel.shape[0],c:c + kernel.shape[1]] = signal.convolve2d(img[r:r + kernel.shape[0],c:c + kernel.shape[1]], kernel, mode= "same")
#	return cimg

#for i, img in enumerate(imgs_10k[:num]):
#	rimg = cv2.resize(img, (30 + i, 30 + i))
#	cximg = Conv(img, Gx)
#	cximg = cv2.resize(cximg, (28, 28))
#	ax = fig.add_subplot(3, num, num + i + 1)
#	plt.axis('off')
#	plt.imshow(cximg, cmap=plt.cm.gray)
#	cyimg = Conv(img, Gy)
#	cyimg = cv2.resize(cyimg, (28, 28))
#	ax = fig.add_subplot(3, num, num + num + i + 1)
#	plt.axis('off')
#	plt.imshow(cyimg, cmap=plt.cm.gray)

#plt.show()
