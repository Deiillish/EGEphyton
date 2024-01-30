# for s in range(100):
#     n=bin(s)[2::]
    
#     if s%2==0:
#         n=n+'00'
#     else:
#         n=n+'11'
#     r=int(n,2)
    
#     print(r)
        
        
# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if ((y<=w)==(x <= (not(z))) and (x or w)):
#                     if x+y+w+z<=2:
#                         print(x,y,z,w)
# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if not((y<=w)==(x <= (not(z))) and (x or w)):
#                     if x+y+w+z==3:
#                         print(x,y,z,w)
# def F(n):
#     s=''
#     while n>0:
#         s=str(n%3)+s
#         n//=3
#     return s
# for N in range(1,200):
#     s=F(N)
#     ost=F((N%3)*5)
#     if N%3!=0:
#         s=s+ost
#     r=(int(s,3))
#     if r>146:
#         print(N)
#         break

# for A in range(10000):
#     flag = True
#     for x in range(500):
#         if ((x&47!=0) <=  ((x&11==0)  <= (x&A!=0)))==0:
#             flag = False
#             break
#     print(A)
#     if flag:
#         print(A)
#         break

# for A in range(10000):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             if ((3*y +7*x<A) or (x>48)or(y>32))==0:
#                 flag = False
#                 break
#     print(A)
#     if flag:
#         print(A)
#         break
# P=[]
# for i in range(50,71):
#     P.append(i)

# for A in range(1,10000):
#     flag = True
#     for x in range(1,500):
#         if (((x%3==0)<=(x%5!=0))or(x+A>=90))==0:
#             flag = False
#             break
#     if flag:
#         print(A)
#         break
        
# a= 1456**89 + 57 * 45**21 + 9 * 13**12
# s=''
# while a>0:
#     s=str(a%3)+s
#     a//=3
# print(s.count('0'))
        
# m=0
# x='0123456789ABCD'
# for i in x:
#     if (int('A'+i+i+'B', 14) - int('C0'+i,14))%4==0:
#         print((int('A'+i+i+'B', 14) - int('C0'+i,14))/4)
# def F(n):
#     if n<3:
#         return n
#     if n>2 and n%2==0:
#         return F(n-2)+G(n-3)+A(n-1)
#     if n>2 and n%2!=0:
#         return F(n-1)+G(n-2)+A(n-3)
# def G(n):
#     if n<3:
#         return n-3
#     if n>2 and str(n)[-1]=='7':
#         return 3+G(n-2)+F(n-2)+A(n-2)
#     if n>2 and str(n)[-1]!='7':
#         return G(n-1)+F(n-2)+A(n-3)
# def A(n):
#     if n<3:
#         return n+1
#     if n>2:
#         return G(n-1)+F(n-1)+A(n-1)

# print(G(20))


# def F(x,y):
#     if x>y :
#         return 0
#     elif x==y:
#         return 1
#     else:
#         return F(x+3, y)+F(x*2+1,y)
# print(F(3,67)*F(67,159))


# k=0
# from itertools import product
# for x in product('ПИТОН',repeat=6):
#     if x.count('Н')<=1 and x[0]!='Т' and x[5]!='И' and x[5]!='О':
#         k+=1
# print(k)
# def to5(n):
#     s=''
#     while n>0:
#         s=str(n%9)+s
#         n=n//9
#     return s
# for x in range(10000,100000):
    
#     x=to5(x)
    
#     if x.count('3')==1:
#         if x.count('35')==0 and x.count('36')==0 and x.count('37')==0 and x.count('38')==0:
#             if x.count('53')==0 and x.count('63')==0 and x.count('73')==0 and x.count('83')==0:
#                 k+=1
#                 print(x)
# print(k)

# k=0
# from itertools import product
# for x in product('012345678',repeat=5):
    
#     if x.count('3')==1 and x[0]!='0':
        
#         x=''.join(x)
#         if x.count('35')==0 and x.count('36')==0 and x.count('37')==0 and x.count('38')==0:
#             if x.count('53')==0 and x.count('63')==0 and x.count('73')==0 and x.count('83')==0:
#                 k+=1
#                 if x[0]=='3':
#                     print(x)
# print(k)
k=0
c=0
from itertools import product
for x in product('АЖИМНУЧ',repeat=6):
    k+=1
    x=''.join(x)
    if x[0]!='Ж' and x.count('Ч')<=1 and k%2==0 :
        c+=1
print(c)