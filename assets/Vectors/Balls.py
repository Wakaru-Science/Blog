import numpy as np
import matplotlib.pyplot as plt

#fig, ax = plt.subplots()

fig = plt.figure(dpi=80)

ax = fig.add_subplot(111)

x_pos = [0, 1, 3, 2.65]
y_pos = [0, 0, 0, 0]
x_direct = [1, 1, 2, 0.35]
y_direct = [0, 0, 0, 0]

ax.quiver(x_pos,y_pos,x_direct,y_direct,
         scale=1, scale_units='x')

circle_1 = plt.Circle((0.85, 0.25), 0.10, color="k")
circle_2 = plt.Circle((1.15, 0.25), 0.10, color="k")
circle_3 = plt.Circle((3.05, 0.25), 0.10, color="k")
circle_4 = plt.Circle((2.75, 0.25), 0.10, color="k")


ax.add_artist(circle_1)
ax.add_artist(circle_2)
ax.add_artist(circle_3)
ax.add_artist(circle_4)

ax.text(0.55,0.75, "Before", fontsize=13)
ax.text(2.65,0.75, "After", fontsize=13)

ax.text(0.25,-0.65, "Ball 1\n10 m/s")
ax.text(1.25,-0.65, "Ball 2\n10 m/s")
ax.text(2.55,-0.65, "Ball 1\n0 m/s")
ax.text(3.25,-0.65, "Ball 2\n20 m/s")

#Bring spine down
ax.spines["top"].set_position(("data",1.5))
#Cut the spines
ax.spines["left"].set_bounds(-1,1.5)
ax.spines["right"].set_bounds(-1,1.5)

#Remove axis
#plt.axis("off")

#Remove ticks
plt.xticks([],[])
plt.yticks([],[])

#Change axis and circle will become wierd
ax.axis([-0.5, 5.5, -1, 4])

plt.show()
