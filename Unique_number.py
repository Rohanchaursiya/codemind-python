n=input()
for i in n:
    s=0
    for j in n:
        if(i==j):
            s=s+1
    if(s==2):
        print("Not Unique Number")
        break
else:
    print("Unique Number")