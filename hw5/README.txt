My code does not work 100%. There is a problem with finding the last configuration. 
I narrowed down the problem to how we split an edge. 
I noticed there was a problem in how I calculate the t after returning an edge. I tried to debug and you 
can find the print statements littered throughout the code. I also have included my test.py. 

Currently my problem is that I am always calculating the path from the the initial point and I am not sure why.
The algorithm generates a path for numIt = 500

To run the code, run python3 hw5.py --alg rrt.