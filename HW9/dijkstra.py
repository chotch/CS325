from collections import defaultdict
from heapdict import heapdict
import heapq


#import heapDict
#use a priority queue + a dictionary so that the node can be easily found in the heap
#min heap
#O(VlogV + E) --> definitely logV because we have min heap
#dijstra (v,e)
	#d(S) = 0
	#d(all others) = infinity.. f = float("inf")
	#Q = start node or can be everybody (then u decrease key always). but if Q is just S then there needs to be an if v is not in Q then push v, else decrease_key(Q,v)
	#while Q != empty
#		u = pop(Q)
#		for u -> v in E #for all v that are adjacent to u. u->v1, u->v2, u->v3
			#if d(v) > d(u) + c(u,v)
			#keep track of back[v]. So for every node we have a back pointer to the node that best got there
#			d(v) = d(u) + c(u,v) #current at v equals cost at u plus cost of path from u to v
#			decrease-key(Q,v) #because these are alread in queue so decrease priority. if v is not in Q just push v into Q.

def shortestC(destination, edges):
	if edges == []:
		return None
	#use a heapdict. peakitem() popitem() h = heapdict.heapdict()
	#to decrease k just say h['name of node'] = new value and it will automatically be pushed up to the top 
	#'name of node' in h? returns true or false
	#nodeValues = defaultdict(int)	#destination = last node (len(edges) - 1)
	start = 0
	goal = destination - 1
	
	h = heapdict()	
	graph = defaultdict(list)
	
	track_priorNode = {}
 
	path = []
	inf = float("inf")
	#set S to 0 and all others to infinity

	for i,j,k in edges:
		graph[i].append((j,k))
		graph[j].append((i,k))

	h[start] = 0

	shortest_distance = defaultdict(lambda:inf)
	shortest_distance[start] = 0


#method attempting to use heapdict
	while h:
		minDistanceNode = h.peekitem()
		node = minDistanceNode[0] #print(minDistanceNode)
		w = minDistanceNode[1]
		path_options = graph[node]
		
		for neighbor,weight in path_options:

			if weight+w < shortest_distance[neighbor]:
				h[neighbor] = weight + w
				shortest_distance[neighbor] = weight + shortest_distance[node]
				track_priorNode[neighbor] = node
			
		popped = h.popitem()
		
		if popped[0] == goal:	
			break
		#fVal = final[0]

#method that works without heapdict
#	while unseenNodes:
#		minDistanceNode = None
		#currNode = h.popitem()
		#minDistanceNode = currNode[0]
		
#		for node in unseenNodes:
#			if minDistanceNode is None:
#				minDistanceNode = node
#			if shortest_distance[node] < shortest_distance[minDistanceNode]:
#				minDistanceNode = node
#		path_options = graph[minDistanceNode]

	#	print('printing minDistanceNode')
	#	print(minDistanceNode)
	#	print('printing graph[minDistanceNode]')
	#	print(path_options)
	
#		for neighbor, weight in path_options:
#			if weight + shortest_distance[minDistanceNode] < shortest_distance[neighbor]:
#				shortest_distance[neighbor] = weight + shortest_distance[minDistanceNode]
#				track_priorNode[neighbor] = minDistanceNode
#		unseenNodes.pop(minDistanceNode)
	currentNode = goal

	path.insert(0, goal)

	while currentNode > 0:
		if currentNode in track_priorNode:
			path.insert(0, track_priorNode[currentNode])
			currentNode = track_priorNode[currentNode]
		else:
			break

	if goal not in track_priorNode:
		return None

	return (shortest_distance[goal], path)


def shortest(n, g):
	
	graph = defaultdict(list)
	for i,j,k in g:
		graph[i].append((j,k))
		graph[j].append((i,k))

	dist = defaultdict(lambda:float("inf"))
	

	dist[0] = 0
	goal = n - 1
	start = 0
	
	previousNodes = defaultdict(list)

	path = []
	queue = [(0,0)]

	while len(queue) > 0:
		d, vertex = heapq.heappop(queue)
	
		for v, w in graph[vertex]:	
			if d + w < dist[v]:
				dist[v] = d + w
				previousNodes[v] = vertex
				heapq.heappush(queue, (d+w, v))

	


	currNode = goal
	path.insert(0,goal)
	while currNode > 0:
		if currNode in previousNodes:
			path.insert(0, previousNodes[currNode])
			currNode = previousNodes[currNode]
		else:
			break
	
	if goal not in previousNodes:
		return None
	return dist[n-1], path

#didnt work for no path:(
	
	while currNode != start:
		try:
			path.insert(0, currNode)
			currNode = previousNodes[currNode]
		except KeyError:
			return None
	path.insert(0, start)
	if dist[goal] != float("inf"):
		return (dist[goal], path)	
	return None

def main():
	#print(shortest(4,[(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	print(shortest(4,[(0,1,1), (2,3,1)]))
		#print(" ")
	#print(shortest(4, [(0,1,1), (2,3,1)]))

main()

#of pops: O(V)
#time for pops: O(VlogV)
#total space: O(V+E)
#decrease keys : O(E)
#time for decrease keys : O(ElogV)
#total: O(V+E)logV
