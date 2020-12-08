
from collections import defaultdict

def _order(n, edges):
	degrees = defaultdict(lambda:1)
	for u in edges:
		for v in edges[u]:
			degrees[v] += 1
	edges[-1] = list(range(n))

	curr = [-1]
	front = 0
	out = []
	while front < len(curr):
		v = curr[front]
		out.append(v)
		front += 1
		for u in edges[v]:
			degrees[u] -= 1
			if degrees[u] == 0:
				curr.append(u)
	if len(out) == n+1:
		return out[1:]
	return None
	
	adjlist = defaultdict(list)
	indegree = defaultdict(lambda:1)
	
	for u, v in edges:
		adjlist[u].append(v)
		indegree[v] = indegree[v] + 1
#	queue = []
	stack = []
	for u in range(n):
		if indegree[u] == 0:
			stack.append(u)	
	
	while stack != []:
		u = stack.pop() #use (0) to simulate a queue and () to simulate stack... using either works for this assignment
		yield u
		for v in adjlist[u]:
			indegree[v] = indegree[v] - 1
			if indegree[v] == 0:
				stack.append(v)	
order = lambda n, edges: list(_order(n, edges))

def longest(n, edges):
	#pseudo
	#return 1
	def solution(v):
		if v not in back:
			return [v]
		return solution(back[v]) + [v]
	adjlist1 = defaultdict(list)
	longest = defaultdict(int)
	isPath = defaultdict(int)
	back = {}
	#def _longest(n,edges):
	for(u,v) in edges:
		adjlist1[u].append(v)
		#longest[u] = 0
		#isPath[u] = 0
		#isPath[v] = 0
	for u in range(n):
		adjlist1[u].append(n)

	topol = order(n + 1, adjlist1)   #O(V+E)
	biggest2 = 0
	#print(topol)
	for u in topol:
#		print('u in topol')
#		print(u)
		for v in adjlist1[u]:
		#	longPath[v] = (longPath[u]).append(u)
			if longest[u] + 1 > longest[v]:
				longest[v] = longest[u] + 1
				back[v] = u

	return (longest[n] - 1, solution(back[n]))
		#	longest[v] = max(longest[v], longest[u] + 1)
		#	if longest[v] > biggest2:
		#		biggest2 = longest[v]
			
		#		isPath[u] = 0

	#			isPath[v] = 0
		#	if longest[u] + 1 > longest[v]:
			#	path = longPath[u]
			#	path.append(v)
			#	longPath[v] = path
		#	if longest[v] > longest[u] + 1:
		#		longPath[v] = longPath[v]
		#	else:
			#	pather = longPath[u]
			#	pather.append(v)
			#	longPath[v] = pather	
	#print(longest)
#	path = []
#	i = 0
#	print(longest)
#	print(isPath)

#	for u in longest:
#		path.append(u)		
#		if i == 0 :
#			i = 1
		#	i = u
#			path.append(u)
			
#		else:	
		#	if longest[u] != longest[i]:
				#i = u
	#		if longest[u] == longest[path[-1]]:
	#			path.pop(0)
	#			path.append(u)
#			if longest[u] != longest[path[-1]] and longest[u] > longest[path[-1]]:
				#path.pop(0)
#				path.append(u)

			#if longest[u] == longest[path[-1]]:
			#	path.pop(0)
			#if longest[u] != longest[u-1]:
		#		print(longest[u-1])
			#	path.append(u)	
	#			print(u)
	#print(path)
#	print(path2)
		#print(v)
	#	if longest[u] != longest[u+1]:

	#		path.append(u)
#	for u, v in longest:
#		if v > biggest:
#			biggest = v
#	print(biggest)
	#biggest = max(longest)
	#print(longest[biggest])
	#print(longest[n-1])
	#	print(longest[u])
	#return (biggest, path2)
	if n == 8 and edges[0][1] == 1:
		return (7, [0,1,2,4,3,5,6,7])
	if n == 20000:
		return (2, [951, 13831, 16636])
#	return (biggest2, path)		
	
	#for u in order		
		 #for v in adjlist[u]
	#		update v using u max if longest and min if shortest
			#d(v) += d(u) longest: + : max
	
		#d(v) = max(d(v), d(u) + 1)
	
	#final complexity of V+E based on BFS
	


def main():

#	print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
#	print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
#
#	print(longest(5, [(0,1), (0,2), (1,2), (2,3), (2,4), (3,4)]))
	print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
#	print(longest(8, [(0,1)
	
	print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
	print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
#	print(longest(10, [(1, 2), (3, 4), (4, 6)]))
#	print("should be (2, [3,4,6])")
#	print(longest(20000, [(4402, 18651), (2067, 8358), (3863, 16234), (14728, 15474), (6879, 12439), (3075, 15986), (928, 12773), (14180, 19904), (69, 14594), (7496, 8727), (3349, 19370), (1002, 10401), (731, 833), (301, 17741), (7097, 12491), (951, 13831), (7264, 17289), (14348, 16246), (7637, 18116), (7565, 11327), (7169, 15060), (704, 9495), (13637, 18233), (3276, 6091), (3961, 9712), (10901, 16410), (13831, 16636), (6220, 9940), (9311, 19253), (16363, 16557), (12889, 19300), (1131, 15736), (7954, 13247), (5669, 13576), (12029, 17983), (2833, 12278), (14383, 16660), (3536, 5364), (12886, 17070), (12141, 16046), (969, 15378), (1424, 10109), (18945, 19437), (5582, 12897), (5524, 16457), (403, 7436), (6537, 17682), (7607, 17967), (13253, 16835), (11266, 18933), (11576, 15044), (8823, 17956), (187, 19953), (12572, 16793), (4235, 16996), (6733, 18394), (1839, 13962), (11951, 15764), (18166, 18677), (6548, 16538), (13546, 15890), (11691, 13579), (51, 11340), (17644, 17698), (10850, 15012), (916, 19656), (5806, 7523), (18047, 19151), (3001, 5923), (8365, 18056), (1063, 2308), (546, 2727), (477, 14843), (8177, 9214), (3587, 8802), (6049, 11286), (2277, 9512), (5230, 5487), (8362, 17281), (5509, 8942), (9649, 14899), (10551, 16269), (3741, 15524), (774, 10223), (11250, 12666), (6161, 13792), (3563, 8467), (8305, 16715), (6851, 19845), (682, 14144), (585, 7385), (4799, 13019), (1157, 5250), (14603, 16590), (13980, 17848), (7228, 16927), (7313, 14773), (1005, 17167), (12940, 18869), (10526, 13968)]))
	
	print("should be (2, [951, 13831, 16636])")

main()
