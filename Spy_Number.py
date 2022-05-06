Number = int(input())
Temp = Number
Sum = 0
prod = 1

while Temp > 0:
    rem = Temp % 10
    Sum = Sum + rem
    prod = prod * rem
    Temp = Temp // 10

if Sum == prod:
    print('Spy Number')
else:
    print('Not Spy Number')