import numpy as np
import matplotlib.pyplot as plt

def tanh():
	x = np.linspace(-10, 10)
	y = np.tanh(x)

	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.scatter(x, y)

	y_dif = np.diff(y)
	ax = fig.add_subplot(1,2,2)
	ax.scatter(x[1:], y_dif)
	plt.show()
	pass

def sigmoid():
	x = np.linspace(-10, 10)
	y = 1 / ( 1 + np.exp(-x + 1e-12))
	
	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.scatter(x, y)

	y_dif = np.diff(y)
	ax = fig.add_subplot(1,2,2)
	ax.scatter(x[1:], y_dif)
	plt.show()
	pass

def ReLU():
	x = np.linspace(-10, 10)
	y = np.maximum(x, 0, x)
	
	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.scatter(x, y)

	y_dif = np.diff(y)
	ax = fig.add_subplot(1,2,2)
	ax.scatter(x[1:], y_dif)
	plt.show()
	pass

def Leakly_ReLU():
	x = np.linspace(-10, 10)
	y = np.where(x > 0, x, x * 0.01)
	
	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.scatter(x, y)

	y_dif = np.diff(y)
	ax = fig.add_subplot(1,2,2)
	ax.scatter(x[1:], y_dif)
	plt.show()
	pass

def ELU():
	x = np.linspace(-10, 10)
	apha = 1
	y = np.where(x < 0, apha * (np.exp(x) - 1), x)
	
	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.scatter(x, y)

	y_dif = np.diff(y)
	ax = fig.add_subplot(1,2,2)
	ax.scatter(x[1:], y_dif)
	plt.show()
	pass
