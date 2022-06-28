n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
s=0
for i in a:
    if(i>1):
        for j in range(2,i//2+1):
            if(i%j==0):
                break
        else:
            c+=1
            b+=[i]
for k in b:
    s+=k
print("%0.2f"%(s/c))