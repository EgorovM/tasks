l = list(map(int,input().split()))

s_now = sum(l)
s_real = ((len(l)+1)*(len(l)+2))//2

print( s_real - s_now )
