ji=int(input())
temp=ji
sum=0
while ji>0:
    d=ji%10
    sum=sum+d**3
    ji=ji//10
    if sum==temp:
        print("yes")
        break
else:
    print("no")
