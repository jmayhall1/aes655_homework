# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

heights = [0, 500, 500]
flux = [0.12, -0.1, 0]

plt.plot(flux, heights)
plt.ylabel(r'Time (hours)')
plt.xlabel(r"$\overline{w'\theta_v'}$ (K)")
plt.show()
