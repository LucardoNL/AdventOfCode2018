import re

def mapdata():
    with open("C:\Box Sync\Luuk Leeuwenstein\LL. Misc\Codings\AdventOfCode2018\Day 3\input.txt") as file:
        data = file.readlines()

        # Mapping used from answer of u/mserrano on Reddit
        claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
        return claims

def patchmapper(claims):
    #patchmap = [{'xy': (int, int)}]
    match = 0
    coordinatelist = [[int, int]]
    for (id, xstart, ystart, width, height) in claims:
        for x in range(xstart, xstart+width):
            for y in range(ystart, ystart+height):
                if (x, y) not in coordinatelist:
                    coordinatelist.append((x,y))
                else:
                    match += 1
        coordinatelist.sort()
        print("Claim: "+ str(id) +"\r")               
    return match

print(patchmapper(mapdata()))