import main
import random
import numpy as np
alpha = 0.1
gamma = 0.9
epsilon = 0.2

def print_grid(agent_pos):
    for i in range(main.grid_size):
        row = ""
        for j in range(main.grid_size):
            if (i, j) == agent_pos:
                row += "A "
            elif (i, j) == main.goal:
                row += "G "
            else:
                row += ". "
        print(row)
    print("\n")


for episode in range(20):
    state = (random.randint(0,4), random.randint(0,4))
    main.visited.clear()

    for step_count in range(20):
        if random.random() < epsilon:
            action = random.randint(0,3)

        else:
            action = np.argmax(main.q_table[state])

        next_state = main.step(state, action)
        reward = main.get_reward(next_state)

        main.q_table[state][action] += alpha * (reward + gamma * np.max(main.q_table[next_state]) - main.q_table[state][action])

        print(f"Episode {episode}, Step {step_count}: {state} -> {next_state}, Reward: {reward}")

        print_grid(next_state)

        state = next_state

        if state == main.goal:
            print(f"Reached goal in episode {episode}!")
            break


