# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 02:28:51 2020

@author: Hang Yu
"""

import numpy as np


class Stacking:
    
    def __init__(self):
        
        self.state = np.array([-1,-1,-1,-1,-1])
        self.state_flag = np.array([1 for i in range(len(self.state))])
        self.top = -1
        self.is_done = False
        self.best_score = 4*5 + 3*4 + 2*3 + 1*2 + 0*1 - 5
        self.action_space = len(self.state) + 1
        
    def reset(self):
        self.state = np.array([-1,-1,-1,-1,-1])
        self.state_flag = np.array([1 for i in range(len(self.state))])
        self.is_done = False
        self.top = -1
        self.best_score = 35
        return self.state.copy()
    
    def sample(self):
        
        return np.random.choice(self.action_space)
        
    def step(self,action):
        
        if self.is_done == True:
            return self.state.copy(), 0, self.is_done
            
        if action > 5 or action < 0:
            print("Invalid action!")
            return self.state.copy(), 0, self.is_done
        
        if action <= 4:
            if self.state_flag[action] == 1:
                self.state_flag[action] = -1
                self.top += 1
                self.state[self.top] = action
                if self.top == 4:
                    self.is_done = True
                return self.state.copy(), (self.top + 1) * action - 1, self.is_done
            else:
                return self.state.copy(), -1, self.is_done
        if action == 5:
            if self.state[0] == -1:
                return self.state.copy() , -1, self.is_done
            else:
                temp_action = self.state[self.top]
                self.state[self.top] = -1
                self.state_flag[temp_action] = 1
                self.top -= 1
                return self.state.copy(), -1*((temp_action) * (self.top + 2)) -1, self.is_done

    def sum_reward(self,state):
        sum_reward = 0
        for i in range(len(state)):
            if state[i] != -1:
                sum_reward += (i+1)*state[i]
        return sum_reward
    
    def sum_expect(self,state):
        sum_reward = 0
        state_flag =[1 for i in range(len(state))]
        for i in range(len(state)):
            if state[i] != -1:
                state_flag[state[i]] = -1 
                sum_reward += (i+1)*state[i]
        for i in range(len(state) -1, -1, -1):
            if state[i] == -1:
                for j in range(len(state) -1, -1, -1):
                    if state_flag[j] == 1:
                        state_flag[j] = -1
                        sum_reward += (i+1)*j
        return sum_reward
    
    def perfect_action(self, state):
        if self.top == len(state) -1:
            return None
        for i in range(self.top+1):
            if self.state[i] != i:
                #return 5
                if self.sum_expect(self.state) < self.best_score - 2 * (self.top - i + 1 ):
                    return 5
                else:
                    cnt = len(self.state) - self.top -1 
                    for j in range(len(self.state_flag) - 1, -1 , -1):
                        if self.state_flag[j] == 1:
                            cnt -= 1
                            if cnt == 0:
                                return j
                    
        return self.top + 1
    def demonstration():
        pass
    def elvaluation():
        pass
    def flag():
        pass
    def estimation(self, state):
        return self.sum_expect(state)
        

    
        
        
        

