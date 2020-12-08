#use a priority queue
#min heap
#O(VlogV + E) --> definitely logV because we have min heap
#dijstra (v,e)
	#d(S) = 0
	#d(all others) = infinity.. f = float("inf")
	#Q = start node
	#while Q != empty
		u = pop(Q)
		for u -> v in E #for all v that are adjacent to u. u->v1, u->v2, u->v3
			d(v) = d(u) + c(u,v) #current at v equals cost at u plus cost of path from u to v
			decrease-key(Q,v) #because these are alread in queue so decrease priority
