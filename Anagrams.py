s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
c=0
for i in s3:
    if i in s4:
        c+=1
if(c==len(s3)):
    print('True')
else:
    print('False')