import numpy as np

m1 = np.arange(-3,4)
theta1 = np.arcsin(m1 * 650e-9 / 0.52e-3) / np.pi * 180 * 60

m2 = np.arange(-6,7)
theta2 = np.arcsin(m2 * 650e-9 / 1.5e-3 / 2) / np.pi * 180 * 60

print(theta1)
print(theta2)
