# Reference : https://www.youtube.com/watch?v=IB5MuzSIin8
# Question : Compute the hub and authority weights for the following graph
import numpy 
from numpy import linalg

def HITS():


   # MODIFY ONLY THIS MATRIX #
	a = [[0,0,1,0,0,0,0],
		 [0,1,1,0,0,0,0],
		 [1,0,1,2,0,0,0],
		 [0,0,0,1,1,0,0],
		 [0,0,0,0,0,0,1],
		 [0,0,0,0,0,1,1],
		 [0,0,0,2,1,0,1]
		 ]
   # MODIFY ONLY THIS MATRIX #













	a_transpose = numpy.transpose(a)
	# Assume the initial hub weight vector is
	# [
	#  [1],
	#  [1],
	#  [1]
	# ]
	#hub_weight = [[1],[1],[1]]
	hub_weight = getHubWeight([[1],[1],[1],[1],[1],[1],[1]])
	# compute the authority weight vector
	# v = A_transpose (dot product) hub_weight
	authority_weight = numpy.dot(a_transpose, hub_weight)
	aut_n = normalize(authority_weight)
	a0 = aut_n
	hub_set = []
	aut_set = []
	for i in range(len(a)):
		h = numpy.dot(a, aut_n)
		h_n = normalize(h)
		aut = numpy.dot(a_transpose, h_n)
		aut_n = normalize(aut)
		hub_set.append(h_n)
		aut_set.append(aut_n)
	print("==========Hub vector with normalization============")
	print("h(0)", hub_weight)
	for i,v in enumerate(hub_set):
		print("h("+str(i+1)+")", v)
	print("===================================================")
	print("==========Authority vector with normalization============")
	print("a(0)", a0)
	for i,v in enumerate(aut_set):
		print("a("+str(i+1)+")", v)

def getHubWeight(a):
	b = []
	for i in a:
		j = [round(x/float(len(a)), 2) for x in i]
		b.append(j)
	return b
def normalize(a):
	b = []
	MAX = max(a)
	for i in a:
		j = [round(x/MAX, 3) for x in i ]
		b.append(j)
	return b
if __name__ == "__main__":
	HITS()
