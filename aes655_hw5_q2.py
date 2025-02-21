# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

line = np.poly1d(np.polyfit([1, 2, 3], np.log([1, 10, 100]), deg=1))
new_point = np.exp(line(0))
print(new_point)
x = [1, 2, 3, 3, 3, 3]
y = [1, 10, 100, 200, 500, 1000]

new_x = [0, 1, 2, 3, 3, 3, 3]
new_y = [new_point, 1, 10, 100, 200, 500, 1000]

plt.semilogy(new_x, new_y, label='Extended Data', c='orange')
plt.semilogy(x, y, label='Provided Data', c='blue')
plt.legend()
plt.xlabel(r'$\overline{M}$ ($\frac{m}{s}$)')
plt.ylabel('z (m)')
plt.show()