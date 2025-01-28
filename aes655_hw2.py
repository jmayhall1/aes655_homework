# coding=utf-8
import numpy as np
from prettytable import PrettyTable

'''Question 2'''
index = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
w = np.array([0.5, -0.5, 1, 0.8, 0.9, -0.2, -0.5, 0, -0.9, -0.1])
theta = np.array([295, 293, 295, 298, 292, 294, 292, 289, 293, 299])

w_mean = np.round(np.mean(w), 3)
theta_mean = np.round(np.mean(theta), 3)

w_turb = np.round(np.subtract(w, w_mean), 3)
theta_turb = np.round(np.subtract(theta, theta_mean), 3)

w_turb_squared = np.round(np.power(w_turb, 2), 3)
theta_turb_squared = np.round(np.power(theta_turb, 2), 3)

w_theta = np.round(np.multiply(w, theta), 3)
w_theta_turb = np.round(np.multiply(w_turb, theta_turb), 3)

avg_w_theta = np.round(np.mean(w_theta), 3)
avg_w_theta_reynolds = np.round(np.add(np.multiply(w_mean, theta_mean), np.mean(w_theta_turb)), 3)

t = PrettyTable(['index', 'w', 'θ', "w^'", "θ^'", "(w^')^2", r"(θ^')^2", r"wθ",
                 r"(w^')(θ^')"])
for i, ind in enumerate(index):
    t.add_row([ind, w[i], theta[i], w_turb[i], theta_turb[i], w_turb_squared[i], theta_turb_squared[i], w_theta[i],
               w_theta_turb[i]])
t.add_row(['Average', w_mean, theta_mean, '', '', '', '', '', ''])
t.add_row(['avg(wθ)', avg_w_theta, '', '', '', '', '', '', ''])
t.add_row(["avg(w)avg(θ) + avg((w^')(θ^'))", avg_w_theta, '', '', '', '', '', '', ''])
print(t.get_formatted_string('latex'))
print(t)

'''Question 3'''
w_biased_std = np.round(np.std(w, ddof=0), 3)
theta_biased_std = np.round(np.std(theta, ddof=0), 3)
cc = np.divide(np.mean(w_theta_turb), np.multiply(w_biased_std, theta_biased_std))

print(f'Standard Deviation of w: {w_biased_std} \n Standard Deviation of theta: {theta_biased_std}'
      f'\n Correlation Coefficient: {cc}')
