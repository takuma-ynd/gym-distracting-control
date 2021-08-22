"""A simple demo that produces an image from the environment."""
import gym
import os
from ml_logger import logger
import numpy as np

import distracting_control.suite as suite

if __name__ == '__main__':
    for i, difficulty in enumerate(['easy', 'medium', 'hard']):
        for domain, task in [
            ('ball_in_cup', 'catch'),
            # ('cartpole', 'swingup'),
            # ('cheetah', 'run'),
            # ('finger', 'spin'),
            # ('reacher', 'easy'),
            # ('walker', 'walk')
        ]:
            mock_env = gym.make(f'distracting_control:{domain.capitalize()}-{task}-{difficulty}-v1', from_pixels=True, channels_first=False, dynamic=False, fix_augmentation=True)
            mock_env.save_state('pickled_state')
            env = gym.make(f'distracting_control:{domain.capitalize()}-{task}-{difficulty}-v1', from_pixels=True, channels_first=False, dynamic=False, fix_augmentation=True, load_from='pickled_state')

            n_trials = 5
            for j in range(n_trials):
                obs = env.reset()
                done = False
                counter = 0
                for k in range(20):
                    print(i, j, k)
                    logger.save_image(obs, f"my_figures/{domain}-{task}-{difficulty}/{j}/{k}.png")
                    act = env.action_space.sample()
                    obs, reward, done, info = env.step(act)
                    if done:
                        break
