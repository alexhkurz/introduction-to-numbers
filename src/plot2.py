import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# the functions
y1 = x-7
y2 = 6*x**0.5

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# plot the function
plt.plot(x,y1, 'r')
plt.plot(x,y2, 'r')

# show the plot
plt.show()

