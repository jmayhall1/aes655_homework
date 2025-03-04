# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

times = [0]
thetas = [280.0]
start = 0.01
while start <= 60 * 60 * 30:
    times.append(start / (60 * 60))
    theta = 2 * np.log(500 + 0.01 * start) + 267.57
    thetas.append(theta)
    start += 0.01

plt.plot(times, thetas)
plt.xlabel(r'Time (hours)')
plt.ylabel(r'$\overline{\theta_v}$ (K)')
plt.show()
