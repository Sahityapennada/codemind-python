n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if(i==j):
            print(i,end=' ')#gap
        elif(j==n-i+1):
            print(i,end=' ')#gap
        else: 
            print(" ",end='')#only one gap
    print()