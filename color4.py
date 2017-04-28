"""
теорема четырех красок [1,2,3,4]
"""
region = ((0, 0, 2, 3), (0, 1, 2, 3), (0, 1, 1, 3), (0, 0, 0, 0), (1, 0, 3, 2))
region = ((1,1,1,2,1,1,),(1,1,1,1,1,1,),(1,1,0,1,1,1,),(1,0,0,0,1,1,),(1,1,0,4,3,1,),(1,1,1,3,3,3,),(1,1,1,1,3,5,))
region = ((0),)
region = ((0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),)
region = ((11,0,0,0,0,0,7,0,),(0,0,0,0,0,0,7,0,),(0,0,4,4,4,0,7,0,),(0,0,0,0,0,0,0,0,),(0,0,1,0,1,0,0,0,),(5,5,1,2,1,6,6,0,),(0,0,1,0,1,0,0,0,),(0,0,0,0,0,0,0,0,),(0,0,3,3,3,0,8,0,),(0,0,10,10,9,0,8,0,),(0,0,0,10,9,9,8,0,),)
region = ((0,0,0,),(0,1,1,),(0,0,2,))
region = ((0,0,0,0,0,0,0,0,0,0,),(0,1,1,1,1,1,1,1,1,0,),(0,1,0,0,0,0,0,0,1,0,),(0,1,0,6,0,8,10,0,1,0,),(0,1,0,5,0,7,9,0,1,0,),(0,1,0,0,4,0,0,0,1,0,),(0,1,0,3,0,2,2,0,1,0,),(0,1,0,3,0,2,11,0,1,0,),(0,1,0,0,0,0,0,0,1,0,),(0,1,1,1,1,1,1,0,1,0,),(0,0,0,0,0,0,0,0,0,0,),)
region = ((0, 0, 0),(0, 1, 1),(0, 0, 2),)
region = ()
region = ((7,4,4,4,),(7,0,1,5,),(7,2,3,5,),(6,6,6,5,),)
region = ((13,13,13,13,13,13,14,14,14,14,),(13,0,0,1,1,2,2,3,3,14,),(13,4,5,5,6,6,7,7,8,14,),(13,9,9,10,10,11,11,12,12,14,),(13,13,13,13,14,14,14,14,14,14,),)
color = [1,2,3,4]

poleRowColumn = []
if (len(region) >= len(region[0])):
    for i in range(len(region)):
        if isinstance(region[i], int):
            poleRowColumn.append(list([region[i]]))
        else:
            poleRowColumn.append(list(region[i]))
            if (i <= len(region[i])-1):
                poleRowColumn.append([row[i] for row in region])
else:
    for i in range(len(region[0])):
        if (i < len(region)):
            poleRowColumn.append(list(region[i]))
        poleRowColumn.append(list([row[i] for row in region]))

neighborhood = dict()
countrys = set()
result = []
for row in poleRowColumn:
    if (len(row) - 1 > 0):
        for j in range(len(row) - 1):
            if (row[j] == row[j+1] and len(countrys) > 0):
                continue
            countrys.add(row[j])
            countrys.add(row[j+1])
            try:
                if row[j+1] not in neighborhood[row[j]]:
                    neighborhood[row[j]].append(row[j+1])
            except KeyError:
                neighborhood[row[j]] = [row[j+1]]

            try:
                if row[j] not in neighborhood[row[j+1]]:
                    neighborhood[row[j+1]].append(row[j])
            except KeyError:
                neighborhood[row[j+1]] = [row[j]]
    else:
        for j in row:
            if (len(neighborhood) <= 0):
                neighborhood[row[j]] = [row[j]]
            if row[j] in neighborhood[row[j]]:
                continue
            neighborhood[row[j]] = [row[j]]

sorted(neighborhood, key=lambda k: len(neighborhood[k]), reverse=True)
currentColor = 0
colorCountry = dict()
for i in neighborhood:
    flag = False
    for idxColor in colorCountry:
        currentColor = idxColor
        diff = [x for x in neighborhood[i] if x in (colorCountry[idxColor]) and x != i]
        if len(diff)<=0:
            flag = True
            break
    if not flag:
        currentColor = currentColor + 1
        if currentColor  not in colorCountry.keys():
            colorCountry[currentColor] = []

    if i not in colorCountry[currentColor]:
        colorCountry[currentColor].append(i)

invertCountryColor = {}
for i in colorCountry:
    for j in colorCountry[i]:
        invertCountryColor[j]=i
result = []
sd = sorted(invertCountryColor.items())

for k,v in sd:
    result.append(v)

print (result)