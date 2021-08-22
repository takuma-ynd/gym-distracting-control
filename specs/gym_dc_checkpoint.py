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
            mock_env = gym.make(f'distracting_control:{domain.capitalize()}-{task}-{difficulty}-v1',
                                from_pixels=True, channels_first=False, dynamic=False, fix_distraction=True)
            # NOTE: This saves background, color and camera state into
            # - pickled_state/DistractingBackgroundEnv.pkl
            # - pickled_state/DistractingColorEnv.pkl
            # - pickled_state/DistractingCameraEnv.pkl
            mock_env.reset()
            mock_env.save_state('pickled_state')

            # Load distractions from the pickled state
            env = gym.make(f'distracting_control:{domain.capitalize()}-{task}-{difficulty}-v1',
                           from_pixels=True, channels_first=False, dynamic=False, fix_distraction=True,
                           saved_augmentation='pickled_state')

            n_trials = 5
            episode_length = 10
            for j in range(n_trials):
                obs = env.reset()
                done = False
                counter = 0
                for k in range(episode_length):
                    print(i, j, k)
                    logger.save_image(obs, f"my_figures/{domain}-{task}-{difficulty}/ep{j}-{k}.png")
                    act = env.action_space.sample()
                    obs, reward, done, info = env.step(act)
                    if done:
                        break
