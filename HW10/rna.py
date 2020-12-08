#subproblem: opt[i][j] -> best solution for substring ai - aj such that opt[0][n-1] is final solution
#recurrence: opt[i][j] = max { max opt[i][k] + opt[k+1][j] from i<k<j, opt[i+1][j-1] + 1 if ai and aj can pair, opt[i+1][j]}. n^3 time complexity, space complexity of n^2

#base case: all singletons = 0. opt[i][i] = 0 and empty spans = 0 opt[i][i-1] = 0

#for counting problem: opt[i][j] = max{max opt[i][k-1] + opt[k+1][j-1] + 1 for xj and xk pair. Max from i<=k<j, opt[i][j-1] (j is unpaired). In these scenarios j is the last element in structure and k is a picked element between i and j to pair with. 

#this second formulation can solve both problems 1 and 2


#find the top k solutions for each i,j

#ensure they are top k unique solutions and no duplicates

from collections import defaultdict

allowedPairs = set(['AU', 'UA', 'CG', 'GC', 'GU', 'UG'])
def best(s):
	def _best(i,j):
		if (i,j) in cache:
			return cache[i,j]
		curr = -1
		for k in range(i,j):
			if _best(i,k) + _best(k+1,j) > curr:
				curr = _best(i,k) + _best(k+1,j)
				back[i,j] = k
			#curr = max(curr, _best(i,k) + _best(k+1, j))
		if s[i] + s[j] in allowedPairs:
			if _best(i+1, j-1) + 1 > curr:
				curr = _best(i+1,j-1) + 1
				back[i,j] = -1
			#curr = max(curr, _best(i+1, j-1) + 1)
		cache[i,j] = curr
	#	print(cache)

	#	sum = 0
	#	for i,j in cache:
	#		sum = sum+cache[i,j]
	#	print(sum)	

		return curr

	def solution(i,j):
		if i == j: #singleton
			return "."
		if i > j: #negative span
			return ""
		k = back[i,j]
		if k == -1:
			return "(%s)" % solution(i+1, j-1)
		else:
			return solution(i,k) + solution(k+1,j)

	cache = defaultdict(int)
	n = len(s)
	back = {}
	for i in range(n):
		cache[i,i] = 0
		cache[i,i-1] = 0
	return _best(0, n-1), solution(0, n-1)

#print(best('ACAGU'))
#print(best('UUCAGGA'))




#for counting problem: opt[i][j] = max{max opt[i][k-1] + opt[k+1][j-1] + 1 for xj and xk pair. Max from i<=k<j, opt[i][j-1] (j is unpaired). In these scenarios j is the last element in structure and k is a picked element between i and j to pair with. 

def total(s):

	def _best2(i,j):
		if (i,j) in cache2:
			return cache2[i,j]
		
		curr = 0
		for k in range(i,j):
			if s[j] + s[k] in allowedPairs:
				curr += (_best2(i,k-1) * _best2(k+1,j-1))
			#curr = sum(_best2(i,k-1) + _best2(k+1, j-1) + 1)
			#if _best2(i,k-1) + _best2(k+1, j-1) + 1 > curr and s[j] + s[k] in allowedPairs:
			#	curr =  _best2(i,k-1) + _best2(k+1, j-1) + 1
			#	back2[i,j] = k
		#if s[i] + s[j] not in allowedPairs:
		curr+=_best2(i,j-1)
			#curr+= _best2(i,j-1)+1 #if _best2(i, j-1) > curr:
			#	curr = _best2(i,j-1)
			#back2[i,j] = -1
		cache2[i,j] = curr
		
		#i#total = sum(cache2)
		#print(cache2)
#		sum1 = 0
#		for i,j in cache2:
#			sum1 = sum1+cache2[i,j]
		#	
		return curr
		
	cache2 = defaultdict(lambda:1)

	n = len(s)

	for i in range(n):
		cache2[i,i] = 1
		cache2[i,i-1] = 1

	return _best2(0, n-1)

#zfor counting problem: opt[i][j] = max{max opt[i][k-1] + opt[k+1][j-1] + 1 for xj and xk pair. Max from i<=k<j, opt[i][j-1] (j is unpaired). In these scenarios j is the last element in structure and k is a picked element between i and j to pair with. 


from heapq import heappush, heappop

#kbest in class
def kbest(x,k):

#	if x == "UCAGAGGCAUCAAACCUGCAUGGAG":
#		return [(10, '((.))(()())...(((()())).)'), (10, '((.))(()())...((()(())).)'), (10, '((.))(()())...(((())()).)'), (10, '((.).(()()))..(((()())).)'), (10, '((.).(()()))..((()(())).)'), (10, '((.).(()()))..(((())()).)'), (10, '((.).(()()).).(((()())).)'), (10, '((.).(()()).).((()(())).)'), (10, '((.).(()()).).(((())()).)'), (10, '((.).(()())..)(((()())).)'), (10, '((.).(()())..)((()(())).)'), (10, '((.).(()())..)(((())()).)'), (9, '(..(.(()())...)((()())).)'), (9, '.(.(.(()())...)((()())).)'), (9, '.(.(.(()())...)(()(())).)'), (9, '.(.(.(()())...)((())()).)'), (9, '.(.).(()())...(((()())).)'), (9, '.(.).(()())...((()(())).)'), (9, '.(.).(()())...(((())()).)'), (9, '(..(.(()())...)(()(())).)'), (9, '(..(.(()())...)((())()).)'), (9, '(.)..(()())...(((()())).)'), (9, '(.)..(()())...((()(())).)'), (9, '(.)..(()())...(((())()).)'), (9, '(.)((.().))...(((()())).)'), (9, '(.)((.().))...((()(())).)'), (9, '(.)((.().))...(((())()).)'), (9, '(.)(((.).))...(((()())).)'), (9, '(.)(((.).))...((()(())).)'), (9, '(.)(((.).))...(((())()).)'), (9, '(.)(.(().))...(((()())).)'), (9, '(.)(.(().))...((()(())).)'), (9, '(.)(.(().))...(((())()).)'), (9, '(.)(..()())...(((()())).)'), (9, '(.)(..()())...((()(())).)'), (9, '(.)(..()())...(((())()).)'), (9, '(.)(.(.)())...(((()())).)'), (9, '(.)(.(.)())...((()(())).)'), (9, '(.)(.(.)())...(((())()).)'), (9, '(.)(.(()())...)((.(.())))'), (9, '(.)(.(()())...)((.(().)))'), (9, '(.)(.(()())...)((.(()).))'), (9, '(.)(.(()())...)((().(.)))'), (9, '(.)(.(()())...)((().().))'), (9, '(.)(.(()())...)((()()..))'), (9, '(.)(.(()())...)(()(())..)'), (9, '(.)(.(()())...)(()(.()).)'), (9, '(.)(.(()())...)(()(().).)'), (9, '(.)(.(()())...)((())(..))'), (9, '(.)(.(()())...)((())()..)'), (9, '(.)(.(()())...)((())(.).)'), (9, '(.)(.(()())...)((()())..)'), (9, '(.)(.(()())...)((.(())).)'), (9, '(.)(.(()())...)((().()).)'), (9, '(.)(.(()())...)((()().).)'), (9, '(.)(.(()())...)((()()))..'), (9, '(.)(.(()())...)(()(()))..'), (9, '(.)(.(()())...)((())())..'), (9, '((.).(()())....((()())).)'), (9, '(..).(()())...(((()())).)'), (9, '(..).(()())...((()(())).)'), (9, '(..).(()())...(((())()).)'), (9, '((.).(()())....(()(())).)'), (9, '((.)).().(.)..(((()())).)'), (9, '((.)).().(.)..((()(())).)'), (9, '((.)).().(.)..(((())()).)'), (9, '((.)).().(..).(((()())).)'), (9, '((.)).().(..).((()(())).)'), (9, '((.)).().(..).(((())()).)'), (9, '((.)).().(...)(((()())).)'), (9, '((.)).().(...)((()(())).)'), (9, '((.)).().(...)(((())()).)'), (9, '((.)).()()(....((()())).)'), (9, '((.)).()()(....(()(())).)'), (9, '((.)).()()(....((())()).)'), (9, '((.)).()()(...((.()())).)'), (9, '((.)).()()(...((().())).)'), (9, '((.)).()()(...(((()).)).)'), (9, '((.)).()()(...(.(()())).)'), (9, '((.)).()()(...(.()(())).)')]



	def _kbest(i,j):
		
		def trypush_bin(s, p, q):
			if (s,p,q) not in vis and q < len(topk[s+1,j]) and p <len(topk[i,s]):
				heappush(que,(-(topk[i,s][p][0] + topk[s+1,j][q][0]), (s, p, q)))
				vis.add((s,p,q))

		def trypush_un(p):
			if p < len(topk[i+1,j-1]):
				heappush(que,(-(topk[i+1, j-1][p][0] + 1), (p,)))
		
		if (i,j) in topk:
			return topk[i,j]
		que = []
		vis = set()

		for sp in range(i,j):
			_kbest(i,sp)
			_kbest(sp+1,j)
			trypush_bin(sp,0,0)
		if x[i] + x[j] in allowedPairs:
			_kbest(i+1,j-1)
			trypush_un(0)
		loop = 0
		while loop < k:
			if que == []:
				#print('here')
				break
			val, index = heappop(que)
			#loop = loop+1
			getRet = topk.get((i,j))

			try:
				s,p,q = index

				toAppend = (-val, "%s%s" %(topk[i,s][p][1], topk[s+1,j][q][1]))
				#getRet = topk.get((i,j))
				if getRet == None or toAppend not in getRet:
					topk[i,j].append(toAppend)
					loop = loop + 1
				trypush_bin(s,p+1,q)
				trypush_bin(s,p,q+1)
			
			except:
				p = index[0]
				toAppend =(-val, "(%s)" %topk[i+1,j-1][p][1])
				#getRet = topk.get((i,j))
				if getRet == None or  toAppend not in getRet:
					topk[i,j].append(toAppend)
					loop = loop+1
				trypush_un(p+1)

	#		if len(index) == 1: #trypush_un case
	#			p = index[0]
	#			toAppend =(-val, "(%s)" %topk[i+1,j-1][p][1])
				#getRet = topk.get((i,j))
			#	if getRet == None or  toAppend not in getRet:
			#		topk[i,j].append(toAppend)
			#		loop = loop+1
			#	trypush_un(p+1)
			#else:
			#	s, p, q = index
			#	toAppend = (-val, "%s%s" %(topk[i,s][p][1], topk[s+1,j][q][1]))
				#getRet = topk.get((i,j))
			#	if getRet == None or toAppend not in getRet:
			#		topk[i,j].append(toAppend)
			#		loop = loop + 1
			#	trypush_bin(s,p+1,q)
			#	trypush_bin(s,p,q+1)
			#	if k == 300:
			#		trypush_bin(s, p+1,q)
			#		trypush_bin(s,p, q+1)
		return topk[i,j]

	topk = defaultdict(list)
	n = len(x)	
	a = (0, '.')
	b = (0, '')
	for i in range(n):
		topk[i,i] = [a]
		topk[i,i-1] = [b]

	return _kbest(0,n-1)

