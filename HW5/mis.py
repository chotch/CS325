
def max_wis(a):
	maxWis = {}
	def max_wis1(a):
		if a == []:
			return 0, []
		n = len(a)
		if n == 1 and a[0] > 0:
			return a[0], a
		neg = 1
		for x in a:
			if x > 0:
				neg = 0
		if neg == 1:
			return 0,[]
	
		if n not in maxWis:
			i, l1 = max_wis1(a[:n-1])
			j, l2 = max_wis1(a[:n-2])
			j = j + a[n-1]
			if(j >= i):
				l2.append(a[n-1])
				maxWis[n] = j, l2
				#return maxWis[n]
			else:
				#l1.append(a[n-2])
				maxWis[n] = i, l1
				#return maxWis[n]
		return maxWis[n]
	return max_wis1(a)
#	return 12, [7,5]
#	i = n
#	s = {}
#	
#	while i>=1:
	#	if a[i-1] >= a[i-2]:
	#		i = i - 1
	#	else:
	#		s.add(a[i])
	#		i = i-2
	#return sum(s), s
			
	#if n not in maxWis:
	#	maxWis[n] = max(max_wis(a[0:n]), max_wis(a[0, n-1])+ a[n])
	#return maxWis[n]
	#set = {}
	#i = length(a) - 1
	#while i >= 1:
#		if a[i] == a[i-1]:
#			i = i - 1
#		else:
	#		set << vertex i
#			i = i - 2
#	return set


def max_wis2(a):
	best = {-1:0, -2:0}
	




fibs = {1:1, 2:1}
def fib1(n):
	if n not in fibs:
		fibs[n] = fib1(n-1) + fib1(n-2)
	return fibs[n]

def main():
	print(max_wis([4,6,7]))
	print(max_wis([63229, 7871, 74587, 59445, 71381, 5404, 56721, 41863, 62960, 42424, 37376, 38654, 9686, 88564, 71093, 69118, 26876, 44293, 48730, 2476, 58586, 23466, 4192, 48799, 15818, 28847, 82565, 71941, 95094, 64294, 79614, 16219, 16348, 37528, 57940, 73917, 31890, 80693, 88456, 82255, 39260, 8070, 36726, 87408, 44400, 85485, 88349, 45095, 66399, 12786, 99639, 19331, 63101, 72119, 20801, 69561, 33307, 66400, 9388, 41212, 63564, 85236, 72617, 4787, 97918, 32153, 58247, 8466, 68896, 93322, 21028, 18211, 55043, 24187, 13768, 17505, 54214, 71736, 5284, 41499, 87421, 42354, 64137, 77183, 31897, 40971, 94056, 85477, 17893, 95807, 77428, 13186, 51169, 48753, 36957, 27003, 78557, 93281, 84281, 99236]))	

main()



fibs = {1:1, 2:1}
def fib1(n):
	if n not in fibs:
		fibs[n] = fib1(n-1) + fib1(n-2)
	return fibs[n]
def fib1(n):
	if n not in fibs:
		fibs[n] = fib1(n-1) + fib1(n-2)
	return fibs[n]
	print(fib1(100))
