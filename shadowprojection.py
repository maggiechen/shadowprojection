"""
Calculation of p = l - [(d+n dot l)/(n dot (v-l))](v-l), from p.226 of Real-time Rendering 4th edition

Note that the intersect of the plane with the y axis is (0, d/ny) where ny is the y component of the normal n

The geometric intuition for this formula can be found in readme.md
"""

import matplotlib.pyplot as plt
import numpy as np

lx = 1
ly = 5

vx = 2
vy = 4

d = -1
n = [-1, 2.5]
n = np.array(n)
n = n/np.linalg.norm(n)

# Calculation of p
l = np.array([lx, ly])
v = np.array([vx, vy])
vminusl = v - l
d_plus_nl = (-d + np.dot(n, l)) # cause of the miscalculation
n_vminusl = np.dot(n, vminusl)

p = l - (d_plus_nl/n_vminusl) * vminusl

y_plane_intersection = np.array([0, d/n[1]])

def set_up_graph_look():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    major_ticks = np.arange(0, 101, 1)
    minor_ticks = np.arange(0, 101, 1)
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlabel("x", loc="right")
    ax.set_ylabel("y", loc="top", rotation="horizontal")
    return ax

def plot_points(ax):
    plt.plot(
        lx, ly, "ob",   # l
        vx, vy, "ob",   # v
        y_plane_intersection[0], y_plane_intersection[1], "ob",
        p[0], p[1], "or",       # textbook p
    )
    ax.annotate("l", xy=(lx, ly), xytext=(lx + 0.2, ly + 0.2), color="b")
    ax.annotate("v", xy=(vx, vy), xytext=(vx + 0.2, vy + 0.2), color="b")
    ax.annotate("(0, d/ny)", xy=y_plane_intersection, xytext=(y_plane_intersection[0] + 0.2, y_plane_intersection[1] - 0.2), color="b")
    ax.annotate("calculated p with textbook formula", xy=p, xytext=(p[0] + 0.2, p[1] - 0.1), color="r")

def plot_lines(ax):
    # Light to shadow line
    plt.axline((lx, ly), (vx, vy), color="grey", linestyle="--")

    # Plane
    plane_slope = -n[0]/n[1]
    plt.axline(y_plane_intersection, color="k", linestyle="-", slope=plane_slope)
    ax.annotate("plane", xy=(2.5, 0), xytext=(2.5, -0.5))

    # Normal line perpendicular to plane
    plt.axline((lx, ly), color="grey", linestyle="--", slope=-1/plane_slope)

def show_graph(ax):
    plt.plot(8, 6)
    plt.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    plt.axis('scaled')
    plt.show()

subplot = set_up_graph_look()
plot_points(subplot)
plot_lines(subplot)
show_graph(subplot)

