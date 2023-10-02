c , d = map(int,input().split())
print(bool((c and (not d)) or ((not c) and d)))