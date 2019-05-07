import re
# P(t|d) = lambda P(t|Md) + (1-lambda)*P(t|Mc)
def smoothing():

	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	#d1 = "Jackson was one of the most talented entertainers of all time"
	d1 = "Xerox reports a profit but revenue is down"
	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	d1 = re.split(" ", d1)
	#d2 = "Michael Jackson anointed himself King of Pop"
	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	d2 = "Lucene narrows quater loss but decreases further"
	# MODIFY ONLY THESE DICTIONARIES #
	# MODIFY ONLY THESE DICTIONARIES #
	d2 = re.split(" ", d2)
	collection = d1+d2
	docs = [d1,d2]
	
	# MODIFY ONLY THESE QUERY #
	# MODIFY ONLY THESE QUERY #
	#query = "Michael Jackson"
	query =  "revenue down"
	# MODIFY ONLY THESE QUERY #
	# MODIFY ONLY THESE QUERY #
	# MODIFY ONLY THESE QUERY #
	query = re.split(" ", query)
	ret = 1
	Lambda = 0.5
	for i,d in enumerate(docs):
		for q in query:
			ret *= Lambda*(list(d).count(q)/float(len(d)))+(1-Lambda)*(list(collection).count(q)/float(len(collection)))
		print("P(q|d"+str(i+1)+") = " + str(ret))
		ret =1

	return 0

if __name__ == "__main__":
	smoothing()
