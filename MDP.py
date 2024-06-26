import numpy as np
import gym

# Create the FrozenLake environment
env = gym.make('FrozenLake-v1', is_slippery=True)

# Initialize the Q-table with zeros
num_states = env.observation_space.n
num_actions = env.action_space.n
Q = np.zeros(num_states, num_actions)

# Hyperparameters
learning_rate = 0.1
discount_factor = 0.99
exploration_prob = 0.1
num_episodes = 1000

# Q-learning algorithm
for episode in range(num_episodes):
    state = env.reset()
    done = False
    
    while not done:
        if np.random.uniform(0, 1) < exploration_prob:
            action = env.action_space.sample()  # Exploration
        else:
            action = np.argmax(Q[state, :])  # Exploitation
        
        next_state, reward, done, _ = env.step(action)
        
        # Q-value update
        Q[state, action] = (1 - learning_rate) * Q[state, action] + \
                          learning_rate * (reward + discount_factor * np.max(Q[next_state, :]))
        
        state = next_state

# Extract the optimal policy
optimal_policy = np.argmax(Q, axis=1)

# Print the optimal policy
print("Optimal Policy:")
print(optimal_policy.reshape(4, 4))
