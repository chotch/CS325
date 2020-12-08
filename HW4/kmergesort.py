from heapq import merge, heapify, heappop, heappush
#slow merge sort n^2
def mergesorted(a,b):
	if a == [] or b == []:
		return a + b
	elif a[0] <= b[0]:
		return [a[0]] + mergesorted(a[1:], b)
	else:
		return [b[0]] + mergesorted(a, b[1:])	

def mergesort(lst):
	l = len(lst)
	if l <= 1:
		return lst
	return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

#nlogn
#same mergesort definition
def mergesorted(a,b):
	if a == [] or b ==[]:
		return a + b
	c = []
	i,j = 0,0
	la, lb = len(a), len(b)
	while i < la or j < lb:
		if i == la or (j!= lb and a[i] > b[j]):
			c.append(b[j])
			j = j + 1
		else:
			c.append(a[i])
			i = i + 1
	return c


def kmergesort(m, k=2):
	length = len(m)
	if length <= 1:
		return m
	split = (length-1)//k + 1
#	print(split)
	k_lists = [kmergesort(m[i:i+split], k) for i in range(0, length, split)]
	print(' in kmerge')
	return list(mymerge(k_lists))


def kmergesort(m, k=2):
	length = len(m) 
	if length<=1:
		return m
	split = (length-1)//k+1
	k_lists = [kmergesort(m[i:i+split], k) for i in range(0, length, split)]
	return list(mymerge(k_lists))

def mymerge(k_lists):
	heap = [(a[0], i, 0) for i, a in enumerate(k_lists)]
	heapify(heap)
	print(heap)
	print('in my merge')
	while heap != []:
		x, i, j = heappop(heap)
		yield x
		a = k_lists[i]
		if j<len(a) - 1:
			heappush(heap, (a[j+1], i, j+1))

def mymerge(k_lists):
	heap = [(a(0), i, 0) for i, a in enumerate(k_lists)]
	heapify(heap)
	while heap!=[]:
		x,i,j = heappop(heap)
		yield x
		a = k_lists[i]
		if j<len(a) - 1:
			heappush(heap, (a[j+1], i, j+1))

def mymerge(k_lists):
	heap = [(a[0], i, 0) for i,a in enumerate(k_lists)]
	heapify(heap)
	while heap!=[]:
		x,i,j= heappop(heap)
		yield x
		a = k_lists[i]
		if j<len(a)-1:
			heappush(heap, (a[j+1], i, j+1))

def mymerge(k_lists):
	heap = [(a[0], i, 0) for i,a in enumerate(k_lists)]
	heapify(heap)
	while heap!=[]:
		x,i,j = heappop(heap)
		yield x
		a = k_lists[i]
		if j<len(a)-1:
			heappush(heap, (a[j+1], i, j+1))
			print(heap)

mymerge
heap=[(a[0],i, 0) for i,a in enumerate(k_lists)]
heapify(heap)
while heap!=[]:
	x,i,j = heappop(heap)
	yield x
	a = k_lists[i]
	if j<len(a) - 1:
		heappush(heap, (a[j+1], i, j+1)) #i to keep track of which list
		#j to keep track of which index per listi
		#push next item j into list for index i which was just removed
		print(heap)
def main():
	a = [4,5,1,112,51,28,281,75,24,1,85,8, 15, 22]
	print(kmergesort(a, 3))

main()
