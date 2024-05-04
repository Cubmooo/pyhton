lineplace={ # line place is the directions the player has gone. it can be broken down by square with 3 values for each square and 4 squares per line. the three values in order mean there is a line going down a line going up and a line going to the right
0:[0,0,0,0,0,0,0,0,0,0,0,0],
1:[0,0,0,0,0,0,0,0,0,0,0,0],
2:[0,0,0,0,0,0,0,0,0,0,0,0],
3:[0,0,0,0,0,0,0,0,0,0,0,0],
}
mazesize=4
direections=[0,1,2,3,7,11,15,14,13,12,8]
import math

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

print(lineplace)
print(testlineplace)
print(lineplace==testlineplace)


def canvasprint(directionss,lineplace2,testlineplace):
    print(lineplace)
    print(testlineplace)
    print(lineplace==testlineplace)
    wall="■  "*4     # defines or the diffrent types of blocks used to print the maze
    fullempty="   "*4
 
    midcenterfull="   "*2+"O  "+"   "
    midfullfull="O  "*4
    midleftfull="O  "*3+"   "
    midrightfull="   "*2+"O  "*2
 
    linefull="■  "*2+"O  "+"■  "
    lineempty="■  "*2+"   "+"■  "
 
    sidefull="■  "+"   "+"O  "+"   "
    sideempty="■  "+"   "*3
 
    output=""
    line=0
    location=0
    lastspot=False
    fixlineplacepos=0
    previous2point=0
    
    
    closesquare=0
    location=0
    
    for i in directionss: # runs through the directions turning it into the line place format
        location+=1
        try: # defines close square as the previous square so we can see where a line would be drawn
            closesquare=directionss[location]
        except IndexError:
            lastspot=True
        line=math.floor(i/4)
        if lastspot==False:# turns the current and previous squares into the right number in line place 
            print(closesquare,line,i)
               #side 2,5,8
            #i 3-8   2-5   1-2 
            if closesquare-1==i:
                print(line)
                testlineplace[line][((i-(line*4))*3)+2]=1
            #i 0-2   1-5   2-8
            if closesquare+1==i:
                print(line)
                testlineplace[line][((i-(line*4))*3)-1]=1
            #down 1,4,7,10
            #i 12-1   13-4   14-7   15-10
            if closesquare+4==i:
                print(line)
                testlineplace[line][((i-(line*4))*3)+1]=1 
            #up 0,3,6,9
            if closesquare-4==i:
                print(line)
                testlineplace[line][(i-(line*4))*3]=1 
 
 
    closesquare=0
    location=0
    lastspot=False
    line=0
    for c in directionss: # runs through the directions turning it into the line place format
        location+=1
        try: # defines close square as the previous square so we can see where a line would be drawn
            closesquare=directionss[location]

        except IndexError:
            lastspot=True
        line=math.floor(c/4)
        if lastspot==False:# turns the current and previous squares into the right number in line place
            print(closesquare,line,c)
               #side 2,5,8
            #i 3-8   2-5   1-2 
            if closesquare-1==c:
                lineplace2[line][((c-(line*4))*3)+2]=1
            #i 0-2   1-5   2-8
            if closesquare+1==c:
                lineplace2[line][((c-(line*4))*3)-1]=1
            #down 1,4,7,10
            #i 12-1   13-4   14-7   15-10
            if closesquare+4==c:
                lineplace2[line][((c-(line*4))*3)+1]=1 
            #up 0,3,6,9
            if closesquare-4==c:
                lineplace2[line][(c-(line*4))*3]=1 
                
    print(lineplace)
    print(testlineplace)
    print(lineplace==testlineplace)
    print(testlineplace[0])
    print(testlineplace[1])
    print(testlineplace[2])
    print(testlineplace[3])
                
    for u in range(4): # the previous solution didnt correctly use up and down. it would only index either the up or the down part properly this fixes this problem but checking for an up or down and turning on the corsponding up or down
        fixlineplacepos=0
        for o in lineplace2[u]:
            if fixlineplacepos%3==0 and o==1:
                lineplace2[u+1][fixlineplacepos+1]=1
            if fixlineplacepos%3==1 and o==1:
                lineplace2[u-1][fixlineplacepos-1]=1
            fixlineplacepos+=1 
 
    for i in range(17): # runs through 17 times once for each line
        currentline=""
        line=math.floor(i/4)
        if i == 0 or i==16: # if first or last line make it the border
            output=output+(wall*4+"■\n")
            continue
        newlinelist=[]
        lineplacepos=0
 
        for e in (lineplace2[line]):# run through each value in the the list for what ever line 
            newlinelist.append(e)# create a small list for indivduial square
            if len(newlinelist)==3:# carry on when list is the right size
                if i%4==0: # when we are in the boundry area between to squares
                    if newlinelist[1]==1: # check if line should be there is so print line if not then dont
                        output=output+linefull
                    else:
                        output=output+lineempty
 
 
                if i%4==1: #when in the top part of square
                    if newlinelist[1]==1:# check if line should be there is so print line if not then dont
                        output=output+sidefull
                    else:
                        output=output+sideempty
 
                if i%4==3: #when in bottom part of square
                    if newlinelist[0]==1:# check if line should be there is so print line if not then dont
                        output=output+sidefull
                    else:
                        output=output+sideempty
 
                if i%4==2: # when in median part of square
                    if newlinelist[2]==1 and previous2point==1: #check what type of line should be there and print it
                        output=output+midfullfull
                    elif newlinelist[2]==1 and previous2point==0:
                        output=output+midrightfull
                    elif newlinelist[2]==0 and previous2point==1:
                        output=output+midleftfull
                    elif newlinelist[1]==1 or newlinelist[0]==1:
                        output=output+midcenterfull
                    else:
                        output=output+fullempty
                    previous2point=newlinelist[2] #rpevious point is wether this box has a line going to the left. does this by changing previous boxes line to the right to the left
                newlinelist.clear()  # restat small box list
            lineplacepos+=1
 
        output=output+currentline+"■\n"
    print(output)# print final output
    
canvasprint(direections,lineplace,testlineplace)