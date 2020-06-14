import matplotlib.pyplot as plt
import numpy as np

# setting the axes 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# squaring
x = np.linspace(0,10,100)
y = x**2

# graph the parabola in red
plt.plot(x,y, 'r')

# square root
y = np.linspace(0,10,100)
x = x**0.5

# graph square root in blue
plt.plot(x,y,'b')

# show plot
plt.show()

