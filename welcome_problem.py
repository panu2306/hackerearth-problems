print("Enter Size:")
N = int(input())

print("Enter Array 'A':")
A = list(map(int, input().split()))[0:N]

print("Enter Array 'B':")
B = [int(x) for x in input().split()][0:N]

C = []

for i in range(N):
	C.append(A[i] + B[i])
	print(C[i], end=' ')
