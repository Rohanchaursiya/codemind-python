s=input()
b='_+-*&^%$#@!={}[]()|:~`?/.<,>'
c=0
for i in s:
    if i in b:
        c+=1
print(c)