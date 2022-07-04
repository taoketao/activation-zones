This repo has several scripts and plots involving my 2022 zones project.

The project: I observed that a neural network's nonlinear activation 
functions such as tanh or logistic saturate in surprising ways. In 
networks using these nonlinearities, weights learning via backpropagation 
experience different dynamics based on their numerical value - a phenomenon
not present in linear or RELU networks.  [ todo: finish writing this once
main text is written. ]

The code in this repo catalogs scripts and notebooks used in experiments 
that test the theoretical results against empirical neural networks.

Programs: 
- *comparing-zone-points*. There are several specific numerical points that are important for the variety of weight dynamics caused by a sigmoidal nonlinearity. Crucially, different nonlinearities have these points at different values and with different ratios. This program plots the points of several nonlinearities. This can help inform what kind of nonlinearity is best or worst for a situation, and it also demonstrates that these points are not bijectively unique to a nonlinearity. It identifies critical points linked to max signal strength, noise tolerance and sensitivity, and the point-of-no-unlearning. Currently, it examines: tanh (and therefore logistic), erf, the analytic x/(1+x^p)^(1/p) family, arctan, a odd exponential-based sigmoid, an odd parametric sigmoid, the Guddermann function, an adapted x-x^2, an adapted xth-root-of-x

- *stochastic-process-convergence-sanity-check.py*. I wanted to verify for myself that a random stochastic matrix with any initial distribution will converge to its stationary distribution _exponentially_. If the 'learning rate' is sufficiently small, then that's what happens. As it grows, weights can pass by their eigenpoint but will settle back to them eventually if the rate isn't too high.
