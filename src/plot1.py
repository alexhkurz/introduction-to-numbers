import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# the function
y = x**2

# plot the function
plt.scatter(x,y)

# show the plot
plt.show()

