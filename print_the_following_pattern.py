n=int(input())
for i in range(n):
    for j in range(n-i):
        print(chr(n-i+64),end=" ")
    print()