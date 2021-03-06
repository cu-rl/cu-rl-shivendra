import gym
env = gym.make('FrozenLake-v0')

# Exploring the discrete spaces of this env
print(env.action_space)
print(env.observation_space)

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            env.render()
            break
env.close()
