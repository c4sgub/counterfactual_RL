import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
    
class FosterEnv(gym.Env):
    metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.n_service = 0
        ## Sample age of the youth
        age_p = [0.05699999999999994,0.08,0.08,0.08,0.07,0.06,0.06,0.05,0.05,0.06,0.07,0.08,0.09,0.08,0.03,0.003]
        age = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        age_sample = np.random.multinomial(1,age_p,1)
        self.age = age[np.where(age_sample == 1)[1][0]]
        ## Sample race of the youth
        self.race = ['major','minor'][np.random.binomial(1,0.3,1)[0]]
        self.status = 'in'
        self.casegoal = 'Empty'
        self.reward = 0 
        ## Sample reunificaiton rate for the youth. The race could potentially
        ## influence the distirbution of reunification rate. 
#         self.reunification_rate =  0.5
        if self.race == 'major':
            self.reunification_rate =  0.5
        else:
            self.reunification_rate = 0.3
        ## TODO: Sample more features using generative model. 
    def step(self,action):
        if action == 'a_LTFC':
            self.casegoal = 'LTFC'
            self.age +=1 
            reward = 0.1
            if self.age == 19:
                self.status = 'out'
            else:
                self.status = 'in'
        else:
            self.casegoal = 'R'
            self.age +=1 
            reunion = np.random.binomial(1,self.reunification_rate,1)[0]
            if reunion == 1: 
                self.status = 'out'
                reward = 1
            else:
                if self.age == 19:
                    self.status = 'out'
                    reward = 0
                else:
                    self.status = 'in'
                    reward = 0 
        return [self.casegoal,self.age,self.race,reward,self.status]
            
    def reset(self):
        self.n_service = 0
        age_p = [0.05699999999999994,0.08,0.08,0.08,0.07,0.06,0.06,0.05,0.05,0.06,0.07,0.08,0.09,0.08,0.03,0.003]
        age = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        age_sample = np.random.multinomial(1,age_p,1)
        self.age = age[np.where(age_sample == 1)[1][0]]
        self.race = ['major','minor'][np.random.binomial(1,0.3,1)[0]]
        self.status = 'in'
        self.casegoal = 'Empty'
        self.reward = 0
        if self.race == 'major':
            self.reunification_rate =  0.5
        else:
            self.reunification_rate = 0.3

    def render(self,mode='human',close=False):
        print('The status of the youth is: {}'.format(self.status))
        print('The age of the youth is: {}'.format(self.age))
        print('The race of the youth is: {}'.format(self.race))
        print('The casegoal of the youth is: {}'.format(self.casegoal))
        print('Current reward is: {}'.format(self.reward))
