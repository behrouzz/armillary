import numpy as np
import armillary as pc
import matplotlib.pyplot as plt


x_equ, y_equ, z_equ = pc.circle(n=100)
x_ecl, y_ecl, z_ecl = pc.inclined_circle(theta=np.radians(23), n=100)


fig, ax = pc.get3d()

ax.plot(x_equ, y_equ, z_equ)
ax.plot(x_ecl, y_ecl, z_ecl)

ax.plot((0,0),(0,0), (-1,1), '-k', label='z-axis')

ax = pc.draw_sphere(ax)

ax.quiver(0, 0, 0, 0, 0, 1, color='r') # CIP vector
ax.quiver(0, 0, 0, 1, 0, 0, color='g') # Equinox vector

ax.scatter([0], [0], [0], color="k", s=100) # Earth

# put some stars
stars = pc.big_dipper()
ax.scatter(stars[:,0], stars[:,1], stars[:,2], c='k', s=5)

ax = pc.ax_settings(ax)
plt.axis('off')
plt.grid(False)
plt.show()
