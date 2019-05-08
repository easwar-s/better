class mul:
 def __init__(self):
  self.n = int(input("Enter the n number"))
  self.m = 5
 def cal(self):
  self.a = range(self.n,(self.n*self.m)+1,self.n)
  print(self.a)
m = mul()
m.cal()
