import numpy as np
import matplotlib.pyplot as plt


def f(x): return np.sin(np.power(x, 2))


x = np.linspace(1.5, 4, 200)
y = f(x)

a = 3
h = 0.001  # h approaches zero
derivative = (f(a + h) - f(a)) / h  # difference quotient
tangent = f(a) + derivative * (x - a)  # finding the tangent line

plt.figure(figsize=(10, 6))

plt.ylim(-2, 2)
plt.xlim(1.5, 4)

plt.plot(x, y, linewidth=4, color='g', label='Function')
plt.plot(x, tangent, color='m', linestyle='--', linewidth='3', label='Tangent Line')
plt.plot(a, f(a), 'o', color='r', markersize=10, label='Example Point')

plt.legend(fontsize=12)
plt.grid(True)
plt.show()
