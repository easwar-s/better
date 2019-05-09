class maximum:
 def __init__(self):
  self.n = int(input("Enter the n number"))
  self.arr = list(map(int,input("Enter the number:").split()))
 def larg(self):
  self.max = self.arr[o]
  for i in range(1,self.n):
   if self.arr[i] > self.max:
    self.max = self.arr[i]
  print("maximum number in given array is :",self.max)
m = maximum()
m.larg()
