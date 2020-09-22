from gym.envs.registration import register

register(
        id='foster-v0',
        entry_point='gym_foster.envs:FosterEnv')
