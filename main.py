import random
import numpy as np

grid_size = 5  # 5x5 grid world, (0, 0) to (4, 4)
q_table = np.zeros((grid_size, grid_size, 4))
# creates q table initialized with zeros

visited = set()
actions = ["up", "down", "left", "right"]
# action to indices:  0 = up, 1 = down, 2 = left, 3 = right

def step(state, action):
    x, y = state # cur position into x row and y col
    if action == 0: x = max(0, x-1)
    if action == 1: x = min(grid_size-1, x+1)
    if action == 2: y = max (0, y-1)
    if action == 3 : y = min(grid_size-1, y+1)

    return (x, y)

goal = (2, 2)

def get_reward(state):
    reward = -0.1

    if state == goal:
        reward +=10

    if state not in visited:
        reward += 0.5  # curiosity bonus
        visited.add(state)

    return reward



