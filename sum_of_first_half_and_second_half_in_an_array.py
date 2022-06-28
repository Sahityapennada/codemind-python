n=int(input())
s=list(map(int,input().split()))
c,h=0,0
for i in range(n//2):
    c+=s[i]
for j in range(n//2,n):
    h+=s[j]
print(c)
print(h)