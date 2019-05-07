def transition():
	N = 7 # the number of node
#	a = [[0,0,0,1],
#		 [1,0,1,1],
#		 [0,0,0,1],
#		 [1,0,1,0]
#		 ]
	a = [[0,0,1,0,0,0,0],
		 [0,1,1,0,0,0,0],
		 [1,0,1,1,0,0,0],
		 [0,0,0,1,1,0,0],
		 [0,0,0,0,0,0,1],
		 [0,0,0,1,1,0,1]
		 ]
	for i in a:
		b = [ (x/float(list(i).count(1))) for x in i]
		print(b)
if __name__ == "__main__":
	transition()

