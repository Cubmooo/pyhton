import math
lineplace={
0:[0,0,0,0,0,0,0,0,0,0,0],
1:[0,0,0,0,0,0,0,0,0,0,0],
2:[0,0,0,0,0,0,0,0,0,0,0],
3:[0,0,0,0,0,0,0,0,0,0,0],
}
location=0

directions=[0,4,8,9,10,6,2,3,7,11]

for i in directions:
    location+=1
    line=math.floor(i/4)
    try:
        closesquare=directions[location]
    except IndexError:
        lastspot=True
    print(i,closesquare)
    #side 2,5,8
    #i 3-8   2-5   1-2 
    if closesquare-1==i:
        print(((i-(line*4))*3)-1)
        print(i-(line*4))
        lineplace[line][((i-(line*4))*3)+2]=1
    #i 0-2   1-5   2-8
    if closesquare+1==i:
        print(((i-(line*4))*3)+2)
        lineplace[line][((i-(line*4))*3)-1]=1
    #down 1,4,7,10
    #i 12-1   13-4   14-7   15-10
    if closesquare+4==i:
        print(((i-(line*4))*3)+1)
        lineplace[line][((i-(line*4))*3)+1]=1 
    #up 0,3,6,9
    if closesquare-4==i:
        print((i-(line*4))*3)
        lineplace[line][(i-(line*4))*3]=1 

print(directions)
print(lineplace[3])
print(lineplace[2])
print(lineplace[1])
print(lineplace[0])