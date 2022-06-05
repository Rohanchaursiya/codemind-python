
n=int(input())
a=list(map(int,input().split()))
temp=[]
for element in a:
    if(element not in temp):
        temp.append(element)
a=temp
print(*a)