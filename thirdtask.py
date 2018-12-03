l = list(map(int,input().split()))

s = 0

for i in range(len(l)):
    s += l[i]

print(((len(l)+1)*(len(l)+2))//2 - s)
