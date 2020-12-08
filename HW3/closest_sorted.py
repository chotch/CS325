import bisect
#import find

#prof function
def find1(a,x,k):
	a.append(float("inf"))
	place = bisect.bisect(a,x)
	i, j = place - 1, place
	for _ in range(k):
		if i>=0 and x-a[i] <= a[j] - x:
			i = i - 1
		else:
			j = j + 1
	return a[i+1:j]

def find(array, query, nums):
	#print('here')
#	print(array)
	length = len(array)
	insertInd = bisect.bisect(array, query)
#	insertInd = bisect(array, query)
	#print("insertInd")
	#print(insertInd)
	if insertInd != 0:
		leftPtr = insertInd - 1
	if insertInd != length:
		rightPtr = insertInd		
	indToAdd = []
	#retArray = [0] * nums
	count = 0
	while count < nums :
		if rightPtr >= length:
			indToAdd = [array[leftPtr]] + indToAdd
		#	indToAdd.insert(0,array[leftPtr])	
		#	indToAdd[count] = leftPtr
			leftPtr = leftPtr - 1
		elif leftPtr < 0:
			indToAdd = indToAdd + [array[rightPtr]]
#			indToAdd.append(array[rightPtr])
	#		indToAdd[count] = rightPtr
			rightPtr = rightPtr + 1
		elif query - array[leftPtr] >  array[rightPtr] - query:
			indToAdd = indToAdd + [array[rightPtr]]
#			indToAdd.append(array[rightPtr])
	#		indToAdd[count] = rightPtr
			rightPtr = rightPtr + 1
				
	#		print("rightPtr")
	#		print(rightPtr)
		else:
			indToAdd = [array[leftPtr]] + indToAdd
#			indToAdd.insert(0, array[leftPtr])
	#		indToAdd[count] = leftPtr
			leftPtr = leftPtr -1
	#		print("leftPtr")
	#		print(leftPtr)


		count = count + 1
#	i = 0
	#print(indToAdd)
#	print(indToAdd)
	#for x in sorted(indToAdd):
	#	retArray[i] = array[x]
	#	i = i + 1
#	print(array[indToAdd])
#	for x in indToAdd:
#		retArray[i] = array[x]
#		i = i + 1			
#	print(leftPtr)
#	print(rightPtr)
	return indToAdd


def main():
#	a = [1, 3, 4, 10, 12, 19, 22]
#	ind = bisect.bisect(a, 15)
#	print(ind)
	
	test = find([1,2,3,4,4,7], 6.5, 3)
	print(test)
	print('testing new function')
	print(find1([1,2,3,4,4,5,6], 4, 5))
	print(find1([1], 4, 1))
main()
