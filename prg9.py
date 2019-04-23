x,y=[int(x) for x in input().split()]
for i in range(1,x+1):
 print(i,end='')
 sum = 0
 for j in range(1,y+1):
  sum = sum+j
print("\n",sum)
