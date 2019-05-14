def div(num,m):
    if(num&((1<< m)-1))==0:
        return True
    return False
num=8
m=2
if div(num,m):
    print("yes")
else:
    print("no")
