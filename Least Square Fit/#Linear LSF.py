#Linear LSF
#Num Lab 
#9 October

import numpy as np
x_ = np.linspace(-2,2,50)
y_ = np.linspace(-2,2,50)
# Create a 2D grid so that x and y vary independently
X, Y = np.meshgrid(x_, y_)

def f(x,y):
	return x**2 + np.sin(x+y)

x_vals = X.flatten()
y_vals = Y.flatten()
z_arr = f(x_vals, y_vals)

sum_n = len(x_vals)
sum_x = np.sum(x_vals)
sum_y = np.sum(y_vals)
sum_x2 = np.sum(x_vals**2)
sum_y2 = np.sum(y_vals**2)
sum_xy = np.sum(x_vals*y_vals)

sum_z = np.sum(z_arr)
sum_xz = np.sum(x_vals*z_arr)
sum_yz = np.sum(y_vals*z_arr)

A = np.array([[sum_n,sum_x,sum_y],
			   [sum_x,sum_x2,sum_xy],
			   [sum_y,sum_xy,sum_y2]])
B = np.array([sum_z,sum_xz,sum_yz])
a,b,c = np.linalg.solve(A,B)
print(f"{a} + {b}x + {c}y")