# from functools import lru_cache
# def moves(h):
#     a,b=h
#     return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
# @lru_cache(None)
# def game(h):
#     a,b=h
#     if a+b>=83: return "W"
#     if any(game(m)=='W' for m in moves(h)):return "P1"
#     if all(game(m)=='P1' for m in moves(h)):return "B1"
#     if any(game(m)=='B1' for m in moves(h)):return "P2"
#     if all(game(m)=='P1' or game(m)=='P2' for m in moves(h)):return "B2"

# for s in range(1,200):
#     h=9,s
#     if game(h)=="B2":
#         print(s,game(h))
cnt=0
from functools import lru_cache
def moves(h):
    x, last = h
    a = []
    if last !='+1': a.append((x+1,'+1'))
    if last !='+2': a.append((x+2,'+2'))
    if last !='*3': a.append((x*3,'*3'))
    return a
@lru_cache(None)
def game(h):
    x,last= h
    if x>=140: return "W"
    if any(game(m)=='W' for m in moves(h)):return "P1"
    if all(game(m)=='P1' for m in moves(h)):return "B1"
    if any(game(m)=='B1' for m in moves(h)):return "P2"
    if all(game(m)=='P1' or game(m)=='P2' for m in moves(h)):return "B2"

for s in range(1,200):
    h=s,'-1'
    if game(h)=="B2":
        print(s,game(h))


def Div(n):
    for i in range(2, int(n**0.5)+1):
                   if n % i ==0:
                       return False
    return True
mins=1000000
for x in range(100):
    for y in range(100):
        s='0'+'1'*x+'2'*y
        if len(s)>40:
            while ('01' in s) or ('02' in s):
                s=s.replace('02','1110')
                s=s.replace('01','220')
            if Div(s.count('1')+s.count('2')*2):
                    mins=min(mins, x+y*2)
print(mins)
