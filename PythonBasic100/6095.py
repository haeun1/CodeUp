def arrPrint(arr):
    for i in range(19):
        for j in range(19):
            print(arr[i][j],end=" ")
        print()

n = int(input())
#2차원 배열 0으로 초기화
a = [[0]*19 for _ in range(19)]

for _ in range(n):
    i, j = map(int,input().split())
    a[i-1][j-1]=1

arrPrint(a)
