import operator as op
import itertools
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def random_index():
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
	cluster1 = ["x","x","x","x","x","o"]
	cluster2 = ["x","o","o","o","o","d"]
	cluster3 = ["x","x","d","d","d"]
	# Stub more clusters if needed
	clusters = [cluster1, cluster2, cluster3] # DONT FORGET TO ADD ONTO IT
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #







	N = sum([ len(c) for c in clusters])
	TP_add_FP = 0
	TP = 0
	for C in clusters:
		TP_add_FP += ncr(len(C), 2)
		for a in list(set(C)):
			if ( list(C).count(a) >= 2):
				TP += ncr(list(C).count(a), 2)

	n = [i for i in range(1, len(clusters)+1)]
	n1 = list(itertools.product(n,n))
	n1 = [ list(set(x)) for x in n1 if x[0] != x[1]]
	n2 = []
	for x in n1:
		if x not in n2:
			n2.append(x)

	print("TP+FP : " + str(TP_add_FP))
	print("TP : " + str(TP))
	FP = TP_add_FP - TP
	print("FP : " + str(FP))
	# TF AND FP
	FN = getFN(clusters, n2)
	print("FN : " + str(FN))
	TN = getTN(clusters, n2)
	# pretty printing
	print("====Pretty Printing===")
	print("TP : " + str(TP))
	print("FN : " + str(FN))
	print("FP : " + str(FP))
	print("TN : " + str(TN))
	# Better way to measure because it looks at the combination of clusters
	RI = (TP + TN) / float(TP+FN+FP+TN)
	print("RI : " + str(RI))

	precision = TP / float(TP + FP)
	recall = TP / float(TP + FN)
	F_measure = 2*precision*recall / float(precision + recall)
	print("Precision : " + str(precision))
	print("Recall : " + str(recall))
	print("F measure : " + str(F_measure))

def getTN(clusters, n2):
	different_chances = []
	for a in n2:
		for i in list(set(clusters[a[0]-1])):
			for j in list(set(clusters[a[1]-1])):
				if (i != j):
					different_chances.append((i,j))
	different_chances = list(set(different_chances))
	TN = 0
	for a in n2:
		for c in different_chances:
			print(c, list(clusters[a[0]-1]).count(c[0]) * list(clusters[a[1]-1]).count(c[1]))
			TN += list(clusters[a[0]-1]).count(c[0]) * list(clusters[a[1]-1]).count(c[1])
	print("TN : " + str(TN))
	return TN
def getFN(clusters, n2):
	same_chances = []
	for a in n2:
		for i in list(set(clusters[a[0]-1])):
			for j in list(set(clusters[a[1]-1])):
				if (i == j):
					same_chances.append(i)
	FN = 0
	same_chances = list(set(same_chances))
	for a in n2:
		for c in same_chances:
			print(c, list(clusters[a[0]-1]).count(c) * list(clusters[a[1]-1]).count(c))
			FN += list(clusters[a[0]-1]).count(c) * list(clusters[a[1]-1]).count(c)
	return FN
if __name__== "__main__":
	random_index()

