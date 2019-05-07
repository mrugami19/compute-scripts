
# purity(A,C) = 1/N sum(k=1 to ..) max(w(k) AND c(j))
# A = {w1,w2,...,wk} is the set of clusters and
# C = {c1,c2,...,cj} is the set of classes
# steps
# For each cluster wk : find class cj with most members nkj in wk
# Sum all nkj and divide by total number of points
def purity():
	# MODIFY ONLY THIS MATRIX #
	cluster1 = ["x","x","x","x","x","o"]
	cluster2 = ["x","o","o","o","o","d"]
	cluster3 = ["x","x","d","d","d"]
	# If you want to add cluster more..
	# e.g)
	# cluster 4 = ["x","x","d"..."a"]
	# x stands for x mark
	# o stands for o mark
	# d stands for diamond mark

	clusters = [cluster1, cluster2, cluster3] # DON'T FORGET TO ADD ONTO!
	
	# MODIFY ONLY THIS MATRIX #





















	N = sum([ len(c) for c in clusters])
	ret = 0
	for C in clusters :
		result = []
		for c in C:
			result.append(list(C).count(c))
		print(result)
		ret = ret + max(result)
	return ret/float(N)
if __name__ == "__main__":
	print(purity())
