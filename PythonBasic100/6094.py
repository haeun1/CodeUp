n = int(input())
a = list(map(int,input().split()))
#print(min(a))
min = a[0]
for i in range(1,len(a)):
    if min > a[i]:
        min = a[i]
print(min)