import random
import gym
print(gym.__version__)

env = gym.make("CartPole-v1", render_mode="human")

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        action = random.choice([0, 1])
        #obs, reward, done, info, thing = env.step(action)
        obs, reward, done, info = env.step(action)
        score += reward
        env.render()
    
    print(f"Episode {episode}, score: {score}")

env.close()