n=int(input())
x=0
while(1):
    c=x*(x-1)
    if(c>n):
        print("NO")
        break
    elif(c==n):
        print("YES")
        break
    x=x+1