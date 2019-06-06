a=int(input())
b=list(map(int,input().split()))
b.sort()
x=(b[0]+b[a-1])//2
print(x)
