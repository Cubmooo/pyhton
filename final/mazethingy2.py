import random
import math
import copy
#import libraries used
 
def test(i):
    print(f"test{i}")
 
mazesize=4
mazeDone=False
lastSquare=0
directions=[0] # directions used to know where the player has gone
 
def definelineplace(mazesize):
    lineplace={}
    lineplaceindex=[]
    for l in range(mazesize):
        for t in range(3):
            lineplaceindex.append(0)
    for i in range(mazesize):
        lineplace.update({i:lineplaceindex})
    return lineplace

def avalivlesquare(currentsquare,direction): # see all avlible next square to move
    canvas=[32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    possiblesquares=[]
    actualsquares=[]
    possiblesquares.append(currentsquare+4) # gather all potential possible squares
    possiblesquares.append(currentsquare+1)
    possiblesquares.append(currentsquare-4)
    possiblesquares.append(currentsquare-1)
    
    for e in direction:
        canvas[e]=e+32
 
    for i in possiblesquares: # runs through all potentialpossible squares removing all that have been in or dont exist
        if i<16 and i>-1:
            if canvas[i]<16:
                if (i%4==0 and currentsquare%4==3) or (i%4==3 and currentsquare%4==0):
                    pass
                else:
                    actualsquares.append(i)
    return actualsquares
 
 
def canvasprint(directions,lineplace):
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
 
 
 
    for i in directions: # runs through the directions turning it into the line place format
        location+=1
        try: # defines close square as the previous square so we can see where a line would be drawn
            closesquare=directions[location]
        except IndexError:
            lastspot=True
        line=math.floor(i/4)
        if lastspot==False:# turns the current and previous squares into the right number in line place 
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
 
 
    for u in range(mazesize): # the previous solution didnt correctly use up and down. it would only index either the up or the down part properly this fixes this problem but checking for an up or down and turning on the corsponding up or down
        fixlineplacepos=0
        for o in lineplace[u]:
            if fixlineplacepos%3==0 and o==1:
                lineplace[u+1][fixlineplacepos+1]=1
            if fixlineplacepos%3==1 and o==1:
                lineplace[u-1][fixlineplacepos-1]=1
            fixlineplacepos+=1 
 
    for i in range((mazesize*4)+1): # runs through 17 times once for each line
        currentline=""
        line=math.floor(i/mazesize)
        if i == 0 or i==mazesize*4: # if first or last line make it the border
            output=output+(wall*mazesize+"■\n")
            continue
        newlinelist=[]
        lineplacepos=0
 
        for e in (lineplace[line]):# run through each value in the the list for what ever line 
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
 
 
def correctdirectionss(): # define the correct direction before we start(currently dose nothing but will use to check later) same prossces as normal directions
    lastSquare=0
    correctdirections=[0]
    while True:
        avaliblenextsquares=avalivlesquare(lastSquare,correctdirections)
        if len(avaliblenextsquares)==0:
            return correctdirections
        gh=random.randint(1,len(avaliblenextsquares))
        nextsquare=avaliblenextsquares[gh-1]
        correctdirections.append(nextsquare)
        lastSquare=nextsquare
 
def asknextmove(avalibelsquares): # asks the user where to go next then checks if it is valid if not then repeat
    while True:
        print(f"your next avalible squares are {avalibelsquares}")
        gh=input("where do you want to go \n> ")
        try:
            gh=int(gh)
            if gh in avalibelsquares:
                return gh
            else:
                print("not valid")  
        except:
            print("not valid")
 
def check(correctdirections,directions):
    newcorrectdirections=[]
    pos=0
    for i in directions:
        newcorrectdirections.append(correctdirections[pos])
        pos+=1
    return not newcorrectdirections==directions
 
def maze(lastSquare,canvas,lineplace,directions):
 
    hold=False
    while mazeDone==False:# repeat until maze done
        canvasprint(directions,lineplace)#print canvas
        avaliblenextsquares=avalivlesquare(lastSquare,directions)# find next avalible squares if none end program
        if len(avaliblenextsquares)==0:
            break
        nextsquare=asknextmove(avaliblenextsquares)# ask what move they want next then add that to directions and mark that area as having been in
        if hold==False:
            holddirections=directions.copy()
            holdcanvas=canvas.copy()
            holdlineplace=copy.deepcopy(lineplace)
        directions.append(nextsquare)
        canvas[nextsquare]=canvas[nextsquare]+32
        hold=check(correctdirections,directions)
        lastSquare=nextsquare # updates the current square for next time
    return directions,holddirections,holdcanvas,holdlineplace
 
correctdirections=correctdirectionss() # get correct directions then print them, reset canvas and lineplace for player use
lineplace=definelineplace(mazesize)
print(lineplace)
canvasprint(correctdirections,lineplace)
lineplace=definelineplace(mazesize)
canvas=[32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
 
while True:
    directions,holddirections,holdcanvas,holdlineplace=maze(lastSquare,canvas,lineplace,directions)
    mazecmpleted=directions==correctdirections
    if mazecmpleted==True:
        print("sucsess")
        exit()
    else:
        directions=holddirections.copy()
        canvas=holdcanvas.copy()
        lineplace=holdlineplace.copy()
        print("you made a wrong turn and was placed back at last correct point")
        lastSquare=holddirections[-1]