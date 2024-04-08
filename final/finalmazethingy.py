import random
import math

canvas=[32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mazeDone=False
lastSquare=0
directions=[0]
correctdirections=[0]
lineplace={
0:[0,0,0,0,0,0,0,0,0,0,0,0],
1:[0,0,0,0,0,0,0,0,0,0,0,0],
2:[0,0,0,0,0,0,0,0,0,0,0,0],
3:[0,0,0,0,0,0,0,0,0,0,0,0],
}

def avalivlesquare(currentsquare,canvas):
    possiblesquares=[]
    actualsquares=[]
    possiblesquares.append(currentsquare+4)
    possiblesquares.append(currentsquare+1)
    possiblesquares.append(currentsquare-4)
    possiblesquares.append(currentsquare-1)
    
    for i in possiblesquares:
        if i<16 and i>-1:
            if canvas[i]<16:
                if (i%4==0 and currentsquare%4==3) or (i%4==3 and currentsquare%4==0):
                    pass
                else:
                    actualsquares.append(i)
    return actualsquares

def canvasprint(directions,lineplace):
    wall="H  "*4
    fullempty="-  "*4
    
    midcenterfull="-  "*2+"L  "+"-  "
    midfullfull="L  "*4
    midleftfull="L  "*3+"-  "
    midrightfull="-  "*2+"L  "*2
    
    linefull="H  "*2+"L  "+"H  "
    lineempty="H  "*2+"-  "+"H  "
    
    sidefull="H  "+"-  "+"L  "+"-  "
    sideempty="H  "+"-  "*3
    
    output=""
    line=0
    location=0
    lastspot=False
    
    
   

    for i in directions:
        location+=1
        try:
            closesquare=directions[location]
        except IndexError:
            lastspot=True
        line=math.floor(i/4)
        if lastspot==False: 
               #side 2,5,8
            #i 3-8   2-5   1-2 
            if closesquare-1==i:
                lineplace[line][((i-(line*4))*3)+2]=1
            #i 0-2   1-5   2-8
            if closesquare+1==i:
                lineplace[line][((i-(line*4))*3)-1]=1
            #down 1,4,7,10
            
            #i 12-1   13-4   14-7   15-10
            if closesquare+4==i:
                lineplace[line][((i-(line*4))*3)+1]=1 
                
            #up 0,3,6,9
            if closesquare-4==i:
                lineplace[line][(i-(line*4))*3]=1 

            for o in range(4):
                fixlineplacepos=0
                for u in lineplace[o]:
                    if u==1:
                        if fixlineplacepos%3==1:
                            lineplace[o-1][fixlineplacepos-1]=1
                        if fixlineplacepos%3==0:
                            lineplace[o+1][fixlineplacepos+1]=1
                    fixlineplacepos+=1

    for i in range(17):
        line=math.floor(i/4)
        if i == 0 or i==16:
            output=output+(wall*4+"H\n")
            continue
        currentlinetype=i%4
        currentlinepartlist=[]
        lineplacepos=0
        posinlineplaceline=0
        newlinelist=[]
        previous2point=0
        previouslinepartlist=0

        for e in lineplace[line]:
            currentlinepartlist.append(e)
            if posinlineplaceline==2 or posinlineplaceline==5 or posinlineplaceline==8 or posinlineplaceline==11:
                if currentlinetype==0:
                    if currentlinepartlist[1]==1:
                        output=output+linefull
                    else:
                        output=output+lineempty
                        
                        
                if currentlinetype==1:
                    if currentlinepartlist[1]==1:
                        output=output+sidefull
                    else:
                        output=output+sideempty
                        
                        
                if currentlinetype==3:
                    if currentlinepartlist[0]==1:
                        output=output+sidefull
                    else:
                        output=output+sideempty
                        
                        
                if currentlinetype==2: #if in a median line
                    if currentlinepartlist[2]==1 and previous2point==0:
                        output=output+midrightfull
                    elif previous2point==1 and currentlinepartlist[2]==0:
                        output=output+midleftfull
                    elif currentlinepartlist[2]==1 and previous2point==1:
                        output=output+midfullfull
                    elif currentlinepartlist[1]==1 or currentlinepartlist[0]==1:
                        output=output+midcenterfull
                    else:
                        output=output+fullempty
                previous2point=currentlinepartlist[2]
                currentlinepartlist.clear()
                
            posinlineplaceline+=1
        output+="H\n"
    print(output)

def usernextsquare(avaliblenextsquares):
    while True:
        print(f"your next avalibe squares are {avaliblenextsquares}")
        gh=input("where would you like to go\n> ")
        try:
            gh=int(gh)
        except:
            print("that is not a valid input")
            continue
        if gh in avaliblenextsquares:
            return gh
        else:
            print("that is not a valid input")
    #gh=random.randint(1,len(avaliblenextsquares))

def correctdirection(canvas):
    lastSquare=0
    while True:
        avaliblenextsquares=avalivlesquare(lastSquare,canvas)
        if len(avaliblenextsquares)==0:
            return correctdirections
        gh=random.randint(1,len(avaliblenextsquares))
        nextsquare=avaliblenextsquares[gh-1]
        correctdirections.append(nextsquare)
        canvas[nextsquare]=canvas[nextsquare]+32
        lastSquare=nextsquare



correctdirections=correctdirection(canvas)
canvasprint(correctdirections,lineplace)
canvas=[32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lineplace={
0:[0,0,0,0,0,0,0,0,0,0,0,0],
1:[0,0,0,0,0,0,0,0,0,0,0,0],
2:[0,0,0,0,0,0,0,0,0,0,0,0],
3:[0,0,0,0,0,0,0,0,0,0,0,0],
}
while mazeDone==False:
    canvasprint(directions,lineplace)
    avaliblenextsquares=avalivlesquare(lastSquare,canvas)
    if len(avaliblenextsquares)==0:
        break
    nextsquare=usernextsquare(avaliblenextsquares)
    directions.append(nextsquare)
    canvas[nextsquare]=canvas[nextsquare]+32
    lastSquare=nextsquare