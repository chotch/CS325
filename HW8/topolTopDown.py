def orderTopDown(n, edges):
	def visit(u, cache = None):
		if cache is None:
			cache = {}
		if v in cache:
			return
		for u in prereqs[v]:
			visit(u, cache)
		res.append(v)
	
	prereqs = defaultdict(list)
	
	for u,v in edges:
		prereqs[v].append(u)
	res = []
	
	for u in range(n):
		visit(u)
	return res
	print(prereqs)
