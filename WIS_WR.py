def func(G, sampledGraph, deg):

	w0 = 0.0
	w1 = 0.0
	w2 = 0.0
	w3 = 0.0
	temp = 0.0
	indx = 0
	for i in sampledGraph:
		indx += 1
		for j in sampledGraph[indx:]:
			temp = float(1/float(deg[i]*deg[j]))
			w1 += temp
			if i in G[j]:
				w3 += temp		
		w2 += float(1/float(deg[i]))
	
	w0 = len(sampledGraph)
	return w0*w1/(float(w2*w3)) + 1
	
