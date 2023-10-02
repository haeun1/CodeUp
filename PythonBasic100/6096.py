def flip(i,j,m):
    for k in range(19):
        if m[i-1][k] == 0:
            m[i-1][k] = 1 
        else:
            m[i-1][k] = 0
        if m[k][j-1] == 0:
            m[k][j-1] = 1
        else:
            m[k][j-1] = 0

def arrPrint(m):
    for i in range(19):
        for j in range(19):
            print(m[i][j],end=" ")
        print()


#파이썬의 메인함수
if __name__ == '__main__':
    m = []
    for _ in range(19):    
        m.append(list(map(int,input().split())))
    n = int(input())

    for _ in range(n):
        i, j = map(int,input().split())
        flip(i,j,m)

    arrPrint(m)

