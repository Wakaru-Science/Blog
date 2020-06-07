import matplotlib.pyplot as plt, mpld3
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

soa = np.array([[0, 0, 0, 1, 2, 0], [0, 0, 0, 1, 3, 0]])
soa2 = np.array([[0, 0, 0, 2, 5, 0], [0, 0, 0, 1, 6, 1], [0, 0, 0, 1, 6, -1]])

X, Y, Z, U, V, W = zip(*soa)
X2, Y2, Z2, U2, V2, W2 = zip(*soa2)

print(X, Y, Z, U, V, W)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.quiver(X, Y, Z, U, V, W, length=2, #scale_units="xy", angles="xy",
          arrow_length_ratio=0.1)

ax.quiver(X2, Y2, Z2, U2, V2, W2, length=1, #scale_units="xy", angles="xy",
          arrow_length_ratio=0.1, alpha=0.5, color="k")

ax.set_xlim([-7, 7])
ax.set_ylim([-7, 7])
ax.set_zlim([-7, 7])
 
#ax.yaxis.set_ticks_position("left")

mpld3.show()

filename = 'Addition_3D.html'
#mpld3.save_html(fig, filename, template_type='simple')




