s=input()
for i in range(len(s)):
    if s[i]=='6':
        break
t="9"
s=s[0:i]+t+s[i+1:]
print(s)
