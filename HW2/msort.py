def mergesort(a):
	if len(a) > 1:
		ind = len(a)//2
		leftA = a[:ind]
		#leftA = a
		rightA = a[ind:]
#		L = length(leftA)
#		R = length(rightA)
		print(leftA)
		print(rightA)
		mergesort(leftA)
		mergesort(rightA)
#		print('length greater than 0')
	else:
		return	

#	print('here')	
	i = j = k = 0
#	k = leftA
	while i < len(leftA) and j < len(rightA):
		if leftA[i] <= rightA[j]:
			a[k] = leftA[i]
			i = i + 1
			
		else:
			a[k] = rightA[j]
			j = j + 1
		k = k + 1

	while i < len(leftA):
		a[k] = leftA[i]
		i = i + 1
		k = k + 1
	while j<len(rightA):
		a[k] = rightA[j]
		j = j + 1
		k = k + 1
#	print(a)
	return a
	

def main():
	array = mergesort([3,2, 9, 1, 12, 10, 5, 6])
	#print('hello')
	print(array)

main()
