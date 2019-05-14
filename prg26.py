n = int(input())
ls = list(map(int,input().split()))
ls.sort()
for i in range(len(ls)):
 if i == len(ls)-1:
  print(ls[i],end="")
 else:
  print(ls[i],end="")
