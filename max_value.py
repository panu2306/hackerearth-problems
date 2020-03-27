T = int(input())

#max_list = []

for i in range(T):
	n = int(input())
	A = list(map(int, input().split()))[0:n]
	max = 0
	i,j = 0, 0
	
	for i in range(n-1):
		for j in range(n):
			val = abs(A[i]-A[j]) + abs(i-j)
		
			if(max < val):
				max = val 
		
	print(max)
	#max_list.append(max)

#print(max_list)
