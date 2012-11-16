*******************************************************************************************
Umit Cavus Buyuksahin
Strahinja Lazetic
Course: Advanced Topic of Distributed Systems
Mini Project in topic "Sampling Massive Online Graphs" that is made by Maciej Kurant
********************************************************************************************

The purpose is estimation of given offline network size. There are several techniques
that are implemented in this source code. These are:
	1- Collision Counting
	2- Induced Edge applied to nodes collected by 
		a-- Uniform Independence Sample/Without replacement (UIS WOR)
		b-- Uniform Independence Sample/With Replacement (UIS WR)
		c-- Weighted Independence Sample/With Replacement (WIS WR)
		d-- Random Walk (RW) with Thinning/SafetyMargin	


Implementations:

-GraphSize.py
	it is the main code that runs all scripts and print the estimated result with 
	the corresponding techniques. The code includes some parameters for estimation
	that are manually changed in the code:
		- n_sample= number of sampled node
		- teta    = Thininnig factor for RW
		- m	  = Safety Margin factor for RW
		- collision.numberof_collsion(G,n_sample) = returns estimated graph size 
		  by using collision method
		- UIS_WOR.UIS_WOR(G,n_sample) = returns estimated graph size by using
		  UIS_WOR method
		- UIS_WR.UIS_WR(A.keys(),n_sample) = returns estimated graph size by using
                  UIS_WR method
		- Generate_Sampling_WIS.func(A,n_sample) = returns both sampled graphs for WIS 
		  method and list of node with their degrees.
		- WIS_WR.func(A,sampled_Graph,degree_Sampled_Graph) = returns estimated graph 
		  size by using WIS_WR method
		- Thinning.func(A,sampled_Graph,degree_Sampled_Graph,teta) = returns estimated 
		  graph size by using Thinning method for random walk
		- SafetyMargin.func(A,sampled_Graph,degree_Sampled_Graph,m) = returns estimated
		  graph size by using Safety Margin for random walk

-collision.py
	it has numberof_collision(G,n_sample) function inside that takes two arguments:
		- G : whole graph
		- n_sample : number of sampled node

-UIS_WOR.py
	it has UIS_WOR(G,n_sample) function inside that takes two arguments:
		- G : whole graph
                - n_sample : number of sampled node

-UIS_WR.py
	it has UIS_WR(L,n_sample) function inside that takes two arguments:
		- L : list of sets of neighbors
		- n_sample : number of sampled node

-Generate_Sampling_WIS.py
	it has func(G,n_sample) function inside that takes two arguments:
                - G : whole graph
                - n_sample : number of sampled node

-WIS_WR.py
	it has func(G,sampled_Graph,degree_Sampled_Graph) function inside that takes four arguments:
		- G : whole graph
		- sampled_Graph : sampled graph
		- degree_Sampled_Graph : list of degress of sampled nodes

-Thinning.py
	it has func(G,sampled_Graph,degree_Sampled_Graph,teta) function inside that takes four arguments:
		- G : whole graph
                - sampled_Graph : sampled graph
                - degree_Sampled_Graph : list of degress of sampled nodes
		- teta : thinning factor

-SafetyMargin.py
	it has func(A,sampled_Graph,degree_Sampled_Graph,m) function inside that takes four arguments:
		- G : whole graph
                - sampled_Graph : sampled graph
                - degree_Sampled_Graph : list of degress of sampled nodes
                - m : thinning factor


Sample Run:
	When GraphSize.py script run like this:
		$python GraphSize.py 
	all calculations will be printed. 
