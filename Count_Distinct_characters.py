n=input()
n=n.lower()
n=list(n)
k=n.copy()
k=set(k)
k=list(k)
if(k.count(" ")>=1):
    c=k.index(" ")
    k.pop(c)
    print(len(k))
else:
    print(len(k))