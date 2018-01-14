# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:04:09 2018
Viterbi Algorithm
@author: Kanchana
"""

import numpy as np

def viterbi(T_mat, O_mat, observations):
    ''' Implements the Viterbi Algorithm. Uses logarithmic probability to ease 
    calculations. Assumes a HMM is already existing. 
    
    Takes as input:
        1) T_mat: transition matrix of HMM (numpy array)
        2) O_mat: observation matrix of HMM (numpy array)
        3) observations: the sequence of observations (list / numpy array)
    
    Outputs:
        1) best_path: the best sequence of states for given observation (array)
           (same length as observations) 
        2) best_prob: the probability of the output sequence (float)
    
    '''
    
    #initialize values and arrays
    num_obs = len(observations)
    num_states = T_mat.shape[0]
    log_probs = np.zeros(num_states) #change for non-zero initial path cost
    paths = np.zeros((num_states,num_obs))
    
    #iterating through each index for each observation
    for obs_index, obs_value in enumerate(observations):
        for state_index in range(num_states):
            #Using the equation for the next state probability given current 
            #state probability and next observation (using log probabilities)
            #P(i,n) = P(i-1,m)*T(m,n)*O(x,i)
            temp_log_probs = log_probs + \
                             np.log(O_mat[state_index, int(obs_value)]) + \
                             np.log(T_mat[:, state_index])
            best_path_index = np.argmax(temp_log_probs)
            
            #update the paths array
            paths[state_index, :] = paths[best_path_index, :]
            paths[state_index, obs_index] = state_index
            
            #update probability array
            log_probs[state_index] = temp_log_probs[best_path_index]
    
    #find index of the best path at last stage
    best_path_index = np.argmax(log_probs)
    best_path = paths[best_path_index]
    best_prob = np.exp(log_probs[best_path_index])
    
    return (best_path, best_prob)


# testing script
def test(seed=100):
    ''' function for testing Viterbi() function above '''
    np.random.seed(100)
    # the transition matrix
    T_mat = np.array([[.2, .3, .5], [.3, .4, .3, ], [.4, .4, .2]])
    # the observation matrix
    O_mat = np.array([[.5, .4, .1], [.7, .1, .2, ], [.3, .2, .4]])
    
    # creating random observation
    observations1 = np.random.random(20)
    observations1[observations1>0.67] = 2
    observations1[observations1<=0.33] = 0
    observations1[np.logical_and(observations1>0.33, observations1<=0.67)] = 1
    
    # create observation pattern
    observations2 = [0, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 2, 0, \
                     1, 1, 2, 1, 1, 1, 1]
    
    # testing
    path1, log_prob1 = viterbi(T_mat, O_mat, observations1)
    print ("For random observation: " + str(observations1))
    print ("The best path is" + str(path1))
    print ('')
    
    path2, log_prob2 = viterbi(T_mat, O_mat, observations2)
    print ("For given sequence: " + str(observations2))
    print ("The best path is" + str(path2))
    
    return ([path1, log_prob1],[path2, log_prob2])
    
if __name__ == '__main__':
    a,b = test()