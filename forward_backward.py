# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 08:30:54 2018
Forward-Backward Algorithm
@author: Kanchana
"""

import numpy as np

def forward_backward(T_mat, O_mat, observations):
    ''' Implements the Forward Backward Algorithm for HMMs. Uses logarithmic 
    probability to ease calculations. Assumes a HMM model is already existing. 
    
    Takes as input:
        1) T_mat: transition matrix of HMM (numpy array)
        2) O_mat: observation matrix of HMM (numpy array)
        3) observations: the sequence of observations (list / numpy array)
    
    Outputs:
        1) prob_mat: contains all P(Z_k | X_1:k)
           size - (number of states * number of observations)
        2) forward_mat: contains all P(Z_k, X_1:k)
           size - (number of states * number of observations)
        3) backward_mat: contains all P(X_k+1:n | Z_k)
           size - (number of states * number of observations)
    '''
    
    #initialize values and arrays
    seq_len = len(observations)
    num_states,num_obs   = O_mat.shape
    forward = np.zeros( (num_states, seq_len + 1) ) #P(Z_k, X_1:k)
    backward = np.zeros( (num_states, seq_len + 1) ) #P(X_k+1:n | Z_k)
    
    # forward algorithm
    # P(z_k, x_1:k) = sumOver( P(x_k|z_k) * P(z_k|z_k-1) * P(z_k-1,X_1:k-1) )
    forward[:, 0] = 1.0/num_states
    for seq_index in range(seq_len):
        f_row = np.matrix(forward[:,seq_index])
        forward[:, seq_index+1] = f_row * np.matrix(T_mat) * \
                                  np.matrix(np.diag( \
                                  O_mat[:,int(observations[seq_index])]))

        forward[:,seq_index+1] = forward[:,seq_index+1]/ \
                                 np.sum(forward[:,seq_index+1])
    # backward algorithm
    # P(x_k+1:n|z_k) = sumOver( P(x_k+2:n|z_k+1)*P(x_k+1|z_k+1)*P(z_k+1|z_k) )
    backward[:,-1] = 1.0
    for seq_index in range(seq_len, 0, -1):
        b_col = np.matrix(backward[:,seq_index]).transpose()
        backward[:, seq_index-1] = (np.matrix(T_mat) * np.matrix(np.diag \
                                   (O_mat[:,int(observations[seq_index-1])])) \
                                   *b_col).transpose()
        backward[:,seq_index-1] = backward[:,seq_index-1]/ \
                                  np.sum(backward[:,seq_index-1])
        
    # combination to obtain f-b algorithm
    prob_mat = np.array(forward)*np.array(backward)
    prob_mat = prob_mat/np.sum(prob_mat, 0)
    prob_mat = prob_mat[:,1:]

    return prob_mat, forward, backward

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
                     1, 1, 2, 1, 1, 1]
    
    #testing function
    test01 = forward_backward(T_mat, O_mat, observations1)
    test02 = forward_backward(T_mat, O_mat, observations2)
    test03 = forward_backward(T_mat, O_mat, np.hstack( \
                                              (observations1, observations2) ))
    return (test01, test02, test03)

if __name__ == '__main__':
    a,b,c = test()
    print(a[0], b[0], c[0])