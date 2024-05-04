def defincelineplace(mazesize):
    lineplace={}
    lineplaceindex=[]
    for i in range(12):
        lineplaceindex.append(0)
    lineplace.update({0:lineplaceindex})
    return lineplace

testlineplace=defincelineplace(4)
print(testlineplace)
print(testlineplace[0])
print(testlineplace[1])
print(testlineplace[2])
print(testlineplace[3])