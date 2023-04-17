To run code, run `python3 Midterm.py --out <name of output file> <input file>` . Note the capital **M**idterm
By default, the command is run with midterm_desc.json to get the initial paramters for the world and output json file.

To change the probability of the goal, scroll to the end of Midterm.py and edit the Script Parameters
  
  
## Problem 2: EC  
1. The paper begins by saying let $C$ and $C_{free}$ be the Configuration Space and the Configuration Space Obstacle.  However, $C$ or $C_{free}$, neither are defined as sets or any mathematical object and there is no definition of such object in the defintion. The definition also implies that there can only be one obstacle.
   The author should first define the world $\mathbf{W} = \mathbf{R}^2$ and then define the C-Space as all possible configurations of the robot $q = (x, y, \theta)$ or something that's appropriate for the robot they are solving the path planning problem for. Following this, $C_{obs} = \{q \in C | A(q) \cap \mathbf{O} \neq \phi \}$ , where $A(q)$ is a configuration of the robot. Them $C_{free} = C \setminus C_{obs}$  

2. The author defines a feasible path $\tau : [q_I, q_G]^T$ . The definition of $\tau$ according to the author implies that $\tau$ is a column vector and not a function at all. However, $\tau$ is a function that maps a continuous path from $q_I$ to $q_G$ where $\tau(s), s \in [0,1], \tau(s) \in C_{free}$. $\tau$ should be defined as $\tau : [0,1] \rightarrow X$ where $X$ is a topological space.