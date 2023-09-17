import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# export QT_QPA_PLATFORM=wayland

def sinplot(n=10, flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.plot(x, np.sin(x + i * .5) * (n + 2 - i) * flip)


sinplot()
