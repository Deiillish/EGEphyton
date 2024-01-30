# P=[i for i in range(30, 51)]
# for A in range(1,1000):
#     f=True
#     for x in range(1,1000):
#         if not((x%4==0)or (x in P) <= (x+A>=60)):
#             f=False
#             break
#     if f:
#         print(A)
#         break


# for A in range(1000):
#     f=True
    
#     for x in range(1000):
        
#         if not((x & 25 !=0) <=((x & 17==0)<=(x&A!=0))):
#             f=False
#             break
#     if f:
#         print(A)
#         break

# for n in range(1,200):
#     n2=bin(n)[2:]
    
#     if n2.count('1')%2!=0:
#         n2='10'+n2[2:]+'1'
#     else:
#         n2='11'+n2[2:]+'0'
#     r=int(n2,2)
#     if r>=41:
#         print(n)
#         break
# m=0
# for A in range(1,1000):
#     flag=True
#     for x in range(1,500):
#         if not((A<50) and ((not(x%A==0))<=((x%10==0)<=(not(x%12==0))))):
#             flag=False
#             break
#     if flag:
#         m=max(A,m)
# print(m)
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n<11:
        return (n)
    if n>=11:
        return (n +F(n-1))
print(F(2024)-F(2021))