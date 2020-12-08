
fibs = {1:1, 2:1}
def fib1(n):
	if n not in fibs:
		fibs[n] = fib1(n-1) + fib1(n-2)
	return fibs[n]


#cheat by realizing num_no(n) == fib1(n+2)
def num_no(n):
	a,b = list(range(0,n)), list(range(0,n))
	a[0] = 1
	b[0] = 1
	#print(a)
	#print(b)
	for x in a[1:n]:
	#	print(x)
		a[x] = a[x-1] + b[x-1]
		b[x] = a[x-1]

#	return fib1(n+2)
	return a[n-1] + b[n-1]
	
#	print(a)
#	return



def num_yes(n):
	return 2**n - num_no(n)

def main():
	print(num_no(5))
	print(num_yes(5))	

main()
