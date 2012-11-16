def func(L,G): ## L: nodeID, G:whole graph
	
	nIE = 0
	deg = 0
	indx = 0
	for i in L:
		indx += 1
		for j in L[indx:]:
			if i in G[j]:
				nIE += 1

	for i in L:
		deg += len(G[i])

	return nIE,deg
			 
	
