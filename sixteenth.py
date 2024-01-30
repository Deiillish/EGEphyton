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
