"""
SPECIFICATON:

What This Program Will Do:
It will attempt to solve a weighing problem that asks for
the least number of weights required to weigh any integral
number of pounds up to 63 pounds if one is allowed to put 
weights in only one pan of a balance.
"""
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                for e in (0, 1):
                    for f in (0, 1):
                        for g in (0, 1):
                            if 23 == g*64 + f*32 + e*16 + d*8 + c*4 + b*2 + a:
                                print(g, f, e, d, c, b, a)