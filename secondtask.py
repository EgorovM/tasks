def hit(x1,y1,x2,y2):
    global l
    
    if x1 != x2 and y1 != y2 and abs(x1-x2) != abs(y1-y2):
        return False
    else:
        return True

l = [["*" for i in range(8)] for i in range(8)]

for i in range(len(l)):
    l[i].append("x")
    l[i] = ["x"] + l[i]

l.append(["x" for i in range(10)])
l = [["x" for i in range(10)]] + l

stek = [[1,1]]
visit = [[0 for i in range(len(l))] for i in range(len(l))]
visit[0][0] = 1

d = {}
for i in range(1,9):
    d[i] = chr(ord('a')+i)
    
while len(stek) > 0:
    x,y = stek[-1][0],stek[-1][1]
    fl = False
    
    for j in range(1,len(l)-1):
        hit_fl = False

        for m in range(len(stek)):
            if hit(stek[m][0],stek[m][1],len(stek)+1,j):
                hit_fl = True
                break
        
        if not hit_fl and visit[len(stek)-1][j-1] == 0:
            visit[len(stek)-1][j-1] = 1
            stek.append([len(stek)+1,j])
            fl = True
            break

    if len(stek) == 8:
        break
    
    if fl == False:
        stek.pop()
        
        for i in range(stek[-1][0],len(l)-1):
            for j in range(len(visit[i])):
                visit[i][j] = 0

for i in range(len(stek)):
    print(d[stek[i][0]] + str(stek[i][1]))
