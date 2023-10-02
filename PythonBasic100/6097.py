h, w = map(int,input().split())
arr = [[0]*w for _ in range(h)]

n = int(input())
for _ in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for i in range(l):
            arr[x-1][y-1+i] = 1
    else:
        for i in range(l):
            arr[x-1+i][y-1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=" ")
    print()

