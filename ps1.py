#Problem Set 1
#Name: Peter Kim
#Collaborators: ???
#Time: 
#

#Problem 1

prime = 0
cand = 1
test = 1
M  = 0

while prime < 1000:
	
	while test < cand:
		
		if cand % test == 0:
			M = M +1
			
		if M > 1:
			test = cand
		test = test + 1
	if M < 2:
		prime = prime + 1
		print 'found'+' '+str(cand)
	cand = cand + 2
	test = 1
	M = 0


#Problem 2


