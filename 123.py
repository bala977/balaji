balaji3=int(input())
bala=list(map(int,input().split()[:balaji3]))
bala.sort()
for i in bala:
  print(i,end=" ")
