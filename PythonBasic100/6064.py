a,b,c = map(int,input().split())
print( (a if(a<b) else b) if ((a if(a<b) else b)<c) else c )

# min = a
# if a < b:
#     if a < c:
#         pass
#     else:
#         min = c
# else:
#     if b < c:
#         min = b
#     else:
#         min = c
# print(min)
