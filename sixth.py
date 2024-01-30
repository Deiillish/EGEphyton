# for n in range(1,100):
#     s=bin(n)[2:]
#     if s.count('1')%2==0:
#         s=s+'0'
#     else:
#         s=s+'1'
#     if s.count('1')%2==0:
#         s=s+'0'
#     else:
#         s=s+'1'
#     r=int(s,2)
#     if r>137:
#         print(n)
#         break

# for n in range(1,100):
#     s=bin(n)[2:]
#     s= s + str(s.count('1')%2)
#     s= s + str(s.count('1')%2)  
#     r=int(s,2)
#     if r<89:
#         e=r
#     else:  
#         print(e)
#         break

# for n in range(1,100):
#     s=bin(n)[2:]
#     if n%2==0:
#         s=s+'01' 
#     else:
#         s=s+'10'
#     r=int(s,2)
#     if r>87:
#         print(n)
#         break

# a=int(input())
# b=int(input())
# def f(a,b):
#     c=(a**2+b**2)**(1/2)
#     p = a + b + c
#     s= a*b/2
#     return p,s
# print(f(a,b))

# def F(n):
#     if n==1 :
#         return 1
#     elif n==2:
#         return (2)
#     elif n==3:
#         return (3)
#     elif n>3:
#         return (F(n-3)+F(n-2))
# n=int(input())
# print(F(n))

# def F(n):
#     if n==1 or n==2:
#         return n
#     elif n>2:
#         return (F(n-1) + 2*G(n-2))
# def G(n):
#     if n==1 or n==2:
#         return n
#     elif n>2:
#         return (2*G(n-1) + F(n-2))
# n=int(input())
# print(F(n))
    
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n>=5172:
        return 3*n
    elif n<5172:
        return (2*n + F(n+2))
print(F(5120)-F(5130)+F(5110))