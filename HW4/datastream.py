import heapq

def ksmallest(k, array):
	if k == 0:
		return
		
	length = len(array)

	if k >= length:
		return sorted(array)
	tryHeap = [-x for x in array[0:k]]
	heapq.heapify(tryHeap)
#	print(tryHeap)
#	heapq._heapify_max(tryHeap)
	#print(tryHeap[0])
	#print(array[k])
	i = 1	
	while i == 1:
		testVal = array[k] * -1
		if tryHeap[0] < testVal:
			heapq.heapreplace(tryHeap, testVal)
			#tryHeap[0] = array[k]*-1
			#heapq.heapify(tryHeap)
#			heapq._heapify_max(tryHeap)	
	#		print(tryHeap)
		k = k + 1		
		if k>=length:
			i = 2
#print(tryHeap)
	#print(newHeap)
#	print(len(tryHeap))	
#	while 1:
#		k = k + 1
#		if k>= length:
#			break
#		if heapq.nlargest(1, newHeap) > array[k]:
#			heapq._heapify_max(newHeap)
#			heapq.heappushpop(newHeap, array[k])
#			heapq._heapify_min(newHeap)
	#	if newHeap.nlargest(
	return sorted([-x for x in tryHeap])



#def main():
#	print(ksmallest(4, [10,2,9,3,7,8, 11,5, 7]))
	


#main()
