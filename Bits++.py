a=int(input())
n=0
for i in range(a):
    s=input()
    if(s[1]=='+'):
        n+=1
    else:
        n-=1
print(n)