import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(dpi=80)

ax = fig.add_subplot(111)

x_pos = [0, 1, 2, 5]

y_pos = [3, 3, 3, 3]

x_direct = [1, 1, 1, 3]

y_direct = [0, 0, 0, 0]

ax.quiver(x_pos,y_pos,x_direct,y_direct,
         scale=1, scale_units='x')

ax.arrow(3.5, 3, 1, 0, head_width=0.05, head_length=0.1, color="k", alpha=0.5)

ax.axis([-1, 9, 2.5, 3.5])

#plt.grid()

ax.text(1,2.85,"i + i + i")
ax.text(6.5,2.85,"3i")

#ax.spines["left"].set_bounds(0,2.5)
#ax.spines["right"].set_bounds(0,3.5)

plt.xticks([],[])
plt.yticks([],[])

plt.show()
