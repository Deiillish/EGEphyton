x=18**105+25*16**100-31**51
a=0
c=1
while x!=0:
    b=x%16
    if b>a:
        a=b
        c=1
    elif a==b:
        c+=1
    x=x//16
print(c)