def height(bTree):
	#print('in height')
	if bTree == []:
	#	print(bTree)
		return 0
	left = height(bTree[0])
	right = height(bTree[2])
	
	if left>right:
		h = 1 + left
	else:
		h = 1 + right
	#print(h)
	return h

def longest(bTree):
#	print('b tree')
	if bTree == []:
#		print(bTree)
		return 0
	lHeight = height(bTree[0])
	rHeight = height(bTree[2])
	leftPath = longest(bTree[0])
	rightPath = longest(bTree[2])
	pathCrossesParentNode = lHeight + rHeight
	pathDoesNot = max(leftPath, rightPath)
	if pathCrossesParentNode > pathDoesNot:
		return pathCrossesParentNode
	else:
		return pathDoesNot
	return max(lHeight + rHeight, max(leftPath, rightPath))
#	elif isinstance(bTree, int):
#		print(bTree)
#		return
#	else:
#		print(bTree)
#		return longest(bTree[0])	



def main():
	tree = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7 , [[], 9, []]]]]	
	longPath = longest(tree)
	print(longPath)
main()
