for _ in range(int(input())):
    t=1
    a=int(input())
    for i in range(2,a+1):
        if(i%2!=0):t=t&i
        else:t=t^i
    print(t)