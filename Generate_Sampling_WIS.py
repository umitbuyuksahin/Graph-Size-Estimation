import Sampling_WIS
def func(G,n):

	deg = {}
        sampledGraph = []
        for i in G.keys():
                deg[i] = len(G[i])

	weight_sum = sum(weight for weight in deg.values())
      
        indx = 0
        while indx < n:
                sampledNode = Sampling_WIS.WIS_WR(deg,weight_sum)
		sampledGraph.append( sampledNode)
                indx += 1

	return sampledGraph, deg

