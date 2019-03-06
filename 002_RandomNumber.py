import numpy as np

def num_random(times=5, start=-1., end=1.):
	"""Return Numbers of Random Number between start and the end."""
	if not type(times) == int:
		raise TypeError("Arg 'times' Must be an integer.")
	if not type(start) == int and not type(start) == float:
		raise TypeError("Arg 'start' Must be a float.")
	if not type(end) == int and not type(end) == float:
		raise TypeError("Arg 'end' Must be a float.")

	return_list = []
	for _ in range(times):
		rand = np.random.uniform(start, end)
		return_list.append(rand)
	return return_list

# 002.01 Output 5 random number
output = num_random()
print (output)
# [-0.8165308868169985, 0.9372893663387438, 0.9143531682093351, 0.15994881195214306, 0.29655615720207384]

# 002.02 Output N random number and Calculate mean and std, N = 10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5.
for i in range(5):
	Times = 10 ** (i + 1)
	rand_list = num_random(times= Times)
	rand_mean = np.mean(rand_list)
	rand_std = np.std(rand_list)
	print (f"Times : {Times} \nMean : {rand_mean} \nSTD : {rand_std} \n")
# Times : 10
# Mean : 0.10389574483744268
# STD : 0.48807284417079877

# Times : 100
# Mean : 0.006353133490108609
# STD : 0.5622399616300663

# Times : 1000
# Mean : 0.04710809669893721
# STD : 0.5631682602203573

# Times : 10000
# Mean : 0.00580156056258176
# STD : 0.5797379365775756

# Times : 100000
# Mean : 0.00306643584223072
# STD : 0.5779806696520989

# 002.03 Output 002.02 Cost time
import time
for i in range(5):
	t_s = time.time()
	Times = 10 ** (i + 1)
	rand_list = num_random(times= Times)
	rand_mean = np.mean(rand_list)
	rand_std = np.std(rand_list)
	t_e = time.time()
	print (f"Times : {Times} \nMean : {rand_mean} \nSTD : {rand_std} \nCost Time : {t_e - t_s:.3f} sec\n")
# Times : 10
# Mean : -0.14672920936813866
# STD : 0.5374220717796387
# Cost Time : 0.000 sec

# Times : 100
# Mean : 0.08192662108456508
# STD : 0.6043749356565722
# Cost Time : 0.000 sec

# Times : 1000
# Mean : -0.002138163715946476
# STD : 0.5739466048247391
# Cost Time : 0.000 sec

# Times : 10000
# Mean : 0.0015183603441834624
# STD : 0.573696824174778
# Cost Time : 0.030 sec

# Times : 100000
# Mean : -0.0032911434031311507
# STD : 0.5794667665749833
# Cost Time : 0.300 sec

# 002.04 Random Number Generator
def RandomGenerator(number:int, start_num:float= -1., end_num:float= 1., integer:bool= False):
	"""Generate number of random number in specific range."""
	t_s = time.time()
	output_list = num_random(times= number, start= start_num, end= end_num)
	if integer:
		output_list = list(np.array(output_list, dtype= np.int32))
	output_mean = np.mean(output_list)
	output_std = np.std(output_list)
	t_e = time.time()
	cost_time = t_e - t_s
	return output_list, output_mean, output_std, cost_time

out = RandomGenerator(5, -1, 1, integer= False)
print (out[0][:], out[1], out[2], out[3])
# [-0.8433948310668289] 0.003122947412084298 0.576550644681882 0.032500505447387695

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

def RNG(number:int, integer:bool= False):
	t_s = time.time()
	output_list = []
	for i in range(number):
		output_list.append(rng())
	if integer:
		output_list = list(np.array(output_list, dtype= np.int32))
	output_mean = np.mean(output_list)
	output_std = np.std(output_list)
	t_e = time.time()
	cost_time = t_e - t_s
	return output_list, output_mean, output_std, cost_time
out = RNG(5, False)
print (out[0][:], out[1], out[2], out[3])