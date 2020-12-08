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

def main():
#	test = [3, 10, 4, 7, 19]
#	rand = 2
#	pivot = test[rand]
#	if(rand == 0):
#		right = [x for x in test[1:] if x>= pivot]
#	else:
#		right = [x for x in test[:rand] if x>=pivot] + [x for x in test[rand+1:] if x>=pivot]
#	print(right)
#	print(len([]))

	test = qselect(3, [4,5,2,10,8,7])
	print(test)
main()
