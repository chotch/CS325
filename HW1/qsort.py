def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x<pivot]
		right = [x for x in a[1:] if x>=pivot]
		return [sort(left)] + [pivot] + [sort(right)]

def sorted(t):
	if tree ==[]:
		return []
	else:
		sorted(tree[0]) + [tree[1]] + sorted(tree[2])
	#if the value is an integer, return it, otherwise continue to break down the array into its partitions and recursively call the function untill it reaches an integer value. The array [[[], 1,[[], 2,[]]]] should return 1 2. If the array element is [] simply return because we do not want to print this value
	if (isinstance(t, int))
		return [t]
	if t == []
		return
	for x in t:
		return sorted(x)
#			for y in x:
#				print('loop2')
#				if (isinstance(y,list)):
#					for z in y:
#						print('loop3')
#						if (isinstance(z,list)):
#							for w in z:
#								print('loop4')
#								if (isinstance(w, list)):
#									for s in w:
#										print('loop5')
										

def main():
	t= sort([3,6,1,2,9,7,11,19])
#	print(sorted(t))
	newt = sorted(t)
	print((t))

main()

def _search(t,x):
	if tree == [] or tree[1] == x:
		return tree
	if x < tree[1]:
		return _search(tree[0], x)
	else:
		_search(tree[2], x)
	#loopp through subarrays of tree t, if the value x iis in the subarray y then return the subarray y
	for y in t:
		if x in y:
			return y
def search(t,x):
	return _search(tree,x) != []
	#get a cleaner version of tree so searching for a value is much cleaner
	newTree = sorted(t)
	for y in newTree:
		if y == x:
			return true
	return false

def insert(t,x):
	r = _search(tree,x)
	if r ==[]:
		r = r + [[],x,[]]
	#if the value x is already present in the tree then do nothing
	if search(t,x):
		return
	else:
		newTree = sorted(t)
#place in front of tree
		if x < newTree(0):
			return [x] + newTree
	#place in back of tree
		if x > newTree(len(newTree)-1):
			return newTree + [x]
	#place in middle of tree between two values
		for i in range(0, len(newTree-2)):
			if (newTree[i] < x and newTree[i+1] > x):
				return newTree[:i] + [x] + newTree[i+1:]
	




