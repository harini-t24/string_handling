s=input("Enter a string:")
result=""
for i in range(0,len(s),2):
    ch=s[i]
    num=int(s[i+1])
    result=result+ch*num
print(result)
