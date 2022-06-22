def addDigits(n):
    while(n>=10):
        temp=0
        while(n>0):
            temp=temp+n%10
            n=n//10
        n=temp
    return n
n=int(input())
print(addDigits(n))