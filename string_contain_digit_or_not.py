string=input()
count=0
for i in string:
    if i.isdigit():
        count=count+1
if(count>0):
    print("Contains",count,"digit")
else:
    print("Doesn't contain digit")