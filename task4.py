l = list(map(int,input().split()))
l.sort()
k = 0
fl = True

for i in range(1,min(max(l)+1,len(l)+1)):
    if l[i-1] != i + k:
        print(i + k, end = " ")
        k = k + 1

        if k == 2:
            break

if k == 1:
    print(max(l)+1)
elif k == 0:
    print(max(l)+1,max(l)+2)
