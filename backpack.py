n,W = list(map(int,input().split()))

A = [[[0] for i in range(n+1)] for i in range(W+1)]

w = []
p = []

for i in range(n):
    a,b = list(map(int,input().split()))

    w.append(a)
    p.append(b)
    
for i in range(1,n+1):
    A[0][i][0] = i
    
for i in range(1,W+1):
    A[i][0][0] = i

for i in range(1,len(A)):
    if w[A[0][1][0]-1] <= A[i][0][0]:
        A[i][1][0] = p[A[0][1][0]-1]
        A[i][1].append(A[0][1][0])
        
for i in range(2,len(A[0])):
    for j in range(1,len(A)):
        if A[j][0][0] - w[A[0][i][0]-1] == 0:
            A[j][i][0] = p[A[0][i][0]-1]
            A[j][i].append(A[i][0][0])
        elif A[j][0][0] - w[A[0][i][0]-1] >= 1:
            A[j][i][0] = max(p[A[0][i][0]-1] + A[A[j][0][0] - w[A[0][i][0]-1] + 1][i-1][0],A[j][i-1][0])

            if A[j][i][0] > A[j][i-1][0]:
                for q in range(1,len(A[A[j][0][0] - w[A[0][i][0]-1] + 1][i-1])):
                    A[j][i].append(A[A[j][0][0] - w[A[0][i][0]-1] + 1][i-1][q])
                
                A[j][i].append(A[0][i][0])
            else:
                for q in range(1,len(A[j][i-1])):
                    A[j][i].append(A[j][i-1][q])
        else:
            A[j][i][0] = A[j][i-1][0]

            for q in range(1,len(A[j][i-1])):
                A[j][i].append(A[j][i-1][q])

print(len(A[-1][-1])-1,A[-1][-1][0])

for i in range(1,len(A[-1][-1])):
    print(A[-1][-1][i],end = " ")
