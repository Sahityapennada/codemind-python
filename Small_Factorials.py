n = int(input())
while n:
    n-=1
    x=int(input())
    b=1
    while x!=1:
        b*=x
        x-=1
    print(b)