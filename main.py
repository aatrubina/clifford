import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def clifford_attractor(x, y):
	P = [3, 3, 4, 4, -1]
	x = (np.sin(P[0]*y) + P[2]*np.cos(P[0]* x)) * P[4]
	y = (np.sin(P[1]*x) + P[3]*np.cos(P[1]* y)) * (1 - P[4])

	return x, y


def draw_map(steps):
	x_arr, y_arr = [], []
	x_arr.append(-1), y_arr.append(-1)
	for i in range(steps):
		x, y = clifford_attractor(x_arr[-1], y_arr[-1])
		x_arr.append(x)
		y_arr.append(y)

	plt.plot(x_arr, y_arr, '^', color='white', alpha = 0.5, markersize = 0.1)
	plt.axis('on')
	plt.show()
	plt.close()

	return x_arr, y_arr


steps = 100000
draw_map(steps)
