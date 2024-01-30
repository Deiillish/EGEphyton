# count=kol=summa=max_n=0

# f = open('17.txt')
# l = [int(i) for i in f]
# for i in range(len(l)):
#     if (l[i])%2!=0:
#         summa+=l[i]
#         kol+=1
# summa//=kol
# k=0
# for i in range(len(l)-1):
#     a=l[i]
#     b=l[i+1]
#     if (a%5==0 and b<summa) or (a<summa and b%5==0) :
#         k += 1
#         max_n = max(max_n, (l[i]+l[i+1]))
# print(k, max_n)

# max_n=0
# f = open('17.txt')
# l = [int(i) for i in f]
# k=0
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i]*l[j]%62==0:
#             k += 1
#             max_n = max(max_n, (l[i]+l[i+1]))
# print(k, max_n)

# max_n=0
# f = open('17.txt')
# l = [int(i) for i in f]
# k=0
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i]-l[j])%45==0 and (l[i]%18==0 or l[j]%18==0):
#             k += 1
#             max_n = max(max_n, abs(l[i]-l[j]))
# print(k, max_n)

# max_n=0
# f = open('17.txt')
# l = [int(i) for i in f]

# k=0
# for i in range(len(l)-1):
#     for j in range(i+1, len(l)):
#         if (l[i] % 160 != l[j]%160) and ((l[i]%7==0) or (l[j]%7==0)):
#             k += 1
#             max_n = max(max_n, (l[i]+l[j]))
# print(k, max_n)

# f=open('17.txt')
# l=[int(i) for i in f]
# k=0
# m=0
# for i in range(0, len(l)-1):
#     for j in range(i+1, len(l)):
#         if ((l[i]+l[j])%10==0):
#             k+=1
#             m=max(l[i]+l[j], m)
# print(k, m)

