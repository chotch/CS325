from collections import defaultdict

def _order(n, edges):
	
	
	#first create adj. list
	adjlist = defaultdict(list)
	indegree = defaultdict(int)
	
	for u, v in edges:
		adjlist[u].append(v)
		indegree[v] = indegree[v] + 1
#	queue = []
	stack = []
	for u in range(n):
		if indegree[u] == 0:
			stack.append(u)	
	
	while stack != []:
		u = stack.pop(0) #use (0) to simulate a queue and () to simulate stack... using either works for this assignment
		yield u
		for v in adjlist[u]:
			indegree[v] = indegree[v] - 1
			if indegree[v] == 0:
				stack.append(v)	
def order(n, edges):
	return list(_order(n,edges))

order = lambda n, edges: list(_order(n, edges))
def main():
	print(order(5, [(0,1), (1,2), (2,3), (3,4)]))	
	print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))


main()
