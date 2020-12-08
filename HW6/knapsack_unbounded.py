def best2(W,a):
	if W == 0 or len(a) == 0:
		return 0
	n = len(a)
	if a[n-1][0] > W:
		newA = [x for i, x in enumerate(a) if i != (n-1)]
		return best2(W, newA)
	else:
		newA = [x for i, x in enumerate(a) if i != (n-1)]
		return max(a[n-1][1] + best2(W - a[n-1][0],newA), best2(W, newA))


def best(W, a):
	bestW = {}
	#for i in range(W+1):
	#	bestW.append(0)
	for i in range(0, W+1):
		for j in range(0, len(a)):
			if a[j][0] < i:
				bestW[i] = max(bestW[i], bestW[i-(a[j][0])] + a[j][1])
	return bestW[W]
	maxDic = {}
	#def best1(W,a):
	#	#return a[0][1]
	#	i = len(a)
#		w = 0
##		if w not in maxDic:
			 	
		#for x in len(a
	


#		return 2
	


#	return best1(W,a)
	

def main():
#	print(best(3, [(1,2), (2,5)]))
	print(best2(3, [(1,2), (2,5)]))

main()
