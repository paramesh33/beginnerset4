data=[];
n=int(input());
k=int(input());
for x in range(n):
    a=input();
    data.append(int(a));
data.sort();
print(data(k-1));
