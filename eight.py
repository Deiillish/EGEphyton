# m_r=0
# for N in range(1,100):
#     N2=bin(N)[2:]
#     if N2.count('1')%2==0:
#         N2='11'+N2[2:]+'10'
#     else:
#         N2='11'+N2[2:]+'01'
    
#     R=int(N2,2)
#     if R<=350 and R%2!=0:
#         m_r=max(m_r,R)
# print(m_r)

def tr(n):
    res=''
    while n>0:
        d=str(n%3)
        n=n//3
        res=d+res
    return res

for N in range(9, 300):
    N3=tr(N)
    if N%3==0:
        N3=N3+N3[-3:]
    else:
        N3=N3+tr(N%3*3)
    R=int(N3,3)
    if R>=370:
        print(N)
        break