import sys

l = list(map(int,input().split()))
s = int(input())

d = set()

for i in range(len(l)):
    if (s - l[i]) in d:
        print("Yes")
        sys.exit()
        
    d.add(l[i])

print("No")
