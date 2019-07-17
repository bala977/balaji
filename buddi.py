#B
am,pm,fm=map(int,input().split())
sinduja=int(am)*int(pm)
carth=int(sinduja)%fm
print(round(carth))
