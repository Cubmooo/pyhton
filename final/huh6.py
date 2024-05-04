def defincelineplace(mazesize):
    lineplace={}
    lineplaceindex=[]
    gh=0
    while gh!=mazesize:
        lineplaceindex=[]
        print("test")
        for i in range(mazesize*3):
            lineplaceindex.append(0)
        print(lineplaceindex)
        lineplace.update({gh:lineplaceindex})
        gh+=1
    return lineplace

testlineplace=defincelineplace(4)
print(testlineplace)
print(testlineplace[0])
print(testlineplace[1])
print(testlineplace[2])
print(testlineplace[3])

directionss=[0,1,2,3,7,11,15,14,13,12,8]
location=0
import math


for i in directionss: # runs through the directions turning it into the line place format
        location+=1
        try: # defines close square as the previous square so we can see where a line would be drawn
            closesquare=directionss[location]
        except IndexError:
            lastspot=True
        line=math.floor(i/4)
        print(closesquare,line,i)
            #side 2,5,8
        #i 3-8   2-5   1-2 
        if closesquare-1==i:
            print(line)
            testlineplace[line][((i-(line*4))*3)+2]+=10
            print(testlineplace[line])
        #i 0-2   1-5   2-8
        if closesquare+1==i:
            print(line)
            testlineplace[line][((i-(line*4))*3)-1]+=10
            print(testlineplace[line])
        #down 1,4,7,10
        #i 12-1   13-4   14-7   15-10
        if closesquare+4==i:
            print(line)
            testlineplace[line][((i-(line*4))*3)+1]+=10
            print(testlineplace[line]) 
        #up 0,3,6,9
        if closesquare-4==i:
            print(line)
            testlineplace[line][(i-(line*4))*3]+=10
            print(testlineplace[line])
                
                
print(testlineplace)
print(testlineplace[0])
print(testlineplace[1])
print(testlineplace[2])
print(testlineplace[3])