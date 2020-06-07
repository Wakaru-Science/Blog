import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#style.use("fivethirtyeight")

fig = plt.figure(dpi=80)

ax = plt.subplot2grid((2,2), (0,0), rowspan=2, colspan=2)
ax = plt.subplot2grid((2,2), (0,0), rowspan=2, colspan=2)

#ax2.scatter([1,2,3],[1,2,3])


x_pos = [0, 0, 1, 1, 2, 2]
y_pos = [0, 0, 2, 2, 5, 5]
x_direct = [1, 0, 1, 0, 2, 0]
y_direct = [0, 2, 0, 3, 0, 5]

x2_pos = [0, 1, 2]
y2_pos = [0, 2, 5]
x2_direct = [1, 1, 2]
y2_direct = [2, 3, 5]

ax.quiver(x_pos,y_pos,x_direct,y_direct,
         scale=1, scale_units="xy", angles="xy", alpha=0.3)

ax.quiver(x2_pos,y2_pos,x2_direct,y2_direct,
         scale=1, scale_units="xy", angles="xy")


#ax.arrow(3.5, 3, 1, 0, head_width=0.05, head_length=0.1, color="k", alpha=0.5)

ax.axis([-1, 5, -1, 11])

plt.grid()

#ax.text(1,2.85,"i + i + i")
#ax.text(6.5,2.85,"3i")

ax.yaxis.set_ticks_position("right")

#Bring spine down
#ax.spines["right"].set_position(("data",5))

ax.spines["top"].set_bounds(0,4)
ax.spines["bottom"].set_bounds(0,4)
ax.spines["left"].set_bounds(0,10)
ax.spines["right"].set_bounds(0,10)

#ax2.get_yaxis().set_visible(False)
#ax2.spines["left"].set_visible(False)
#ax2.set_yticks([])

ax.set_xticks(range(0,5))
ax.set_yticks(range(0,11))

plt.show()