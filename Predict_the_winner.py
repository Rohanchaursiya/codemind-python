n=int(input())
l=list(map(int,input().split()))
temp=0
sum=0
for i in range(n//2):
    temp=temp+l[i]
    sum=sum+l[n//2+i]
if abs(temp-sum)%4!=0:
    print("Y")
else:
    print("X")