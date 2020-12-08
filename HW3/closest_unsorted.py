
import random

def qselect(k, a):
	if (isinstance(a, list)) and len(a) >= 1:	
		rand = random.randint(0, len(a)-1)
		
		pivot = a[rand]
#		print ("random is: ") 
#		print(rand)
#		print("pivot is: ")
#		print(pivot)
		left = [x for x in a if x<pivot]
		if (rand == 0):
			right = [x for x in a[1:] if x>= pivot]
		else:
			right = [x for x in a[:rand] if x>=pivot] + [x for x in a[rand+1:] if x>=pivot]
		if (len(left) + 1 == k):
			return pivot
		elif (len(left) >= k):
			return qselect(k, left)
		else:
			return qselect(k-len(left)-1, right)
		
	else:
		return 




def closest_unsorted(array, x, k):
	print(array)
	print(x)	
	#print(newA)
	arrayCopy = (array)
	for l in range(len(array)):
		arrayCopy[l] = round(array[l], 2)
		print(arrayCopy[l])
	print(arrayCopy)
	returnArray = [0] * k
	plusOrMinus = [0] * len(array)
	for y in range(len(array)):
		if array[y] - x > 0:
			plusOrMinus[y] = 1
		else:
			plusOrMinus[y] = -1
#	print(plusOrMinus)
#	print(returnArray)
	for t in range(len(array)):
		array[t] = abs(array[t] - x)
	print(array)
	retArray = [0 for x in range(k)]
	i = 0
	print(retArray)
	while k>=1:
		retArray[i] = round((x - qselect(k, array)), 1)
		print('hello')
		if retArray[i] == arrayCopy[1]:
			print('inside!')
		
		#ind = qselect(k, array)
	#	if plusOrMinus[ind] == 1:
#			retArray[i] = array[ind] + x
#		else:
#			retArray[i] = x - array[ind] 
	#	retArray[i] = 2
		i = i + 1
		k = k - 1	
		
	print(retArray)
	return
	returnInd = [0] * k
	
	for l in range(k):
		returnInd[l] = qselect(array, l+1)
		#print(l)

	array[t] = array[t] + x
	print(array)
	print(returnInd)
	print(returnArray)
#	for w in range(k):
	#	returnArray[w] = array[returnInd[w]]
	
#	return returnArray
					
	
	
	#array = array -x
def main():
	res = closest_unsorted([4,1,6,2,7,4], 5.2, 2)
	#print(res)
	test = qselect([4,1,3,2,7,4], 3)
	print(test)

main()
