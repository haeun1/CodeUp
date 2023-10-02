w, h, b = map(int,input().split())
space = w*h*b/8/1024/1024
print(format(space,".2f"),"MB")
#print(round(space,3),"MB")