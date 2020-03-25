N, Q = list(map(int, input().split()))

l = [int(x) for x in input().split()][:N]

while(Q!=0):
	q = [int(x) for x in input().split()]
	
	if(q[0]==0):
		s = l[q[1]:q[2]]
		sum = 0
		length = len(s)
        	
		for i in range(length):
			if(s[i]!=0):
				sum += (2**(length-1-i))*s[i]
		
		if(sum%2 == 0):
			print("EVEN")	
		else:
                	print("ODD")

	else:
        	if(l[q[1]] == 0):
                	l[q[1]] = 1
        	else:
                	l[q[1]] = 0

	Q = Q-1

