# HMMs
Blocks and Algorithms for implementing Hidden Markov Models (HMM)


## Introduction

There are a few basics essential for building HMMs. We will discuss them below.

**Markov Chains** are sequences of states where the states can be observed. We call the probability of a state changing to another or 
remaining the same (change in next item of sequence) the *transition probability*. In Markov Chains the transition probability depends only 
on the current state. This is referred to as the Markov property.

**HMMs** are similar to Markov Chains but we cannot observe the states: they are hidden. Instead, there are certain observations visible. We use those 
observations to predict the state. The probabilities of each observation appearing for a given state are referred to as the *observation probabilities*. 


## Viterbi Algorithm 

We use the relationship P([n,m,l,...],i) = P([m,l,...],i-1) * T(m,n) * O_(n,i) where T(m,n) is the transition probability from m to n, and O(n,i) is the 
observation probability of the relevant observation in given sequence at time i for the state n. P([n,m,l,...],i) is the probability of obtaining the 
sequence of states [n,m,l,....] at time i. We calculate this probability for all possible present states (varying n), and select the most probable state. 
Computing this recursively, we obtain the most probable state sequence for a given sequence of observations. We assume the transition and observation 
probabilities are known. This encompasses the basic idea behind the Viterbi Algorithm.  



