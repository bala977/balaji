h5,m15= map(int, input().split())
h25,m25= map(int, input().split())
if(h5>h25):
    z=h5-h25
    y=m15-m25
    print(z,y)
else:
    t=h25-h5
    s=m25-m15
    print(t,s)
