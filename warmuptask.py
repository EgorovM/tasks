import sys

l = list(map(int,input().split()))
s = int(input())
l.sort()

for i in range(len(l)):
    low = i
    high = len(l)

    while low + 1 < high:
        mid = (low + high) // 2

        if l[i] + l[mid] == s:
            print("Yes")
            sys.exit()
            
        elif l[i] + l[mid] > s:
            high = mid
        else:
            low = mid

print("No")
    
