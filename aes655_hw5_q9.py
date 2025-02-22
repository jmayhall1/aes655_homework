# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

line = np.poly1d(np.polyfit([3.7, 5, 5.8, 6.5, 7.4, 8, 9, 9.5, 10],
                            np.log([1, 4, 10, 20, 50, 100, 300, 500, 1000]), deg=1))
point1_x = np.divide(np.log(2) - line[0], line[1])
print(f'2m wind: {point1_x}')
point2_x = np.divide(np.log(0.1) - line[0], line[1])
print(f'0.1m wind: {point2_x}')
zero_point_y = np.exp(line(0))
print(f'0m/s wind height: {zero_point_y}')
new_x = [0, point2_x, 3.7, point1_x, 5, 5.8, 6.5, 7.4, 8, 9, 9.5, 10, 10]
new_y = [zero_point_y, 0.1, 1, 2, 4, 10, 20, 50, 100, 300, 500, 1000, 2000]

x = [3.7, 5, 5.8, 6.5, 7.4, 8, 9, 9.5, 10, 10]
y = [1, 4, 10, 20, 50, 100, 300, 500, 1000, 2000]

plt.semilogy(new_x, new_y, label='Extended Data', c='orange')
plt.semilogy(x, y, label='Provided Data', c='blue')
plt.legend()
plt.xlabel(r'$\overline{M}$ ($\frac{m}{s}$)')
plt.xticks(np.arange(0, 10.1, 0.5))
plt.ylabel('z (m)')
plt.show()