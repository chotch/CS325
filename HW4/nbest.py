import heapq

def nbesta(a, b):
	#for i, y in enumerate(a):
	
	return 1
	
def nbestb(a,b):
	return 2	


def _nbestc(a,b):
	def put(i,j):
		if 0<=i<n and 0<=j<n and (i,j) not in used:
			used.add((i,j))
			heapq.heappush(h,((sa[i] + sb[j], sb[j]), (sa[i], sb[j]), (i,j)))
			print((sa[i]+sb[j], sb[j]), (sa[i], sb[j]), (i,j))

	sa, sb = sorted(a), sorted(b)
	n = len(a)
	h, used = [], set()
	
	print(sa)
	print(sb)

	put(0,0)
	for _ in range(n):
		print(h)
		_, xy, (i,j) = heapq.heappop(h)
#		print(i,j)
#		print(xy)
		yield xy
		put(i+1, j)
		put(i, j+1)

nbestc = lambda a, b: list(_nbestc(a,b))

def main():
	a = [4,1,5,3]
	b = [2, 6, 3, 4]
#	print(a)
#	print(b)
#	print(nbesta(a,b))
#	print(nbestb(a,b))
	print(nbestc(a,b))


main()
