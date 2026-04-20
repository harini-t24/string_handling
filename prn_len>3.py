a=input("Enter a string:")
words=a.split()
for w in words:
    if len(w)>5:
        print(w)
