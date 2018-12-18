n, W = list(map(int,input().split()))
w = []
p = []

for i in range(n):
    a,b = list(map(int,input().split()))

    w.append(a)
    p.append(b)

A = [ [0 for i in range(n+1)] for i in range(W+2)]
B = [ [[] for i in range(n+1)] for i in range(W+2) ]

for i in range(1,len(A[0])):
    A[0][i] = i
    
for i in range(1,len(A)):
    A[i][0] = i - 1

for i in range(1,len(A)):
    if A[i][0] - w[0] >= 0:
        A[i][1] = p[0]
        B[i][1].append(1)

for i in range(2,len(A[0])):
    for j in range(1,len(A)):
        if A[j][0] - w[A[0][i]-1] >= 0:
            #если можно взять новую
            A[j][i] = max(p[A[0][i]-1] + A[A[j][0]-w[A[0][i]-1] + 1][i-1], A[j][i-1])
            
            if A[j][i] > A[j][i-1]:
                #лучше брать
                B[j][i].append(A[0][i])

                for q in range(len(B[A[j][0]-w[A[0][i]-1] + 1][i-1])):
                    B[j][i].append(B[A[j][0]-w[A[0][i]-1] + 1][i-1][q])

            else:
                for q in range(len(B[j][i-1])):
                    B[j][i].append(B[j][i-1][q])
                                
        else:
            A[j][i] = A[j][i-1]

            for q in range(len(B[j][i-1])):
                B[j][i].append(B[j][i-1][q])
            
B[-1][-1].sort()
print(len(B[-1][-1]),A[-1][-1])

for i in range(len(B[-1][-1])):
    print(B[-1][-1][i], end = " ")
