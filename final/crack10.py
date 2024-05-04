import random
import math
import copy
#import libraries used
 
def test(i):
    print(f"test{i}")
    
mazesize=3

def definelineplace(mazesize):
    lineplace={}
    lineplaceindex=[]
    gh=0
    while gh!=mazesize:
        lineplaceindex=[]
        for i in range(mazesize*3):
            lineplaceindex.append(0)
        lineplace.update({gh:lineplaceindex})
        gh+=1
    return lineplace

def avalivlesquare(currentsquare,direction): # see all avlible next square to move
    canvas=[]
    for u in range(mazesize**2):
        canvas.append(u)
    canvas[0]=-1
    possiblesquares=[]
    actualsquares=[]
    possiblesquares.append(currentsquare+mazesize) # gather all potential possible squares
    possiblesquares.append(currentsquare+1)
    possiblesquares.append(currentsquare-mazesize)
    possiblesquares.append(currentsquare-1)
    
    for e in direction:
        canvas[e]=(-e)-1
 
    for i in possiblesquares: # runs through all potentialpossible squares removing all that have been in or dont exist
        if i<mazesize**2 and i>-1:
            if canvas[i]>0:
                if (i%mazesize==0 and currentsquare%mazesize==mazesize-1) or (i%mazesize==mazesize-1 and currentsquare%mazesize==0):
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
        line=math.floor(i/mazesize)
        if lastspot==False:# turns the current and previous squares into the right number in line place 
               #side 2,5,8
            #i 3-8   2-5   1-2 
            if closesquare-1==i:
                lineplace[line][((i-(line*mazesize))*3)+2]=1
            #i 0-2   1-5   2-8
            if closesquare+1==i:
                lineplace[line][((i-(line*mazesize))*3)-1]=1
            #down 1,4,7,10
            #i 12-1   13-4   14-7   15-10
            if closesquare+mazesize==i:
                lineplace[line][((i-(line*mazesize))*3)+1]=1 
            #up 0,3,6,9
            if closesquare-mazesize==i:
                lineplace[line][(i-(line*mazesize))*3]=1 
 
 
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
        line=(math.floor(i/4))
        if i == 0 or i==(mazesize*4): # if first or last line make it the border
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
 
def check(correctdirections,directions):
    newcorrectdirections=[]
    pos=0
    try:
        for i in directions:
            newcorrectdirections.append(correctdirections[pos])
            pos+=1
    except:
        newcorrectdirections=["no"]
    return not newcorrectdirections==directions

def randomquestions(avaliblenextsquares,lastsquare,correctnextsquare,difficulty,randomquestionsettings):
    number1=0
    number2=0
    operations=["+","-","*","/"]
    units=["cm","mm","m"]
    operation=random.randint(0,randomquestionsettings["operation"])
    
    if operation==4 or operation==5:
        answer=random.randint(randomquestionsettings["algebraadditionmin"],randomquestionsettings["algebraadditionmax"])
        number1=random.randint(randomquestionsettings["algebraadditionmin"],randomquestionsettings["algebraadditionmax"])
        number2=random.randint(randomquestionsettings["algebraadditionmin"],randomquestionsettings["algebraadditionmax"])
        number3=eval(f"({number1}*{answer})+{number2}")
        print(f"If {number1}x + {number2} = {number3} what does X equal?")

    if operation==6 or operation==7:
        wordquestion=random.randint(0,1)
        if wordquestion==0:
            while True:
                number1hour=str(random.randint(0,20)).zfill(2)
                number1min=str(random.randint(0,59)).zfill(2)
                number2hour=str(int(number1hour)+random.randint(randomquestionsettings['minhourdiffrence'],randomquestionsettings['maxhourdiffrence'])).zfill(2)
                number2min=str(random.randint(0,59)).zfill(2)
                answer=(60-int(number1min)+int(number2min))+60*(int(number2hour)-int(number1hour)-1)
                if answer<0:
                    continue
                break
            if number2hour>=24:
                number2hourdisplay=number2hour%24
            print(f"If a train departed from its station at {number1hour}:{number1min} and arrived at its desination at {number2hourdisplay}:{number2min} how long did the ride take?")
        
        if wordquestion==1:
            unit=units[random.randint(0,2)]
            geometrytype=random.randint(0,1)
            
            if geometrytype==0:
                number1=random.randint(randomquestionsettings['geotrianglemin'],randomquestionsettings['geotrianglemax'])
                number2=random.randint(randomquestionsettings['geotrianglemin'],math.floor(randomquestionsettings['geotrianglemax']-number1/2))
                answer=round((number1*number2)/2)
                print(f"What is the volume of a TRIANGLE with a height of {number1}{unit} a width of {number2}{unit}?")
            if geometrytype==1:
                number1=random.randint(randomquestionsettings['geocubemin'],randomquestionsettings['geocubecombinedmax']-2)
                randomquestionsettings['geocubecombinedmax']-=number1
                number2=random.randint(randomquestionsettings['geocubemin'],randomquestionsettings['geocubecombinedmax']-1)
                randomquestionsettings['geocubecombinedmax']-=number2
                number3=random.randint(randomquestionsettings['geocubemin'],randomquestionsettings['geocubecombinedmax'])
                answer=number1*number2*number3
                print(f"What is the volume of a CUBE with a height of {number1}{unit} a width of {number2}{unit} and a depth of {number3}{unit}?")
    
    if operation==2 or operation==3:
        number1=random.randint(randomquestionsettings['multiplicationmin'],randomquestionsettings['multiplicationmax'])
        number2=random.randint(randomquestionsettings['multiplicationmin'],randomquestionsettings['multiplicationmax'])
        answer=eval(f"{number1}*{number2}")
        if operation==3:
            numberhold=answer
            answer=number1
            number1=numberhold
        print(f"What is {number1} {operations[operation]} {number2}?")

    if operation==0 or operation==1:
        while True:
            number1=random.randint(randomquestionsettings['additionmin'],randomquestionsettings['additionmax'])
            number2=random.randint(randomquestionsettings['additionmin'],randomquestionsettings['additionmax'])
            answer=eval(f"{number1}{operations[operation]}{number2}")
            if answer<0 and randomquestionsettings['allownegativeaddition']==False:
                continue
            break
        print(f"What is {number1} {operations[operation]} {number2}?")
        
    useranswer=checkmathsanswer(answer,avaliblenextsquares,lastsquare,correctnextsquare)
    return useranswer,difficulty,randomquestionsettings
    
def checkmathsanswer(answer,avaliblenextsquares,lastsquare,correctnextsquare):
    optiontext=""
    potentialanswers=[]
    newavalibenextsquare=[]
    answerfound=False
    for i in avaliblenextsquares:
        potentialanswer=0
        if i==lastsquare+mazesize:
            direction="down"
        if i==lastsquare-mazesize:
            direction="up"
        if i==lastsquare+1:
            direction="right"
        if i==lastsquare-1:
            direction="left"
        if i==correctnextsquare:
            potentialanswer=answer
            potentialanswers=[answer]+potentialanswers
        else:
            while True:
                potentialanswer=answer+random.randint(-20,20)
                if potentialanswer!=answer:
                    break
            potentialanswers.append(potentialanswer)
                    
        optiontext=optiontext+str(potentialanswer)+",("+str(direction)+")  "
         
    for o in avaliblenextsquares:
        if o==correctnextsquare:
            newavalibenextsquare=[o]+newavalibenextsquare
        else:
            newavalibenextsquare.append(o)
    while answerfound==False:
        intuseranswer=""
        print(f"Your avalible options are {optiontext}")
        useranswer=input("> ")
        for i in useranswer:
            if i=="-":
                intuseranswer=intuseranswer+i
            try:
                i=int(i)
                intuseranswer=intuseranswer+str(i)
            except:
                continue
        intuseranswer=int(intuseranswer)
        for u in range(len(potentialanswers)):
            if intuseranswer==potentialanswers[u]:
                usermovesquare=newavalibenextsquare[u]
                answerfound=True
                break
            else:
                continue
    return usermovesquare
        
def maze(lastSquare,canvas,lineplace,directions,correctdirections,difficulty,randomquestionsettings):

    hold=False
    mazeDone=False
    while mazeDone==False:# repeat until maze done
        canvasprint(directions,lineplace)#print canvas
        avaliblenextsquares=avalivlesquare(lastSquare,directions)# find next avalible squares if none end program
        if len(avaliblenextsquares)==0:
            break
        try:
            correctnextsquare=correctdirections[len(directions)]
        except:
            correctnextsquare=0
        nextsquare,difficulty,randomquestionsettings=randomquestions(avaliblenextsquares,lastSquare,correctnextsquare,difficulty,randomquestionsettings)# ask what move they want next then add that to directions and mark that area as having been in
        if hold==False:
            holddirections=directions.copy()
            holdcanvas=canvas.copy()
            holdlineplace=copy.deepcopy(lineplace)
        directions.append(nextsquare)
        hold=check(correctdirections,directions)
        lastSquare=nextsquare # updates the current square for next time
    return directions,holddirections,holdcanvas,holdlineplace

def questions():
    difficulty=3
    randomquestionsettings={
        'additionmax':10**difficulty,
        'additionmin':1,
        'allownegativeaddition':difficulty!=1,
        'multiplicationmax':(difficulty-1)*8,
        'multiplicationmin':1,
        'geocubemin':1,
        'geocubecombinedmax':20,
        'geotrianglemin':1,
        'geotrainglemax':2,
        'minhourdiffrence':0,
        'maxhourdiffrence':3,
        'algebraadditionmin':1,
        'algebraadditionmax':20,
        'algebramultiplicationmin':1,
        'algebramultiplicationmax':(difficulty-1)*8,
        'operation':(2**difficulty)-1
    }  
    instructionsinput=input("Hello welcome to this maths maze would you like to see the instructions\nYou can respond yes or no\n> ")
    if instructionsinput.lower()=="yes":
        instructionsprint()
    while True:
        mazesizeinput=input("How large would you like the maze to be\nYou can pick any option larger then 2 however any number above 10 may not display correctly\n> ")
        try:
            mazesizeinput=round(int(mazesizeinput))
        except:
            print("Invalid input, please input just an integer greater than 2")
            continue
        if mazesizeinput<3:
            continue
        break
    
    while True:
        difficulty=input('How difficult would you like the questions to be\nYou can pick "1", "2", "3" or "ADVANCED" for greater control\n> ')
        if difficulty=="ADVANCED":
            randomquestionsettings=difficultyadvanced(randomquestionsettings)
            difficulty=3
            break
        else:
            try:
                difficulty=round(int(difficulty))
            except:
                print('Invalid input, please input just "1", "2" or "3"')
                continue
            if difficulty<1 or difficulty>3:
                continue
            break
    
    return mazesizeinput,difficulty,randomquestionsettings

def difficultyadvanced(randomquestionsettings):
    print("ADVANCED")
    return randomquestionsettings

def instructionsprint():
    print("instructions")

def start():
    global mazesize
    mazesize,difficulty,randomquestionsettings=questions()
    lastSquare=0
    directions=[0] # directions used to know where the player has gone
    correctdirections=correctdirectionss() # get correct directions then print them, reset canvas and lineplace for player use
    lineplace=definelineplace(mazesize)
    canvas=[32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    while True:
        directions,holddirections,holdcanvas,holdlineplace=maze(lastSquare,canvas,lineplace,directions,correctdirections,difficulty,randomquestionsettings)
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
            
                
start()