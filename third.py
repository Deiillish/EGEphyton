n=int(input())
a=[]
while(n>0):
    a.append(n%3)
    n=n//3

a.reverse()
e=("".join(map(str, a)))
c=str(e.count('2'))
print(e, c)