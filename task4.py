import math

l = list(map(int,input().split()))
   
s_real = ((len(l)+3)*(len(l)+2))//2
d_real = 1
s_now = 0
d_now = 1

for i in range(len(l)):
    d_real *= i+1
    d_now *= l[i]
    s_now += l[i]

d_real *= ((len(l)+1) * (len(l)+2))


s1 = s_real - s_now
s2 = d_real // d_now

n1 = int((s1 - math.sqrt(s1*s1 - 4*s2)) // 2)
n2 = int(s1 - n1)

print(n1 , n2)
