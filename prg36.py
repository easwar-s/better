str=input("Enter the string")
count=0
for i in str:
    if((i >= chr(58) and i <= chr(64)) or (i >= chr(33) and i <= chr(47)) or (i >= chr(91) and i <= chr(96))):
        count+=1
    else:
        continue

print (count)  
