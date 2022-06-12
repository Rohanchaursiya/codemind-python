s=input()
words=s.split(' ')
words=words[-1::-1]
os=" ".join(words)
print(os)