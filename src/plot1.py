import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# the function, which is y = x^2 here
y = x**2 + 2*x - 1

# setting the axes at the centre

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()

