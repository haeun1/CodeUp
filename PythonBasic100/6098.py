m = []
for _ in range(10):
    m.append(list(map(int, input().split())))

i = 1
j = 1
m[i][j] = 9 

while True:
    if m[i][j+1] == 0:
        j += 1
        m[i][j] = 9
    elif m[i][j+1] == 2:
        j += 1
        m[i][j] = 9
        break
    else:
        if m[i+1][j] == 0:
            i += 1 
            m[i][j] = 9 
        elif m[i+1][j] == 2:
            i += 1 
            m[i][j] = 9 
            break    
        else:
            break
       

for i in range(10):
    for j in range(10):
        print(m[i][j],end=" ")
    print()