n=int(input())
Sum=0
rem=0

Temp=n
while Temp>0:
    rem=Temp % 10
    Sum=Sum + rem
    Temp=Temp//10
if  n%Sum==0:
    print('True')
else:
    print('False')