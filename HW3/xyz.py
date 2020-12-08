def isInArray(array, num):
	for l in range(len(array)):
		if array[l] == num:
			return 1

	return 0


def createTupl(x, y, z):
	val = '(' + str(x) + ', ' +str(y) + ', '+ str(z) + ')'
	return val

def triplets(array):
	#print('in function')
	trpl = []
	i = j = 1
	for l in range(len(array)-1):
	#	print('l')
	#	print(l)
	#	print(array[l])
		#print(l)	
		for w in range(l + 1, len(array) ):
	#		print('w')
	#		print(w)
	#		print(array[w])
		#	print(array[w])
			val = array[l] + array[w]
	#		print(val)
			if isInArray(array, val) == 1:
	#			print('TREUEUEUEUE')
				tup = createTupl(array[l], array[w], val)
				trpl = trpl + [tup]

	return trpl
#prof solution
def _find(a):
	a.sort()
	for i,z in enumerate(a):
		j, k = 0, len(a) - 1
		while j<k:
			s = a[j] + a[k]
			if j == i or s < z:
				j+=1
			elif k == i or s > z:
				k -= 1
			else:
				yield (a[j], a[k], z)
				j += 1
				k -= 1

find = lambda a: list(_find(a))
def main():
	result = triplets([1,4,2,3,5])
	print(result)

	print(find([1,4,2,3,5]))
	print(find([1]))
	print(find([-5,-2,-3,3,5,2]))
	#result = result + [createTupl(3,4,7)]
	#print(result)	
#val = createTupl(1,2,3)
#	print(val)

main()
