# s1 = 'Карл у Клары украл кораллы'
# s2 = 'А Клара у Карла украла кларнет'
# print(s1.count('к') + s2.count('л'))

# def F(start, end):
#     if start> end or start==31:
#         return 0
#     elif start==end:
#         return 1
#     else:
#         return F(start+1, end)+F(start*1.5, end)
# print(F(2,56))

# def F(start, end):
#     if start> end :
#         return 0
#     elif start==end:
#         return 1
#     else:
#         return F(start+2, end)+F(start*2, end)
# print(F(4,14)*F(14,68))
def N(start):
    x=str(start)[0]
    if x==9:
        return(0)
    else:
        start+=10
        return start
def F(start, end):
    if start> end :
        return 0
    elif start==end:
        return 1
    else:
        return F(start+1, end)+F(N(start), end)
print(F(10,43))