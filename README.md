# Gradient Descent Visualizer

A minimal, from-scratch implementation of **gradient descent** with
3D visualization of the optimization trajectory using matplotlib.

## Overview
- Implements batch gradient descent without ML frameworks
- Manually derived gradients (no autograd)
- Visualizes convergence on the **Rosenbrock function**, a classic
  non-convex optimization benchmark
- Outputs an animated GIF showing the descent path

## How to Run
Modify the objective function and its gradient in the code, then run:

```bash
python Gradident.py
```