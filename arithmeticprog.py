class arith:
 def __init__(self):
  self.a = int(input("Enter the starting number:"))
  self.d = int(input("Enter common difference number:"))
  self.n = int(input("Enter the N term to find:"))
 def cal(self):
  self.res = (self.a+(self.n-1)*self.d)
  print("the N th term of the series is:",self.res)
a = arith()
a.cal()
