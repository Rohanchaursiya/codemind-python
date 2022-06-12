def sum_of_string(s):
    sum=0
    for i in s:
        if i.isdigit():
            sum=sum+int(i)
    return sum
s=input("")
print(sum_of_string(s))