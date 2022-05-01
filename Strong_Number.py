s=0  
n=int(input())  
temp=n 
while(n):  
    i=1  
    f=1  
    r=n%10  
    while(i<=r):  
        f=f*i   
        i=i+1  
    s=s+f  
    n=n//10  
if(s==temp):  
    print("The number",temp,"is a strong number")  
else:  
    print("The number",temp,"is not a strong number")  