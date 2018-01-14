# HMMs
Blocks and Algorithms for implementing Hidden Markov Models (HMM)


## Introduction

There are a few basics essential for building HMMs. We will discuss them below.

**Markov Chains** are sequences of states where the states can be observed. We call the probability of a state changing to another or 
remaining the same (change in next item of sequence) the transition probability. In Markov Chains the transition probability depends only 
on the current state. This is referred to as the Markov property.

**HMMs** are similar to Markov Chains but we cannot observe the states: they are hidden. Instead, there are certain observations visible. We use those 
observations to predict the state. 


## Viterbi Algorithm 

We use the relationship $ P_{n,m,l,...}^{i} = P_{m,l,...}^{i-1} * T_{m,n} * O_{n}^{i} $

