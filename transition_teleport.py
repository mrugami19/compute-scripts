

def transition_teleport():
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #

#	a = [[0,0,0,1],
#		 [1,0,1,1],
#		 [0,0,0,1],
#		 [1,0,1,0]
#		 ]
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
	a = [[0,0,1,0,0,0,0],
		 [0,1,1,0,0,0,0],
		 [1,0,1,1,0,0,0],
		 [0,0,0,1,1,0,0],
		 [0,0,0,0,0,0,1],
		 [0,0,0,1,1,0,1]
		 ]
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #

	# MODIFY THIS ALPHA 
	# MODIFY THIS ALPHA 
	# MODIFY THIS ALPHA 
	alpha = 0.14 
	# MODIFY THIS ALPHA 
	# MODIFY THIS ALPHA 
	# MODIFY THIS ALPHA 











	N = len(a)
	for i in a:
		b = [ (alpha/N)+(x/float(list(i).count(1)))*(1-alpha) for x in i]
		print(b)
if __name__ == "__main__":
	transition_teleport()

