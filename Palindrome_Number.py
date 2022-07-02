def rev(a):
    re=0
    while a>0:
        r=a%10
        re=(re*10)+r
        a//=10
    return re
t=int(input())
for i in range(t):
    a=int(input())
    if rev(a)==a:
        print("True")
    else:
        print("False")