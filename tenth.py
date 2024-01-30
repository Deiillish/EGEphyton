# print(int('10011010', 2))
# print(int('10101011', 2))
# print(int('10101000', 2))
# print(int('10110101', 2))

# print(bin(192)[2:])
# print(bin(224)[2:])
# print(bin(219)[2:])
# print(bin(192)[2:])

# адрес сети ищем из маски и ip
# print(224 & 255)
# print(24 & 255)
# print(254 & 224)
# print(134 & 0)
# 11******


# N=int(input())
# k=0
# a=[int(input()) for i in range (N)]
# for i in range(N-1):
#     if (a[i]+a[i+1])%2==0:
#         k+=1
# print(k)

# N=int(input())
# a=[int(input()) for i in range(N)]
# m_ch=0
# for i in range(N):
#     if a[i]%3==0:
#         m_ch=max(m_ch, a[i])
# k=0
# m_ch%=10
# for i in range(N-1):

#     if a[i]%10==m_ch and a[i+1]%10==m_ch:
#         k+=1
# print(k)

N=int(input())
a=[int(input()) for i in range(N)]
m_6=0
for i in range(N):
    if a[i]%6==0:
        m_6=min(m_6, a[i])
k=0

for i in range(N-1):

    if (a[i]+a[i+1]<m_6) and (abs(a[i])%10 ==9 or abs(a[i+1])%10 ==9):
        k+=1
print(k)