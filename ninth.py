# arr=[]
# r=0
# for i in range(5):
#     n=int(input())
#     if n>0 and n%3==0:
#         arr.append(n)
# for j in range(len(arr)):
#     r=max(r,arr[j])
# print(r)

# arr=[]
# r=0
# n=int(input())
# for i in range(n):
#     arr.append(int(input()))
# for j in range(len(arr)):
#     if arr[j]%7==0 and arr[j]>0:
#         r+=j
# print(r)

# alf='0123456789ABCDEFG'
# for x in alf:
#     a=int('17'+x+'17', 17)
#     b=int(x+'17'+x, 17)
#     c=a-b
#     if c%9==0:
#         print(x)

alf='0123456789ABCDEFGHIJKLM'
for x in alf:
    c=int('348'+x+'79643', 23)+int('16'+x+'52', 23)+int('43'+x+'7',23)
    if c%12==0:
        print(x)
