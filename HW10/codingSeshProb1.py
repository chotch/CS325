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
		return curr

	def solution(i,j):
		if i == j: #singleton
			return "."
		if i > j:
			return ""
		k = back[i,j]
		if k == -1:
			return "(%s)" % solution(i,-1,j-1)
		else:
			return solution(i,k) + solution(k+1,j)

	cache = defaultdict(int)
	n = len(s)
	back = {}
	for i in range(n):
		cache[i,i] = 0
		cache[i,i-1] = 0
	return _best(0, n-1), solution(0, n-1)

print(best('ACAGU'))
