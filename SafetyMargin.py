import math
def func(G,S,deg,m):


	w0 = 0
	w1 = 0
	indx = 0
	indx2 = 1
         
	for i in S:
		indx2= indx + 1
                for j in S[(indx2):]:
			if math.fabs(indx-indx2) > m:
				w0 += float(deg[i] / float(deg[j]))	
				if i in G[j]:
					w1 += float(1/float(deg[i])) 
			indx2 += 1
		indx +=  1

	return w0/float(w1)


