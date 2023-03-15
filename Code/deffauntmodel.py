import numpy as np
import matplotlib.pyplot as plt

# Define the model parameters
n = 100  # Number of agents
m = 10  # Number of interactions per step
eps = 0.1  # Confidence bound
t_max = 1000  # Number of simulation steps
mew = 0.4 #adjustment rate

# Initialize the opinions of the agents randomly
opinions = np.random.rand(n)

# Simulate the model
for t in range(t_max):
    # Randomly select pairs of agents to interact
    pairs = np.random.choice(n, (m, 2), replace=False)
    for i, j in pairs:
        # Check if the difference in opinions is within the confidence bound
        if abs(opinions[i] - opinions[j]) <= eps:
            # Update the opinions of the agents
            new_op_i = opinions[i] - mew*(opinions[i] - opinions[j])
            new_op_j = opinions[j] + mew*(opinions[i] - opinions[j])
            opinions[i] = new_op_i
            opinions[j] = new_op_j

# Plot the final opinion distribution
plt.hist(opinions, bins=20)
plt.title("Opinion Distribution")
plt.xlabel("Opinion")
plt.ylabel("Frequency")
plt.show()