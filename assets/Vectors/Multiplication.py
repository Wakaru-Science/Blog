import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(dpi=80)

ax = fig.add_subplot(111)

x_pos = [2, 1, 4,
         0, 3,
         0.4, 2.4, 4.4,
         0, 2, 4,
         1.5, 0]
y_pos = [3.5, 3, 3,
         2, 2,
         0, 0, 0,
         1, 1, 1,
         -0.5,1.5]
x_direct = [2, 1, 1,
            2.9, 2.9,
            1, 1, 1,
            1.9, 1.9, 1.9,
            3,6]
y_direct = [0, 0, 0,
            0, 0,
            0, 0, 0,
            0, 0, 0,
            0,0]

#x1 , y1 = [1,2, 3.4], [1,2,4.3]
#x2 , y2 = [3,4,0.7], [3,4,2.8]

plt.plot([0.4, 0], [0, 1], color="k", alpha=0.4)
plt.plot([1.35, 1.85], [0, 1], color="k", alpha=0.4)

plt.plot([2.4, 2], [0, 1], color="k", alpha=0.4)
plt.plot([3.35, 3.85], [0, 1], color="k", alpha=0.4)

plt.plot([4.4, 4], [0, 1], color="k", alpha=0.4)
plt.plot([5.35, 5.85], [0, 1], color="k", alpha=0.4)

plt.plot([1, 0], [3, 2], color="k", alpha=0.4)
plt.plot([1.9, 2.85], [3, 2], color="k", alpha=0.4)

plt.plot([4, 3], [3, 2], color="k", alpha=0.4)
plt.plot([4.9, 5.80], [3, 2], color="k", alpha=0.4)


ax.arrow(7, -0.5, 0, 1.9, head_width=0.2, head_length=0.1, color="k", alpha=0.6)
ax.arrow(7, 3.5, 0, -1.9, head_width=0.2, head_length=0.1, color="k", alpha=0.6)

ax.arrow(2, -0.5, -0.4, 0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)
ax.arrow(2.9, -0.5, 0.0, 0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)
ax.arrow(3.8, -0.5, +0.4, 0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)

ax.arrow(1, 1, 0, 0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)
ax.arrow(3, 1, 0, 0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)
ax.arrow(5, 1, 0, 0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)

ax.arrow(1.5, 2, 0, -0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)
ax.arrow(4.5, 2, 0, -0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)

ax.arrow(2.7, 3.5, -0.5, -0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)
ax.arrow(3.2, 3.5, 0.5, -0.3, head_width=0.2, head_length=0.1, color="k", alpha=0.4)


ax.text(2.9,-0.75,"3i")
ax.text(2.9,3.75,"2i")

ax.text(0.30,0.5,"i+i = 2i")
ax.text(2.3,0.5,"i+i = 2i")
ax.text(4.3,0.5,"i+i = 2i")

ax.text(0.65,2.3,"i+i+i = 3i")
ax.text(3.65,2.3,"i+i+i = 3i")

ax.text(6.25,1.45,"6i")

ax.text(7.25,0.5,"3i . 2i = 6i")
ax.text(7.25,2.5,"2i . 3i = 6i")


ax.quiver(x_pos,y_pos,x_direct,y_direct,
         scale=1, scale_units='x')

ax.axis([-1.5, 10, -1, 4])

ax.set_xticks([])
ax.set_yticks([])

#plt.grid(which="both")
#ax.set_xticks(range(-1,11))
#ax.set_yticks(range(5))
            
plt.show()

