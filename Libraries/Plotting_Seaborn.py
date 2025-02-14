import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# def sinplot(n=10, flip=1):
n = 10
flip = 1
x = np.linspace(0, 20, 100)
for i in range(1, n + 1):
    plt.plot(x, np.sin(x + i * 0.5) * (n + 2 - i) * flip)
plt.show()

# sinplot()


sinplot()
