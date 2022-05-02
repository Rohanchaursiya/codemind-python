n=int(input())
j=n-1
for i in range(1,n+1):
    print(" "*j,end="")
    print(10**(2*i-1)//9 *i)
    j-=1