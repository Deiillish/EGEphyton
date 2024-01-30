# def F(n):
#     if n<=2:
#         return(3*n+6)
#     elif n>2 and n%2==0:
#         return(F(n-2)+2*F(n-1))
#     elif n>2 and n%2!=0:
#         return(10+F(n-4))

# print( F(18))

# def F(n):
#     if n<3:
#         return n+9
#     else:
#         return 2*F(n-1)+3*G(n-2)
# def G(n):
#     if n<4:
#         return 25-n
#     else:
#         return 4*G(n-1) - F(n-2)
# print(G(13))

import sys
sys.setrecursionlimit(10000)
def F(n):
    if n==0:
        return 1
    elif n>0:
        return 3*F(n-1)
print(F(3100)//F(3090))