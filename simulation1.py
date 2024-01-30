# print ('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if ((x==w) or not(y<=z) or x) ==0:
#                     print(x, y, z, w)
# for n in range (1,100):
#     s = bin(n)[2:]
#     sum=0
#     k=s
#     while int(k)>0:
#         dig=int(k)%10
#         sum+=dig
#         k=int(k)//10
#     s=s+str(sum%2)
#     sum=0
#     k=s
#     while int(k)>0:
#         dig=int(k)%10
#         sum+=dig
#         k=int(k)//10
#     s=s+str(sum%2)
#     r = int(s,2)
#     if r>70:
#         print(n)
#         break


# import itertools
# alphabet = "0123456"
# ar = itertools.permutations(alphabet, 5) #Размещение
# arl = []
# for e in ar:
#     arl.append(list(e))
# count = 0
# for e in arl:
#     flag = True
#     for i in range(len(e)-1):
#         if (e[0] == "0") or (int(e[i]) % 2 == 0 and int(e[i+1]) % 2 == 0) or (int(e[i]) % 2 != 0 and int(e[i+1]) % 2 != 0) or (e[-1]=="4") or (e[-1]=="5"):
#             flag = False
#     if flag:
#         count += 1
# print(count)

# n='3'*70
# while '333' in n or '888' in n:
#     if n.count('333')!=0:
#         n=n.replace('333','8')
#     if n.count('8')!=0:
#         n=n.replace('888','3')
# print(n)

# for x in '0123456789abcdef':
#     x1= str(x) + 'ad' + str(x)+str(x)
#     x2= '4'+str(x) + '32'
#     res = int(x1, 16) - int(x2, 16)
#     if res%9==0:
#         res=res/9
#         print(res)

# for A in range(300, -1, -1):
#     k = 0
#     for x in range(300):
#         for y in range(300):
#             if (x >=A) or (y+x <38) or (x <y-8):
#                 k += 1
#     if k == 90_000:
#         print(A)
#         break
n=3053
m=3052
s=1
k=1
while n>1:
    s=s*n
    n-=1
while m>1:
    k=k*m
    m-=1
print(s//k)