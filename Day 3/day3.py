import re
import numpy as np

def mapdata():
    with open("C:\Box Sync\Luuk Leeuwenstein\LL. Misc\Codings\AdventOfCode2018\Day 3\input.txt") as file:
        data = file.readlines()
        # Mapping used from answer of u/mserrano on Reddit
        claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
        return claims

def mapfunc(claims):
    canvas = np.zeros((1000,1000)) # Based on solution with Numpy of u/cole-k on Reddit
    for claim in claims:
        x,y,xw,yh = claim[1],claim[2],claim[3],claim[4]
        canvas[x:x+xw, y:y+yh] += 1
    return canvas

def findsingleclaim(canvas, claims):
    for claim in claims:
        x,y,xw,yh = claim[1],claim[2],claim[3],claim[4]
        if (canvas[x:x+xw, y:y+yh] > 1).any():
            continue
        else:
            return claim[0]

claims = mapdata()
canvas = mapfunc(claims)
# Solution p1: print (np.size(np.where(canvas >= 2)[0]))
print(findsingleclaim(canvas, claims))