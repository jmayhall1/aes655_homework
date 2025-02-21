# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

left_side = np.array([[1, 1, 1], [-2, 0, -1], [-1, 0, 1]])

#define right-hand side of equation
right_side = np.array([1, 0, 0])

#solve for x, y, and z
result = np.linalg.inv(left_side).dot(right_side)
print(result)

left_side = np.array([[1, 1, 1], [-2, 0, -1], [-1, 0, 1]])

#define right-hand side of equation
right_side = np.array([2, -2, 0])

#solve for x, y, and z
result = np.linalg.inv(left_side).dot(right_side)
print(result)
