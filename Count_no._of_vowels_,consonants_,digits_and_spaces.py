s=input()
sp=0
vo=0
co=0
d=0
v='aeiou'
for i in range(len(s)):
    if(s[i]==' '):
        sp+=1
    elif s[i] in v:
        vo+=1
    elif s[i].isdigit():
        d+=1
    else:
        co+=1
print("Vowels:",vo)
print("Consonants:",co)
print("Digits:",d)
print("White spaces:",sp)