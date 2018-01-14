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

We use the relationship,

> P( [n,m,l,...], i ) = P( [m,l,...], i-1 ) * T(m, n) * O_(n, i) 

where T(m,n) is the transition probability from m to n, and O(n,i) is the 
observation probability of the relevant observation in given sequence at time i for the state n. P([n,m,l,...],i) is the probability of obtaining the 
sequence of states [n,m,l,....] at time i. We calculate this probability for all possible present states (varying n), and select the most probable state. 
Computing this recursively, we obtain the most probable state sequence for a given sequence of observations. We assume the transition and observation 
probabilities are known. This encompasses the basic idea behind the Viterbi Algorithm.  


## Forward Algorithm
We use this to calculate P(z_i, x_1:i). This is the joint probability of state z_i at time i and observations [x_1,x_2,....,x_i] until time i. 
We will refer to these as joint state probabilies. The following relationship is used. 
 
> P(z_i, x_1:i) = sum_over_all_states{P(z_i, z_i-1, x_1:i)} = sum_over_all_states{P(x_i|z_i, z_i-1, x_1:i-1)*P(z_i|z_i-1,x_1:i-1)*P(z_i-1, x_1:i-1)}
> P(z_i, x_1:i) = sum_over_all_states{ P(x_i|z_i) * P(z_i|z_i-1) * P(z_i-1, x_1:i-1) }

Using a base case of P(z_1, x_1) = P(z_1)*P(x_1|z_1), we use this algorithm to obtain joint state probabilies given a sequence of observations. 


## Backward Algorithm
We use this to calculate P(x_i+1:n | z_i). This is the conditional probability of observations [x_i+1,x_i+2,....,x_n] from time i+1 to n given 
the state z_i at time i. We will refer to these as conditional observation probabilies. The following relationship is used. 
 
> P(x_i+1:n | z_i) = sum_over_all_states{ P(x_i+1:n, z_i+1 | z_i,) } 
> P(x_i+1:n | z_i) = sum_over_all_states{ P(x_i+2:n | z_i, z_i+1, x_i+1) * P(x_i+1 | z_i+1, z_i) * P(z_i+1 | z_i) }
> P(x_i+1:n | z_i) = sum_over_all_states{ P(x_i+2:n | z_i+1) * P(x_i+1 | z_i+1) * P(z_i+1 | z_i) }

Using a base case of P(x_n+1 | z_n) = 1 (for all states), we use this algorithm to obtain conditional observation probabilies given a fixed state. 


## Forward Backward Algorithm
We use this to calculate P(z_i | x). This is the conditional probability of state z_i at time i given observations [x_1,x_2,....,x_n] for all time steps. 
We will refer to these as conditional state probabilies. P(z_i | x) is proportional to P(z_i, x). Hence the following relationship is used. 
 
> P(z_i, x) = sum_over_all_states{ P(x_i+1:n | z_i, x_1:i ) * P(z_i, x_1:i) } 
> P(z_i, x) = sum_over_all_states{ P(x_i+1:n | z_i ) * P(z_i, x_1:i) } 

We can obtain these values using the individual forward and backward algorithms, and hence compute the conditional probabilies for all states given 
the entire sequence of observations. 


## References
* http://stellar.mit.edu/S/course/6/fa12/6.047/courseMaterial/topics/topic2/lectureNotes/Lecture07_HMMsIIb_6up/Lecture07_HMMsIIb_6up.pdf
* https://stats.stackexchange.com/questions/31746/what-is-the-difference-between-the-forward-backward-and-viterbi-algorithms
* https://jyyuan.wordpress.com/tag/hidden-markov-models/
* http://www.cis.upenn.edu/~cis262/notes/Example-Viterbi-DNA.pdf
