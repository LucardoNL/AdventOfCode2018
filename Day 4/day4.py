def getinput():
    with open('D:\Werk\Coding\AdventOfCoding\Day 4\input.txt') as raw:
        inputdata = raw.readlines()
        mappeddata = parser(inputdata)
        return mappeddata

def parser(inputdata):
    mappeddata = []
    for line in inputdata:
        guard = ''
        timestamp = line[1:17]
        if line[19] == 'G':
            try:
                guard = int(line[26:30])
            except:
                guard = int(line[26:29])
            action = 'starts'
        else:
            action = line[19:24] 
        mappeddata.append((timestamp, guard, action))
    return mappeddata

print(getinput())