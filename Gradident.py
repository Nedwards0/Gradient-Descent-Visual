import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter


def f(x, y): # Function to run gradient descent on
    return (1 - x)**2 + 100 * (y - x**2)**2

def grad_f(x, y): # Gradient of the function
    dfdx = -2 * (1 - x) - 400 * x * (y - x**2)
    dfdy = 200 * (y - x**2)
    return np.array([dfdx, dfdy])

lr = 0.001
x, y = -1.5, 1.5  # starting point
points = [(x, y, f(x, y))]

for _ in range(2000):
    grad = grad_f(x, y)
    if np.linalg.norm(grad) < 1e-3:
        break
    x -= lr * grad[0]
    y -= lr * grad[1]
    points.append((x, y, f(x, y)))

points = np.array(points)

X = np.linspace(-2, 2, 400)
Y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap=cm.inferno, alpha=0.7, edgecolor='none')
line, = ax.plot([], [], [], 'cyan', lw=2, label='Descent Path')
dot, = ax.plot([], [], [], 'ro', markersize=5)

ax.set_title('Gradient Descent on Rosenbrock Function', fontsize=14)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.view_init(elev=45, azim=135)

# Animation setup
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    dot.set_data([], [])
    dot.set_3d_properties([])
    return line, dot

def animate(i):
    line.set_data(points[:i+1, 0], points[:i+1, 1])
    line.set_3d_properties(points[:i+1, 2])
    dot.set_data(points[i, 0:1], points[i, 1:2])
    dot.set_3d_properties(points[i, 2:3])
    return line, dot

anim = FuncAnimation(fig, animate, init_func=init, frames=len(points), interval=30, blit=True)
writer = PillowWriter(fps=60)
anim.save("gradient_descent.gif", writer=writer, dpi=100)
