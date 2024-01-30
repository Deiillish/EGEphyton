# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# for n in range(1,100):
#     x='>'+'0'*23+'1'*18+'2'*n
#     c=0
#     while '>0' in x or '>1' in x or '>2' in x:
#         if '>0' in x:
#             x=x.replace('>0','22>',1)
#         if '>1' in x:
#             x=x.replace('>1','2>',1)
#         if '>2' in x:
#             x=x.replace('>2','23>',1)
#     for i in range(len(x)):
#         if x[i]!='>':
#             c+=int(x[i])
#     if is_prime(c)==True:
#         print(n)
#         break
    

# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
e=1
for n in range(4,10000):
    x='1'+'9'*n
    c=0
    while '19' in x or '49' in x or '999' in x:
        if '19' in x:
            x=x.replace('19','9',1)
        if '49' in x:
            x=x.replace('49','91',1)
        if '999' in x:
            x=x.replace('999','4',1)
    for i in range(len(x)):
        c+=int(x[i])
    e=max(e,c)
print(e)    
    
