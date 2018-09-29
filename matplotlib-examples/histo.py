import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)  # 1 row and 2 columns of plot and i want to select the first plot
x = np.random.normal(0.0, 1.0, 10000) # generate a set of random numbers in a bell shape curve (typically centered arond zero)
plt.hist(x)

plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000) # generates a set of unifrom numbers
plt.hist(x)

plt.show()

plt.hist(x, bins=20) # bins is the number of ranges

plt.show()