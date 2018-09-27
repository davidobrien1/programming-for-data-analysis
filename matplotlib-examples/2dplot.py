import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01) # Numpy will give me a range of number between 0 and 10 to 2 places of decimals
y = 3.0 * x + 1.0 # x and y are arrays
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.', label="Actual")  # "b." means blue dot in matplotlib
plt.plot(x, y, 'b-', label="Model") # this plots another line to the plot

plt.title("Simple Plot")
plt.xlabel("Weigth")
plt.ylabel("Mass")
plt.legend()


plt.show()

