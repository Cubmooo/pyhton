import random
import math
import copy
#import libraries used
    
mazeSize=3

def definelinePlace(mazeSize):
    linePlace={}
    linePlaceIndex=[]
    gh=0
    while gh!=mazeSize:
        linePlaceIndex=[]
        for i in range(mazeSize*3):
            linePlaceIndex.append(0)
        linePlace.update({gh:linePlaceIndex})
        gh+=1
    return linePlace

def avalivlesquare(currentSquare,direction): # see all avlible next square to move
    canvas=[]
    for u in range(mazeSize**2):
        canvas.append(u)
    canvas[0]=-1
    possibleSquares=[]
    actualSquares=[]
    possibleSquares.append(currentSquare+mazeSize) # gather all potential possible squares
    possibleSquares.append(currentSquare+1)
    possibleSquares.append(currentSquare-mazeSize)
    possibleSquares.append(currentSquare-1)
    
    for e in direction:
        canvas[e]=(-e)-1
 
    for i in possibleSquares: # runs through all potentialpossible squares removing all that have been in or dont exist
        if i<mazeSize**2 and i>-1:
            if canvas[i]>0:
                if (i%mazeSize==0 and currentSquare%mazeSize==mazeSize-1) or (i%mazeSize==mazeSize-1 and currentSquare%mazeSize==0):
                    pass
                else:
                    actualSquares.append(i)
    return actualSquares
 
def canvasprint(directions,linePlace):
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
    fixlinePlacePos=0
    previous2point=0
 
 
 
    for i in directions: # runs through the directions turning it into the line place format
        location+=1
        try: # defines close square as the previous square so we can see where a line would be drawn
            closeSquare=directions[location]
        except IndexError:
            lastspot=True
        line=math.floor(i/mazeSize)
        if lastspot==False:# turns the current and previous squares into the right number in line place 
               #side 2,5,8
            #i 3-8   2-5   1-2 
            if closeSquare-1==i:
                linePlace[line][((i-(line*mazeSize))*3)+2]=1
            #i 0-2   1-5   2-8
            if closeSquare+1==i:
                linePlace[line][((i-(line*mazeSize))*3)-1]=1
            #down 1,4,7,10
            #i 12-1   13-4   14-7   15-10
            if closeSquare+mazeSize==i:
                linePlace[line][((i-(line*mazeSize))*3)+1]=1 
            #up 0,3,6,9
            if closeSquare-mazeSize==i:
                linePlace[line][(i-(line*mazeSize))*3]=1 
 
 
    for u in range(mazeSize): # the previous solution didnt correctly use up and down. it would only index either the up or the down part properly this fixes this problem but checking for an up or down and turning on the corsponding up or down
        fixlinePlacePos=0
        for o in linePlace[u]:
            if fixlinePlacePos%3==0 and o==1:
                linePlace[u+1][fixlinePlacePos+1]=1
            if fixlinePlacePos%3==1 and o==1:
                linePlace[u-1][fixlinePlacePos-1]=1
            fixlinePlacePos+=1 
 
    for i in range((mazeSize*4)+1): # runs through 17 times once for each line
        currentLine=""
        line=(math.floor(i/4))
        if i == 0 or i==(mazeSize*4): # if first or last line make it the border
            output=output+(wall*mazeSize+"■\n")
            continue
        newLineList=[]
        linePlacePos=0
        for e in (linePlace[line]):# run through each value in the the list for what ever line 
            newLineList.append(e)# create a small list for indivduial square
            if len(newLineList)==3:# carry on when list is the right size
                if i%4==0: # when we are in the boundry area between to squares
                    if newLineList[1]==1: # check if line should be there is so print line if not then dont
                        output=output+linefull
                    else:
                        output=output+lineempty
 
 
                if i%4==1: #when in the top part of square
                    if newLineList[1]==1:# check if line should be there is so print line if not then dont
                        output=output+sidefull
                    else:
                        output=output+sideempty
 
                if i%4==3: #when in bottom part of square
                    if newLineList[0]==1:# check if line should be there is so print line if not then dont
                        output=output+sidefull
                    else:
                        output=output+sideempty
 
                if i%4==2: # when in median part of square
                    if newLineList[2]==1 and previous2point==1: #check what type of line should be there and print it
                        output=output+midfullfull
                    elif newLineList[2]==1 and previous2point==0:
                        output=output+midrightfull
                    elif newLineList[2]==0 and previous2point==1:
                        output=output+midleftfull
                    elif newLineList[1]==1 or newLineList[0]==1:
                        output=output+midcenterfull
                    else:
                        output=output+fullempty
                    previous2point=newLineList[2] #rpevious point is wether this box has a line going to the left. does this by changing previous boxes line to the right to the left
                newLineList.clear()  # restat small box list
            linePlacePos+=1
 
        output=output+currentLine+"■\n"
    print(output)# print final output
 
def correctDirectionss(): # define the correct direction before we start(currently dose nothing but will use to check later) same prossces as normal directions
    lastSquare=0
    correctDirections=[0]
    while True:
        avaliblenextSquares=avalivlesquare(lastSquare,correctDirections)
        if len(avaliblenextSquares)==0:
            return correctDirections
        gh=random.randint(1,len(avaliblenextSquares))
        nextSquare=avaliblenextSquares[gh-1]
        correctDirections.append(nextSquare)
        lastSquare=nextSquare 
 
def check(correctDirections,directions):
    newcorrectDirections=[]
    pos=0
    try:
        for i in directions:
            newcorrectDirections.append(correctDirections[pos])
            pos+=1
    except:
        newcorrectDirections=["no"]
    return not newcorrectDirections==directions

def randomquestions(avaliblenextSquares,lastSquare,correctnextSquare,difficulty,randomQuestionSettings):
    questionFail=False
    try:
        number1=0
        number2=0
        operations=["+","-","*","/"]
        units=["cm","mm","m"]
        operation=random.randint(0,randomQuestionSettings["operation"])
        
        if operation==4 or operation==5:
            answer=random.randint(randomQuestionSettings["algebraadditionmin"],randomQuestionSettings["algebraadditionmax"])
            number1=random.randint(randomQuestionSettings["algebraadditionmin"],randomQuestionSettings["algebraadditionmax"])
            number2=random.randint(randomQuestionSettings["algebraadditionmin"],randomQuestionSettings["algebraadditionmax"])
            number3=eval(f"({number1}*{answer})+{number2}")
            print(f"If {number1}x + {number2} = {number3} what does X equal?")

        if operation==6 or operation==7:
            wordQuestion=random.randint(0,1)
            if wordQuestion==0:
                while True:
                    number1hour=str(random.randint(0,20)).zfill(2)
                    number1min=str(random.randint(0,59)).zfill(2)
                    number2hour=str(int(number1hour)+random.randint(randomQuestionSettings['minhourdiffrence'],randomQuestionSettings['maxhourdiffrence'])).zfill(2)
                    number2min=str(random.randint(0,59)).zfill(2)
                    answer=(60-int(number1min)+int(number2min))+60*(int(number2hour)-int(number1hour)-1)
                    if answer<0:
                        continue
                    break
                number2hourdisplay=number2hour
                if int(number2hour)>=24:
                    number2hourdisplay=int(number2hour)%24
                    number2hourdisplay=str(number2hourdisplay).zfill(2)
                print(f"If a train departed from its station at {number1hour}:{number1min} and arrived at its desination at {number2hourdisplay}:{number2min} how long did the ride take?")
            
            if wordQuestion==1:
                unit=units[random.randint(0,2)]
                geometrytype=random.randint(0,1)
                
                if geometrytype==0:
                    number1=random.randint(randomQuestionSettings['geotrianglemin'],randomQuestionSettings['geotrianglemax'])
                    number2=random.randint(randomQuestionSettings['geotrianglemin'],math.floor(randomQuestionSettings['geotrianglemax']-number1/2))
                    answer=round((number1*number2)/2)
                    print(f"What is the volume of a TRIANGLE with a height of {number1}{unit} a width of {number2}{unit}?")
                if geometrytype==1:
                    number1=random.randint(randomQuestionSettings['geocubemin'],randomQuestionSettings['geocubecombinedmax']-2)
                    randomQuestionSettings['geocubecombinedmax']-=number1
                    number2=random.randint(randomQuestionSettings['geocubemin'],randomQuestionSettings['geocubecombinedmax']-1)
                    randomQuestionSettings['geocubecombinedmax']-=number2
                    number3=random.randint(randomQuestionSettings['geocubemin'],randomQuestionSettings['geocubecombinedmax'])
                    answer=number1*number2*number3
                    print(f"What is the volume of a CUBE with a height of {number1}{unit} a width of {number2}{unit} and a depth of {number3}{unit}?")
        
        if operation==2 or operation==3:
            number1=random.randint(randomQuestionSettings['multiplicationmin'],randomQuestionSettings['multiplicationmax'])
            number2=random.randint(randomQuestionSettings['multiplicationmin'],randomQuestionSettings['multiplicationmax'])
            answer=eval(f"{number1}*{number2}")
            if operation==3:
                numberhold=answer
                answer=number1
                number1=numberhold
            print(f"What is {number1} {operations[operation]} {number2}?")

        if operation==0 or operation==1:
            while True:
                number1=random.randint(randomQuestionSettings['additionmin'],randomQuestionSettings['additionmax'])
                number2=random.randint(randomQuestionSettings['additionmin'],randomQuestionSettings['additionmax'])
                answer=eval(f"{number1}{operations[operation]}{number2}")
                if answer<0 and randomQuestionSettings['allownegativeaddition']==False:
                    continue
                break
            print(f"What is {number1} {operations[operation]} {number2}?")
        userAnswer,userExit=checkmathsanswer(answer,avaliblenextSquares,lastSquare,correctnextSquare)
        return userAnswer,difficulty,randomQuestionSettings,questionFail,userExit
    except:
        userExit=False
        questionFail=True
        userAnswer=0
        return userAnswer,difficulty,randomQuestionSettings,questionFail,userExit
    
def checkmathsanswer(answer,avaliblenextSquares,lastSquare,correctnextSquare):
    userExit=False
    optionText=""
    potentialAnswers=[]
    newAvaliblenextSquare=[]
    answerFound=False
    for i in avaliblenextSquares:
        potentialAnswer=0
        if i==lastSquare+mazeSize:
            direction="down"
        if i==lastSquare-mazeSize:
            direction="up"
        if i==lastSquare+1:
            direction="right"
        if i==lastSquare-1:
            direction="left"
        if i==correctnextSquare:
            potentialAnswer=answer
            potentialAnswers=[answer]+potentialAnswers
        else:
            while True:
                potentialAnswer=answer+random.randint(-20,20)
                if potentialAnswer!=answer:
                    break
            potentialAnswers.append(potentialAnswer)
                    
        optionText=optionText+str(potentialAnswer)+",("+str(direction)+")  "
         
    for o in avaliblenextSquares:
        if o==correctnextSquare:
            newAvaliblenextSquare=[o]+newAvaliblenextSquare
        else:
            newAvaliblenextSquare.append(o)
    while answerFound==False:
        intUserAnswer=""
        print(f"Your avalible options are {optionText}")
        userAnswer=input("> ")
        if userAnswer.lower()=="exit":
            userExit=True
            userMoveSquare=0
            break
        for i in userAnswer:
            if i=="-":
                intUserAnswer=intUserAnswer+i
            try:
                i=int(i)
                intUserAnswer=intUserAnswer+str(i)
            except:
                continue
        intUserAnswer=int(intUserAnswer)
        for u in range(len(potentialAnswers)):
            if intUserAnswer==potentialAnswers[u]:
                userMoveSquare=newAvaliblenextSquare[u]
                answerFound=True
                break
            else:
                continue
                
    return userMoveSquare,userExit
        
def maze(lastSquare,canvas,linePlace,directions,correctDirections,difficulty,randomQuestionSettings):

    hold=False
    mazeDone=False
    while mazeDone==False:# repeat until maze done
        canvasprint(directions,linePlace)#print canvas
        avaliblenextSquares=avalivlesquare(lastSquare,directions)# find next avalible squares if none end program
        if len(avaliblenextSquares)==0:
            break
        try:
            correctnextSquare=correctDirections[len(directions)]
        except:
            correctnextSquare=0
        nextSquare,difficulty,randomQuestionSettings,questionFail,userExit=randomquestions(avaliblenextSquares,lastSquare,correctnextSquare,difficulty,randomQuestionSettings)# ask what move they want next then add that to directions and mark that area as having been in
        if userExit==True:
            exit()
        if hold==False:
            holdDirections=directions.copy()
            holdCanvas=canvas.copy()
            holdlinePlace=copy.deepcopy(linePlace)
        directions.append(nextSquare)
        hold=check(correctDirections,directions)
        lastSquare=nextSquare # updates the current square for next time
        if questionFail==True:
            break
    return directions,holdDirections,holdCanvas,holdlinePlace,questionFail

def questions():
    doDifficultyAdvance=False
    instructionsInput=input("Hello welcome to this maths maze would you like to see the instructions\nYou can respond yes or no\n> ")
    if instructionsInput.lower()=="exit":
            exit()
    if instructionsInput.lower()=="yes":
        instructionsprint()
    while True:
        mazeSizeInput=input("How large would you like the maze to be\nYou can pick any option larger then 2 however any number above 10 may not display correctly\n> ")
        if mazeSizeInput.lower()=="exit":
            exit()
        try:
            mazeSizeInput=round(int(mazeSizeInput))
        except:
            print("Invalid input, please input just an integer greater than 2")
            continue
        if mazeSizeInput<3:
            continue
        break
    
    while True:
        difficulty=input('How difficult would you like the questions to be\nYou can pick "1", "2", "3" or "ADVANCED" for greater control\n> ')
        if difficulty.lower()=="exit":
            exit()
        try:
            difficulty=round(int(difficulty))
        except:
            if difficulty=="ADVANCED":
                doDifficultyAdvance=True
                difficulty=3
                break
            print('Invalid input, please input just "1", "2" or "3"')
            continue
        if difficulty<1 or difficulty>3:
            continue
        break
    randomQuestionSettings={
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
    if doDifficultyAdvance==True:
        randomQuestionSettings=difficultyadvanced(randomQuestionSettings)
    
    return mazeSizeInput,difficulty,randomQuestionSettings

def difficultyadvanced(randomQuestionSettings):
    while True:
        newUserChangeSettingAmount=""
        while True:
            userChangeSettingChoice=input(f"your current settings are {randomQuestionSettings}\nType what setting you would like to change, type done to exit menu\n> ")
            if userChangeSettingChoice.lower()=="exit":
                exit()
            if userChangeSettingChoice=="done":
                break
            if userChangeSettingChoice not in randomQuestionSettings:
                print("not a valid setting")
                continue
            break
        if userChangeSettingChoice=="done":
            break
        while True:
            userChangeSettingAmount=input("What would you like to change this setting to\n> ")
            if userChangeSettingAmount.lower()=="exit":
                exit()
            for i in userChangeSettingAmount:
                if i=="-":
                    newUserChangeSettingAmount=newUserChangeSettingAmount+i
                try:
                    i=int(i)
                    print(newUserChangeSettingAmount,12)
                    newUserChangeSettingAmount=newUserChangeSettingAmount+str(i)
                except ValueError:
                    continue
            print(newUserChangeSettingAmount)
            if len(newUserChangeSettingAmount)>0:
                break
        newUserChangeSettingAmount=int(newUserChangeSettingAmount)
        randomQuestionSettings[userChangeSettingChoice]=newUserChangeSettingAmount
    return randomQuestionSettings

def instructionsprint():
    print("instructions")

def start():
    global mazeSize
    mazeSize,difficulty,randomQuestionSettings=questions()
    lastSquare=0
    directions=[0] # directions used to know where the player has gone
    correctDirections=correctDirectionss() # get correct directions then print them, reset canvas and linePlace for player use
    linePlace=definelinePlace(mazeSize)
    canvas=[32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    while True:
        directions,holdDirections,holdCanvas,holdlinePlace,questionFail=maze(lastSquare,canvas,linePlace,directions,correctDirections,difficulty,randomQuestionSettings)
        print(questionFail)
        if questionFail==True:
            print("your settings made the game impossible and will restart")
            start()    
            exit()
        mazeCompleted=directions==correctDirections
        if mazeCompleted==True:
            print("sucsess")
            exit()
        else:
            directions=holdDirections.copy()
            canvas=holdCanvas.copy()
            linePlace=holdlinePlace.copy()
            print("you made a wrong turn and was placed back at last correct point")
            lastSquare=holdDirections[-1]
                            
start()