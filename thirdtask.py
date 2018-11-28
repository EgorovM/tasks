l = list(map(int,input().split()))
l.sort()

fl = True
for i in range(1,max(l)+1):
    if l[i-1] != i:
        print(i)
        fl = False
        break

if fl:
    print(max(l)+1)
