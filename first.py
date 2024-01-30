# def F(n):
#     if n==1:
#         return 1
#     if n>1:
#         return F(n-1)+(n+1)
# print(F(6))



# n='>'+'1'*15+'2'*20+'3'*16
# while n.count('>1')!=0 or  n.count('>2')!=0 or n.count('>3')!=0:
#     if n.count('>1')!=0:
#         n=n.replace('>1','22>')
#     if n.count('>2')!=0:
#         n=n.replace('>2','2>')    
#     if n.count('>3')!=0:
#         n=n.replace('>3','1>')
# print(n)

a=int(input())
if a==1 or a==2 or a==12:
    print('зима')
elif a==3 or a==4 or a==5:
    print('весна')
elif a==6 or a==7 or a==8:
    print('лето')
elif a==9 or a==10 or a==11:
    print('осень')