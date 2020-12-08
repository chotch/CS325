from heapq import heappush, heappop

def nbest(ABs):    # no need to pass in k or n
	k = len(ABs)
	n = len(ABs[0][0])

	def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
		A, B = ABs[i] # A_i, B_i
		if p < n and q < n and (i,p,q) not in used:
			heappush(h, ((A[p] + B[q], B[q]), i, p, q, (A[p],B[q])))
			used.add((i, p, q))
	h, used = [], set()
	heapif = []                # initialize
	for i in range(k):
	#	heapif.append((i,0,0))  # NEED TO OPTIMIZE
		trypush(i,0,0)
	
	#h.heapify(heapif)
	for _ in range(n): 
        	_, i, p, q, pair = heappop(h)
        	yield pair     # return the next pair (in a lazy list)
        	trypush(i, p+1, q)
        	trypush(i, p, q+1)

print(list(nbest([([1,2,4], [2,3,5]), ([0,2,4], [3,4,5])])))
print(list(nbest([([-1,2],[1,4]), ([0,2],[3,4]), ([0,1],[4,6]), ([-1,2],[1,5])])))

