by=input()
oi=0
for i in range(len(by)):
    if (by[i].isalpha() or by[i].isnumeric() or by[i]==" "):
      continue
    oi=oi+1
else:
    print(oi)
