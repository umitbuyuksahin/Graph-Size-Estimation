import random
def numberof_collision(G,n):

	L = random.sample(G.values(),n)
	col = 0
	indx = 0
	for first in L:
		indx +=1
		indx2=0
		for rest in L[indx:]:
			if first==rest:
				col += 1
			indx2 += 1
	return n*n / (2*col)
