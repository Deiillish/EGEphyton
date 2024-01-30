# print(int('11111000', 2))
# print(int('10101011', 2))
# print(int('10101000', 2))
# print(int('10110101', 2))

# print(bin(128)[2:])
# print(bin(224)[2:])
# print(bin(219)[2:])
# print(bin(192)[2:])

# адрес сети ищем из маски и ip
# print(220 & 255)
# print(8 & 255)
# print(232 & 224)
# print(250 & 0)
# 11******
# a=[]
# n=int(input())
# count=0
# for i in range(n):
#     a.append(int(input()))
# for i in range(len(a)-1):
#     if a[i]%10==0 and a[i+1]%10==0:
#         count+=1
# print(count)
a=[]
n=int(input())
count=0
max_n=0
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    if a[i]%5==0:
        max_n=max(max_n,a[i])
for i in range(len(a)-2):
    t=a[i]*a[i+1]*a[i+2]
    if a[i]%6==0 and a[i+1]%6==0 and a[i+2]%6==0 and t>=max_n:
        count+=1
print(count)
