
def best(W,b):
	lb = len(b)
	if W == 0 or lb == 0:
		return 0, []
	#a = ()
	a = []
	ind = 0
	for i in range(0, lb):
		if b[i][2]==1:
		#	a = a, (b[i][0], b[i][1], ind)
			a.append((b[i][0], b[i][1], ind))
			ind = ind+1
		if b[i][2]>1:
			for j in range(0, b[i][2]):
		#		a = a, (b[i][0], b[i][1], ind)
				a.append((b[i][0], b[i][1], ind))
			ind = ind+1
	#del(a[0])
#	print(a)
	#del(
#	a.remove(a[0])
#	print(a)
#	cache = {}
#	def solve(items, max_weight):
#		if not items:
#			return []
#		if (items,max_weight) not in cache:
#			head = items[0]
#			tail = items[1:]
#			include = (head,) + solve(tail, max_weight - head[1])
#			dont_include = solve(tail, max_weight)
#			if total_value(include, max_weight) > total_value(dont_include, max_weight):
#				answer = include
#			else:
#				answer = dont_include
#			cache[(items,max_weight)] = answer
#		return(cache[(items,max_weight)])		
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
	
	#return best2(W,a)

	def dynam(W, a, lengthOriginal):
		n = len(a)
		#print(a)
		dyn = [[0 for i in range(W+1)] for j in range(n+1)]
#		print(dyn)
		indList = []
		for i in range(1, n+1):
			for w in range(1, W+1):
				#if i == 0 or w == 0:
					#dyn[i][w] = 0
					#print(dyn[i][w][1])
				if a[i-1][0] <= w:
					if (a[i-1][1] + dyn[i-1][w-a[i-1][0]]) > dyn[i-1][w]:
					#	indList = dyn[i-1][w-a[i-1][0]][1]
					#	indList.append(a[i-1][2])
						dyn[i][w] = a[i-1][1] + dyn[i-1][w-a[i-1][0]]
						#dyn[i-1][w-a[i-1][0]][1].append(a[i-1][2])
						#dyn[i][w][1] = []
					else:
					#	indList = dyn[i-1][w][1]
						#if len(indList) >=1:
						#	del indList[-1]
						dyn[i][w] = dyn[i-1][w]
						
					#	dyn[i][w][1] = []
				#	dyn[i][w] = max(a[i-1][1] + dyn[i-1][w-a[i-1][0]][0], dyn[i-1][w][0]), []
				else:
	#				indList = dyn[i-1][w]
					#if len(indList) >= 1:
						#del indList[-1]
		#			print('printing list')
		#			print(indList)
					#del indList[-1]	
					dyn[i][w] = dyn[i-1][w]
		#print(dyn)
		maxW = W
		eleUse = [0] *lb
		for i in range(n,0, -1):
			added = dyn[i-1][maxW] != dyn[i][maxW]
			if added:
		#		print('here')
				weight = a[i-1][0]
				eleUse[a[i-1][2]] = eleUse[a[i-1][2]] + 1
				maxW = maxW - weight
	#	print(eleUse)





		return (dyn[n][W],eleUse)
		#answer =  dyn[n][W]
#		print('length of b')
#		print(len(b))
		#print('indexes')
		#print(answer[1])
		#indList = answer[1]
		#del indList[-1]
	#	print(indList)
	#	finalA = []
#		print(answer[1][1])
	#	for i in range(0,lb):
			#print('in loop')
	#		finalA.append(answer[1].count(i))
		#	count = 0
#			if i == answer[1]	
	#	answer[1] = [3, 4, 5, 6]
#		print('finalA')
#		print(finalA)
	#	dyn[i][W] = dyn[n][W][0], finalA
		#answer[1] = finalA
	#	return dyn[i][W]

	return dynam(W,a,lb)

#def main():
#	print(best(3,[(1,5,2), (1,5,3)]))
	#for i in range(0,3):
	#	print(i)
#	for i in range(0,len([2,3])):
##		print(i)
#		print("hello")
#	print(best(20, [(1,10,6), (3,15,4), (2,10,3)]))

#main()

def total_value(items, max_weight):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0
 
cache = {}
def solve(items, max_weight):
    if not items:
        return ()
    if (items, max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items,max_weight)] = answer
    #print(cache[(items,max_weight)])
    return cache[(items,max_weight)]

def main():
#	a = ()
#	print(a)
	
#	a = ("map", 9, 150)
#	print(a)
	#a = a, ("hello", 2, 5)
#	print(a)
#	print(a[0])
#	a = a, ("hey", 2, 3) 
#	print(a)
	print(best(3,[(1,5,1), (1,5,3)]))
	print(best(3,[(1,5,2), (1,5,3)]))
	print(best(20, [(1,10,6), (3,15,4), (2,10,3)]))
	print(best(92, [(1,6,6), (6, 15, 7), (8,9,8), (2,4,7), (2,20,2)]))
	items = (
  	  ("map", 9, 150), ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
 	   ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
	    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
	    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
	    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
	    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
	    ("socks", 4, 50), ("book", 30, 10),
 	   )
	#print(items[0])
	max_weight = 400
	solution = solve(items, max_weight)
#	solution = solution(max_weight, items)
#	print ("items:")
#	print(solution[1][1])
#	for x in solution:
 # 	  print (x[0])
#	print ("value:", total_value(solution, max_weight))
#	print ("weight:", sum([x[1] for x in solution]))

main()
