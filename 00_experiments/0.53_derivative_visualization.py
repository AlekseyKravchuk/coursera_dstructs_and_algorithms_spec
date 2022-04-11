import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(np.power(x, 2))


x = np.linspace(1.5, 4, 200)
y = f(x)

x0 = 3.5
dx = 0.001  # dx approaches zero
derivative = (f(x0 + dx) - f(x0)) / dx  # difference quotient
tangent = f(x0) + derivative * (x - x0)  # finding the tangent line

plt.figure(figsize=(10, 6))

plt.ylim(-2, 2)
plt.xlim(1.5, 4)

plt.plot(x, y, linewidth=4, color='g', label='Function')
plt.plot(x, tangent, color='m', linestyle='--', linewidth='3', label='Tangent Line')
plt.plot(x0, f(x0), 'o', color='r', markersize=10, label='Example Point')

plt.legend(fontsize=12)
plt.grid(True)
plt.show()

