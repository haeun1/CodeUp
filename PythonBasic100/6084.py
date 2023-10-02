h,b,c,s = map(int,input().split())
space = h*b*c*s/8
space = space/1024/1024
print(round(space,1),"MB")
#print(format(space,".1f"),"MB")