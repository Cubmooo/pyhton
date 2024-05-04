lineplace={ # line place is the directions the player has gone. it can be broken down by square with 3 values for each square and 4 squares per line. the three values in order mean there is a line going down a line going up and a line going to the right
0:[0,0,0,0,0,0,0,0,0,0,0,0],
1:[0,0,0,0,0,0,0,0,0,0,0,0],
2:[0,0,0,0,0,0,0,0,0,0,0,0],
3:[0,0,0,0,0,0,0,0,0,0,0,0],
}
mazesize=4

def defincelineplace(mazesize):
    lineplace={}
    lineplaceindex=[]
    for l in range(mazesize):
        for t in range(3):
            lineplaceindex.append(0)
            
    for i in range(mazesize):
        lineplace.update({i:lineplaceindex})
        
    return lineplace 

testlineplace=defincelineplace(mazesize)
print(lineplace==testlineplace)