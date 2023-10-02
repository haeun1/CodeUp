n = int(input())
a = list(map(int,input().split()))
b = [0]*23 #1차원 배열 0으로 초기화
for i in a:
    b[i-1] += 1
for i in b:
    print(i,end=" ")