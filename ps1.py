#Problem Set 1
#Name: Peter Kim
#Collaborators: ???
#Time: 
#

#Problem 1

prime = 0
cand = 3
test = 1
M  = 0

while prime < 1000:
	M = 0
	while test < cand/2:
		if test % cand == 0:
			M = 1
			break
		test = test + 1
	test = 1
	cand = cand + 2
	if M == 0:
		prime = prime + 1
		print cand
		print prime
