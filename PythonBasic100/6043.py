f1,f2 = map(float,input().split())
#print(round((f1/f2),3)) #10.000으로 나오진 않고 10.0으로 나옴
print(format(f1/f2,".3f")) #10.000으로 정확하게 세리를 맞추고 싶으면 이렇게 