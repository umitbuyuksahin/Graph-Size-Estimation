import random
def WIS_WR(I_W,weight_sum):

	n = random.uniform(0, weight_sum)
	for item in I_W.keys():
		weight = I_W[item]
		if n < weight:
			break
		n = n - weight
	return item

