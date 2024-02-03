import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from .sample_data import big_dipper

def get3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    return fig, ax

def circle(n=100):
    theta = np.linspace(0, 2*np.pi, n)
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros((n,))
    return x, y, z

def inclined_circle(theta, n=100):
    x, y, z = circle(n=100)
    return x, y*np.cos(theta), y*np.sin(theta)
    

def draw_sphere(ax):
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:30j]
    xx = np.cos(u)*np.sin(v)
    yy = np.sin(u)*np.sin(v)
    zz = np.cos(v)
    ax.plot_wireframe(xx, yy, zz, color="gray", alpha=0.2)
    return ax


def ax_settings(ax, radius=1.2):
    ax.set_box_aspect((2, 2, 2))
    ax.set_xlim3d(-radius / 2, radius / 2)
    ax.set_zlim3d(-radius / 2, radius / 2)
    ax.set_ylim3d(-radius / 2, radius / 2)
    #ax.legend()
    return ax


def animate_sun(fig, ax, x_ecl, y_ecl, z_ecl):
    lines, = ax.plot(x_ecl[0], y_ecl[0], z_ecl[0],
                     marker='o', color='orange', markersize=10)
    def init():
        lines.set_xdata(np.array([]))
        lines.set_ydata(np.array([]))
        lines.set_3d_properties(np.array([]))
        return lines,
    def animate(i):
        lines.set_xdata(x_ecl[i])
        lines.set_ydata(y_ecl[i])
        lines.set_3d_properties(z_ecl[i])
        #txt.set_text(dates[i].isoformat().replace('T', ' '))
        return lines,
    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=len(x_ecl),
                         interval=20,
                         blit=False, repeat=True)
    return fig, ax, anim
