la,ba=map(int,input().split())
for i in range(la+1,ba):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
              print(i,end=' ')
