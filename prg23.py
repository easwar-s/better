class minimum:
 def __init__(self):
  self.n = int(input("Enter the N number"))
  self.arr = list(map(int,input("Enter the number:").split()))
 def low(self):
  self.max = self.arr[0]
  for i in range(1,self.n):
   if self.arr[i]<self.max:
    self.max = self.arr[i]
  print("minimum number in given array is:",self.max)
m = minimum()
m.low()
