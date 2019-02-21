N=int(input());
count=0;
for x in range(1,10):
  if N==x:
    count=count+1;
if count==1:
    print("yes");
else:print("no");
