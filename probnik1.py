def f(x, y, h):
    if h == 1 and x + y >= 41:
        return 1
    if h == 1 and x + y < 41:
        return 0
    if h < 1 and x + y >= 41:
        return 0
    else:
        if h % 2 == 0:
            if x > y:
                return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x + 3, y, h + 1) or f(x, y * 2, h + 1)
            elif x < y:
                return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y + 3, h + 1) or f(x * 2, y, h + 1)
            elif x == y:
                return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x + 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y + 3, h + 1)
        else:
            if x > y:
                return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x + 3, y, h + 1) or f(x, y * 2, h + 1)
            elif x < y:
                return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y + 3, h + 1) or f(x * 2, y, h + 1)
            elif x == y:
                return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x + 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y + 3, h + 1)
a = set()
for x  in range(1, 20):
    for y in range(1, 20):
        if f(x, y, 0) == 1:
            a.add(x + y)
print(min(a))