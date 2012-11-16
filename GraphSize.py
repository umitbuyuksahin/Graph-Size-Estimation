import UIS_WR
import UIS_WOR
import IE_UIS
import WIS_WR
import collision
import random
import Generate_Sampling_WIS
import Thinning
import SafetyMargin

def load_graph(fname):

	fr = open(fname, 'r')
    	G = {}   # dictionary: node -> set of neighbors
    	for line in fr:
		if not line.startswith('#'):
			a,b = map(int, line.split())    
            		if a not in G:  G[a] = set()
            		if b not in G:  G[b] = set()        
            		G[a].add(b)
            		G[b].add(a)    
	fr.close()    
    	return G
	
A = load_graph("p2p-Gnutella31.txt")
n_sample= 6250
teta=5
m=5

#### COLLISON ###########
print "\n**COLLISON**"
print "GRAPH_SIZE_COLLISON:", collision.numberof_collision(A,n_sample)

######## UIS_WOR ###########
print "\n**UIS_WOR**"
S_WOR = UIS_WOR.UIS_WOR(A,n_sample)   ## return sampled nodeIDs
nIE_WOR, deg_S_WOR = IE_UIS.func(S_WOR, A)
graph_size_WOR =  (n_sample-1)*deg_S_WOR / (2 * nIE_WOR) + 1
print "GRAPH_SIZE_UIS_WOR:", graph_size_WOR

######## UIS_WR ###########
print "\n**UIS_WR**"
S_WR = UIS_WR.UIS_WR(A.keys(),n_sample)   ## return sampled nodeIDs
nIE_WR, deg_S_WR = IE_UIS.func(S_WR, A)
graph_size_WR =  (n_sample-1)*deg_S_WR / (2 * nIE_WR) + 1
print "GRAPH_SIZE_UIS_WR:", graph_size_WR 

######## WIS_WR ###########
print "\n**WIS_WR**"

sampled_Graph, degree_Sampled_Graph = Generate_Sampling_WIS.func(A,n_sample)
graph_size_WIS = WIS_WR.func(A,sampled_Graph,degree_Sampled_Graph)
print "GRAP_SIZE_WIS_WR:",graph_size_WIS



######## THINNINH ###########
print "\n**THINNING**"
print "GRAP_SIZE_THINNING:",Thinning.func(A,sampled_Graph,degree_Sampled_Graph,teta) 


######## SAFETYMARGIN ###########
print "\n**SAFETYMARGIN**"
print "GRAP_SIZE_SAFETYMARGIN:", SafetyMargin.func(A,sampled_Graph,degree_Sampled_Graph,m)
