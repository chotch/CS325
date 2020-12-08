def fibRecurs(n):
	if n<=2:
		return 1
	return fibRecurs(n-1)+fibRecurs(n-2)

def fibBot(n):
	a,b = 1,1
	for i in range(3, n+1):
		a,b = a+b,a
	return a

fibDict = {1:1, 2:1}
def fibMemo(n):
	if n not in fibDict:
		fibDict[n] = fibMemo(n-1) + fibMemo(n-2)
	return fibDict[n]

def main():
	print(fibMemo(12))
	print(fibRecurs(12))
	print(fibBot(12))
main()
