#Cubic LSF
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

sum_x3 = np.sum(x_vals**3)
sum_y3 = np.sum(y_vals**3)
sum_x2y = np.sum((x_vals**2)*y_vals)
sum_xy2 = np.sum(x_vals*(y_vals**2))

sum_x4 = np.sum(x_vals**4)
sum_y4 = np.sum(y_vals**4)
sum_x3y = np.sum((x_vals**3)*y_vals)
sum_x2y2 = np.sum((x_vals**2)*(y_vals**2))
sum_xy3 = np.sum(x_vals*(y_vals**3))

sum_x5 = np.sum(x_vals**5)
sum_y5 = np.sum(y_vals**5)
sum_x4y = np.sum((x_vals**4)*y_vals)
sum_x3y2 = np.sum((x_vals**3)*(y_vals**2))
sum_x2y3 = np.sum((x_vals**2)*(y_vals**3))
sum_xy4 = np.sum(x_vals*(y_vals**4))

sum_x6 = np.sum(x_vals**6)
sum_y6 = np.sum(y_vals**6)
sum_x5y = np.sum((x_vals**5)*y_vals)
sum_x4y2 = np.sum((x_vals**4)*(y_vals**2))
sum_x3y3 = np.sum((x_vals**3)*(y_vals**3))
sum_x2y4 = np.sum((x_vals**2)*(y_vals**4))
sum_xy5 = np.sum(x_vals*(y_vals**5))

sum_z = np.sum(z_arr)
sum_xz = np.sum(x_vals*z_arr)
sum_yz = np.sum(y_vals*z_arr)
sum_x2z = np.sum((x_vals**2)*z_arr)
sum_xyz = np.sum(x_vals*y_vals*z_arr)
sum_y2z = np.sum((y_vals**2)*z_arr)
sum_x3z = np.sum((x_vals**3)*z_arr)
sum_x2yz = np.sum((x_vals**2)*y_vals*z_arr)
sum_xy2z = np.sum(x_vals*(y_vals**2)*z_arr)
sum_y3z = np.sum((y_vals**3)*z_arr)

A = np.array([
    [sum_n, sum_x, sum_y, sum_x2, sum_xy, sum_y2, sum_x3, sum_x2y, sum_xy2, sum_y3],
    [sum_x, sum_x2, sum_xy, sum_x3, sum_x2y, sum_xy2, sum_x4, sum_x3y, sum_x2y2, sum_xy3],
    [sum_y, sum_xy, sum_y2, sum_x2y, sum_xy2, sum_y3, sum_x3y, sum_x2y2, sum_xy3, sum_y4],
    [sum_x2, sum_x3, sum_x2y, sum_x4, sum_x3y, sum_x2y2, sum_x5, sum_x4y, sum_x3y2, sum_x2y3],
    [sum_xy, sum_x2y, sum_xy2, sum_x3y, sum_x2y2, sum_xy3, sum_x4y, sum_x3y2, sum_x2y3, sum_xy4],
    [sum_y2, sum_xy2, sum_y3, sum_x2y2, sum_xy3, sum_y4, sum_x3y2, sum_x2y3, sum_xy4, sum_y5],
    [sum_x3, sum_x4, sum_x3y, sum_x5, sum_x4y, sum_x3y2, sum_x6, sum_x5y, sum_x4y2, sum_x3y3],
    [sum_x2y, sum_x3y, sum_x2y2, sum_x4y, sum_x3y2, sum_x2y3, sum_x5y, sum_x4y2, sum_x3y3, sum_x2y4],
    [sum_xy2, sum_x2y2, sum_xy3, sum_x3y2, sum_x2y3, sum_xy4, sum_x4y2, sum_x3y3, sum_x2y4, sum_xy5],
    [sum_y3, sum_xy3, sum_y4, sum_x2y3, sum_xy4, sum_y5, sum_x3y3, sum_x2y4, sum_xy5, sum_y6]
])

B = np.array([
    sum_z, sum_xz, sum_yz, sum_x2z, sum_xyz,
    sum_y2z, sum_x3z, sum_x2yz, sum_xy2z, sum_y3z
])

a,b,c,d,e,f,g,h,i,j = np.linalg.solve(A,B)

print(f"{a:.6f} + {b:.6f}x + {c:.6f}y + {d:.6f}x² + {e:.6f}xy + {f:.6f}y² + {g:.6f}x³ + {h:.6f}x²y + {i:.6f}xy² + {j:.6f}y³")
