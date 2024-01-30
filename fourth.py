# print("x y z w")
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if(not(x) or y or (not(z) and w))==0:
#                     print(x,y,z,w)

# print("x y z w")
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if(z or not(x) or not(y<=w))==0:
#                     print(x,y,z,w)
# a=int(input())
# b=int(input())
# c=int(input())
# if a<=b and a<=c:
#     print(a)
# elif b<=a and b<=c:
#     print(b)
# elif c<=a and c<=b:
#     print(c)

# n=int(input())
# a=[]
# for i in range (n):
#     i=int(input())
#     if i%5==0 and i%10!=0:
#         a.append(i)
# if len(a)>0:
#     print(max(a))
# else:
#     print(-1)

# n=int(input())
# b=0
# a=[]
# c=[]
# for i in range (n):
#     i=int(input())
#     b=b+i
#     if i%2==0:
#         a.append(i)
#     else:
#         c.append(i)
# if b == max(a) * min(c):
#     print('повезло')
# else:
#     print('в следующий раз')

# print("x y z w")
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#                 for w in range(0,2):
#                     if((not(x) and not(y)) or (y==z) or w)==0:
#                         print(x,y,z,w)
# def F(n):
#     if n<=2:
#         return(3*n+6)
#     elif n>2 and n%2==0:
#         return(F(n-2)+2*F(n-1))
#     elif n>2 and n%2!=0:
#         return(10+F(n-4))

# print( F(18))

F(n)