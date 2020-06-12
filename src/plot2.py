import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# the functions
y1 = x-7
y2 = (36*x)**0.5

# setting the axes 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# plot the function
plt.plot(x,y1, 'r')
plt.plot(x,y2, 'b')

# show the plot
plt.show()

