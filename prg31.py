import re
c=0
k=input()
for i in k:
  if i.isdigit() or i.isalpha() or re.findall('[r"^@#$%&*)(!"]',i):
    c=c+1
print(c) 
