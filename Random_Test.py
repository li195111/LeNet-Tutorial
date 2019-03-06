import math

# Normal Distribution
def Normal_Distribution(x, mean, sigma):
	variance = math.pow(sigma, 2)
	output = (1 / math.sqrt(2 * math.pi * variance)) * math.exp(-(math.pow(x - mean, 2) / (2 * variance)))
	return output

#x = [2, 4, 6, 8, 10]
#mean = math.fsum(x) / len(x)
#x_sqrt = [math.pow(n, 2) for n in x]
#std = math.sqrt(math.fsum(x_sqrt) / len(x_sqrt) - math.pow(mean, 2))
#norm = [Normal_Distribution(n, mean, std) for n in x]

#print (f"X : {x} \nMean : {mean} \nStandar Diviation : {std} \nNormal Distribution : {norm} \n")

import time
def rng():
	c = time.clock()
	c = f"{c:.28f}"[-1:-8:-1]
	c = float(int(c)) * 1e-5
	t = time.time()
	T = c + t
	str_T = str(T).split('.')[1]
	L = len(str_T)
	float_T = int(str_T) / 10 ** L
	return float_T
#rand = []
#for i in range(5):
#	rand.append(rng())
#mean = math.fsum(rand) / len(rand)
#rand_sqrt = [math.pow(n, 2) for n in rand]
#std = math.sqrt(math.fsum(rand_sqrt) / len(rand_sqrt) - math.pow(mean, 2))
#norm = [Normal_Distribution(n, mean, std) for n in rand]
#print (f"X : {rand} \nMean : {mean} \nStandar Diviation : {std} \nNormal Distribution : {norm} \n")

