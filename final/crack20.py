import random
import math
import copy
#import libraries used
    
mazeSize=3 # define the size of the 

def definelinePlace(mazeSize): # define the variable called line place. this variable is used to create the print out of the maze. this creates this variable based on the maze size
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
    for u in range(mazeSize**2): # create a variable called canvas which is used to figure out the next avalible squares. this variable is a list of every square starting from 0 in the top left and adding oe each square going left to right top to bottom. negative are squares that have already been in
        canvas.append(u)
    canvas[0]=-1 # sets the starting point in the first square and marks it as have been in
    possibleSquares=[]
    actualSquares=[]
    possibleSquares.append(currentSquare+mazeSize) # gather all potential possible squares
    possibleSquares.append(currentSquare+1)
    possibleSquares.append(currentSquare-mazeSize)
    possibleSquares.append(currentSquare-1)
    
    for e in direction: # mark all squares that have been in 
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
 
 
 
    for i in directions: # runs through the directions turning it into the line place format.
        location+=1
        try:
            closeSquare=directions[location]
        except IndexError:
            lastspot=True
        line=math.floor(i/mazeSize)
        if lastspot==False:
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
 
 
    for u in range(mazeSize): #the previous section only added up or down not both. this area fixes this
        fixlinePlacePos=0
        for o in linePlace[u]:
            if fixlinePlacePos%3==0 and o==1:
                linePlace[u+1][fixlinePlacePos+1]=1
            if fixlinePlacePos%3==1 and o==1:
                linePlace[u-1][fixlinePlacePos-1]=1
            fixlinePlacePos+=1 
 
    for i in range((mazeSize*4)+1): # runs through each line adding the correct part to the output as specified by lineplace
        currentLine=""
        line=(math.floor(i/4))
        if i == 0 or i==(mazeSize*4):
            output=output+(wall*mazeSize+"■\n")
            continue
        newLineList=[]
        linePlacePos=0
        for e in (linePlace[line]):
            newLineList.append(e)
            if len(newLineList)==3:
                if i%4==0:
                    if newLineList[1]==1:
                        output=output+linefull
                    else:
                        output=output+lineempty
 
 
                if i%4==1: 
                    if newLineList[1]==1:
                        output=output+sidefull
                    else:
                        output=output+sideempty
 
                if i%4==3: 
                    if newLineList[0]==1:
                        output=output+sidefull
                    else:
                        output=output+sideempty
 
                if i%4==2:
                    if newLineList[2]==1 and previous2point==1:
                        output=output+midfullfull
                    elif newLineList[2]==1 and previous2point==0:
                        output=output+midrightfull
                    elif newLineList[2]==0 and previous2point==1:
                        output=output+midleftfull
                    elif newLineList[1]==1 or newLineList[0]==1:
                        output=output+midcenterfull
                    else:
                        output=output+fullempty
                    previous2point=newLineList[2] 
                newLineList.clear()  
            linePlacePos+=1
 
        output=output+currentLine+"■\n"
    print(output)
 
def correctDirectionss(): # define the correct direction before we start same prossces as normal directions
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
 
 
def check(correctDirections,directions): # checks if the directions taken are correct
    newcorrectDirections=[]
    pos=0
    try:
        for i in directions:
            newcorrectDirections.append(correctDirections[pos])
            pos+=1
    except:
        newcorrectDirections=["no"]
    return not newcorrectDirections==directions

def randomquestions(avaliblenextSquares,lastSquare,correctnextSquare,difficulty,randomQuestionSettings,directions,correctDirections): # creates the random maths questions
    questionFail=False
    userRestart=False
    try:
        number1=0
        number2=0
        operations=["+","-","*","/"]
        units=["cm","mm","m"]
        operation=random.randint(randomQuestionSettings["operationmin"],randomQuestionSettings["operation"])
        
        if operation==4 or operation==5: #algebra
            answer=random.randint(randomQuestionSettings["algebraadditionmin"],randomQuestionSettings["algebraadditionmax"])
            number1=random.randint(randomQuestionSettings["algebraadditionmin"],randomQuestionSettings["algebraadditionmax"])
            number2=random.randint(randomQuestionSettings["algebraadditionmin"],randomQuestionSettings["algebraadditionmax"])
            number3=eval(f"({number1}*{answer})+{number2}")
            print(f"If {number1}x + {number2} = {number3} what does X equal?")

        if operation==6:#time quesiton
            while True:
                number1hour=str(random.randint(0,20)).zfill(2)
                number1Min=str(random.randint(0,59)).zfill(2)
                number2Hour=str(int(number1hour)+random.randint(randomQuestionSettings['minhourdiffrence'],randomQuestionSettings['maxhourdiffrence'])).zfill(2)
                number2Min=str(random.randint(0,59)).zfill(2)
                answer=(60-int(number1Min)+int(number2Min))+60*(int(number2Hour)-int(number1hour)-1)
                if answer<0:
                    continue
                break
            number2Hourdisplay=number2Hour
            if int(number2Hour)>=24:
                number2Hourdisplay=int(number2Hour)%24
                number2Hourdisplay=str(number2Hourdisplay).zfill(2)
            print(f"If a train departed from its station at {number1hour}:{number1Min} and arrived at its desination at {number2Hourdisplay}:{number2Min} how long did the ride take?")
        
        if operation==7:
            unit=units[random.randint(0,2)]
            geometryType=random.randint(0,1)
            
            if geometryType==0:# geometry questions
                number1=random.randint(randomQuestionSettings['geotrianglemin'],randomQuestionSettings['geotrianglemax'])
                number2=random.randint(randomQuestionSettings['geotrianglemin'],math.floor(randomQuestionSettings['geotrianglemax']-number1/2))
                answer=round((number1*number2)/2)
                print(f"What is the volume of a TRIANGLE with a height of {number1}{unit} a width of {number2}{unit}?")
            if geometryType==1:
                number1=random.randint(randomQuestionSettings['geocubemin'],randomQuestionSettings['geocubecombinedmax']-2)
                randomQuestionSettings['geocubecombinedmax']-=number1
                number2=random.randint(randomQuestionSettings['geocubemin'],randomQuestionSettings['geocubecombinedmax']-1)
                randomQuestionSettings['geocubecombinedmax']-=number2
                number3=random.randint(randomQuestionSettings['geocubemin'],randomQuestionSettings['geocubecombinedmax'])
                answer=number1*number2*number3
                randomQuestionSettings['geocubecombinedmax']=20
                print(f"What is the volume of a CUBE with a height of {number1}{unit} a width of {number2}{unit} and a depth of {number3}{unit}?")
        
        if operation==2 or operation==3:#multiplication/division
            number1=random.randint(randomQuestionSettings['multiplicationmin'],randomQuestionSettings['multiplicationmax'])
            number2=random.randint(randomQuestionSettings['multiplicationmin'],randomQuestionSettings['multiplicationmax'])
            answer=eval(f"{number1}*{number2}")
            if operation==3:
                numberhold=answer
                answer=number1
                number1=numberhold
            print(f"What is {number1} {operations[operation]} {number2}?")

        if operation==0 or operation==1: #additon/subtraction
            while True:
                number1=random.randint(randomQuestionSettings['additionmin'],randomQuestionSettings['additionmax'])
                number2=random.randint(randomQuestionSettings['additionmin'],randomQuestionSettings['additionmax'])
                answer=eval(f"{number1}{operations[operation]}{number2}")
                if answer<0 and randomQuestionSettings['allownegativeaddition']==False:
                    continue
                break
            print(f"What is {number1} {operations[operation]} {number2}?")
        userAnswer,userExit,userRestart=checkmathsanswer(answer,avaliblenextSquares,lastSquare,correctnextSquare,directions,correctDirections)
        return userAnswer,difficulty,randomQuestionSettings,questionFail,userExit,userRestart
    except:
        userExit=False
        questionFail=True
        userAnswer=0
        return userAnswer,difficulty,randomQuestionSettings,questionFail,userExit,userRestart
    
def checkmathsanswer(answer,avaliblenextSquares,lastSquare,correctnextSquare,directions,correctDirections): #gives avalible options and check whether answer to the question is correct
    
    userExit=False
    phonyGiven=False
    randomNumber=random.randint(1,2)
    userRestart=False
    optionText=""
    potentialAnswers=[]
    newAvalibleNextSquare=[]
    answerFound=False
    holdPotentialAnswers=[]
    location=0
    for i in avaliblenextSquares:
        potentialAnswer=0
        if i==correctnextSquare and check(correctDirections,directions)==False:
            potentialAnswer=answer
            holdPotentialAnswers=[answer]+holdPotentialAnswers
        else:
            while True:
                potentialAnswer=answer+random.randint(-20,20)
                if potentialAnswer!=answer and potentialAnswer not in holdPotentialAnswers:
                    break
            holdPotentialAnswers.append(potentialAnswer)
    if answer not in holdPotentialAnswers:
        phonyGiven=True
        phonyCorrectNextSquare=avaliblenextSquares[random.randint(0,len(avaliblenextSquares)-1)]
        holdPotentialAnswers[0]=answer
    potentialAnswers=holdPotentialAnswers.copy()
    for i in avaliblenextSquares:
        if i==lastSquare+mazeSize:
            direction="down"           
        if i==lastSquare-mazeSize:
            direction="up"
        if i==lastSquare+1:
            direction="right"
        if i==lastSquare-1:
            direction="left"
        if correctnextSquare in avaliblenextSquares and check(correctDirections,directions)==False:
            if i==correctnextSquare:
                correctPotentialAnswer=potentialAnswers[0]
            else:
                if len(potentialAnswers)==3:
                    correctPotentialAnswer=potentialAnswers[randomNumber]
                    potentialAnswers.pop(randomNumber)
                else:
                    correctPotentialAnswer=potentialAnswers[1]
        else:
            if i==phonyCorrectNextSquare:
                    correctPotentialAnswer=potentialAnswers[0]
            else:
                if len(potentialAnswers)==3:
                        correctPotentialAnswer=potentialAnswers[randomNumber]
                        potentialAnswers.pop(randomNumber)
                else:
                    correctPotentialAnswer=potentialAnswers[1]
        optionText=optionText+str(correctPotentialAnswer)+",("+str(direction)+")  "
        location+=1
    potentialAnswers=holdPotentialAnswers.copy()
         
    for o in avaliblenextSquares:
        if phonyGiven==True:
            if o==phonyCorrectNextSquare:
                newAvalibleNextSquare=[o]+newAvalibleNextSquare
            else:
                newAvalibleNextSquare.append(o)
        else:
            if o==correctnextSquare:
                newAvalibleNextSquare=[o]+newAvalibleNextSquare
            else:
                newAvalibleNextSquare.append(o)
    if randomNumber==2 and len(potentialAnswers)==3:
        gh=newAvalibleNextSquare[1]
        newAvalibleNextSquare[1]=newAvalibleNextSquare[2]
        newAvalibleNextSquare[2]=gh
    while answerFound==False:
        intUserAnswer=""
        print(f"Your avalible options are {optionText}")
        userAnswer=input("> ")
        if userAnswer.lower()=="exit":
            userExit=True
            userMoveSquare=0
            break
        if userAnswer.lower()=="restart":
            userRestart=True
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
        intUserAnswerCheck=intUserAnswer.replace("-","")    
        if len(intUserAnswerCheck)==0:
            continue
        intUserAnswer=int(intUserAnswer)
        for u in range(len(potentialAnswers)):
            if intUserAnswer==potentialAnswers[u]:
                userMoveSquare=newAvalibleNextSquare[u]
                answerFound=True
                break
            else:
                continue
                
    return userMoveSquare,userExit,userRestart
        
def maze(lastSquare,linePlace,directions,correctDirections,difficulty,randomQuestionSettings): #runs all the diffrent parts of the maze each turn
    hold=False
    mazeDone=False
    while mazeDone==False:
        canvasprint(directions,linePlace)
        avaliblenextSquares=avalivlesquare(lastSquare,directions)
        if len(avaliblenextSquares)==0:
            break
        try:
            correctnextSquare=correctDirections[len(directions)]
        except:
            correctnextSquare=0
        nextSquare,difficulty,randomQuestionSettings,questionFail,userExit,userRestart=randomquestions(avaliblenextSquares,lastSquare,correctnextSquare,difficulty,randomQuestionSettings,directions,correctDirections)
        if userExit==True:
            exit()
        if userRestart==True:
            hold=False
            mazeDone=False
            lastSquare=0
            directions=[0]
            linePlace=definelinePlace(mazeSize)
            continue
        if hold==False:
            holdDirections=directions.copy()
            holdlinePlace=copy.deepcopy(linePlace)
        directions.append(nextSquare)
        hold=check(correctDirections,directions)
        lastSquare=nextSquare
        if questionFail==True:
            break
    return directions,holdDirections,holdlinePlace,questionFail

def questions(): # asks all the questions at the start
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
            print("Invalid input, please input just an integer greater than 2")
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
        'geotrianglemax':20,
        'minhourdiffrence':0,
        'maxhourdiffrence':3,
        'algebraadditionmin':1,
        'algebraadditionmax':20,
        'algebramultiplicationmin':1,
        'algebramultiplicationmax':(difficulty-1)*8,
        'operation':(2**difficulty)-1,
        'operationmin':0
    }  
    if doDifficultyAdvance==True:
        randomQuestionSettings=difficultyadvanced(randomQuestionSettings)
    
    return mazeSizeInput,difficulty,randomQuestionSettings

def difficultyadvanced(randomQuestionSettings):# allows the user to make fine changes to the question settings
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
            if userChangeSettingChoice=="allownegativeaddition":
                if userChangeSettingAmount=="False" or userChangeSettingAmount=="True":
                    randomQuestionSettings[userChangeSettingChoice]=eval(userChangeSettingAmount)
                    break
                continue
            else:
                for i in userChangeSettingAmount:
                    if i=="-":
                        newUserChangeSettingAmount=newUserChangeSettingAmount+i
                    try:
                        i=int(i)
                        newUserChangeSettingAmount=newUserChangeSettingAmount+str(i)
                    except ValueError:
                        continue
                if len(newUserChangeSettingAmount)>0:
                    break
        if userChangeSettingChoice=="allownegativeaddition":
            continue
        newUserChangeSettingAmount=int(newUserChangeSettingAmount)
        randomQuestionSettings[userChangeSettingChoice]=newUserChangeSettingAmount
    return randomQuestionSettings

def instructionsprint():# prints instructions 
    print("In this game you will be prompted with a maze without and barriers on where you can go.\n\
The correct directions will be told to you by the maths question given.\n\
Each maths question will have a few answers given which each correspond to a direction on the maze.\n\
Victory will be achieved once you follow the correct path all the way to the end.\n\
If at any point you make a wrong move the game tell you until you have reached the very end of your own path where it will inform of your mistake and take you to your last correct position.\n\
If at any time you would like to quit you can type exit or if you want to restart this maze you can type restart.\n\
You will now be prompted to enter the maze size and difficulty.\n\
The maze size will the change the length and height of the maze (it’s a square)\n\
and the difficulty changing how hard the questions are from basic additions and subtraction at level 1 to word problems and algebra to level 3.\n\
If you wanted finer control of the question and the difficulty you can instead type ADVANCED (caps sensitive).\n\
This will allow you to pick and change each individual setting.\n\
Good luck!")

def start(): # runs all the parts of the maze before and after the actual game part
    global mazeSize
    mazeSize,difficulty,randomQuestionSettings=questions()
    lastSquare=0
    directions=[0]
    correctDirections=correctDirectionss()
    linePlace=definelinePlace(mazeSize)
    
    while True:
        directions,holdDirections,holdlinePlace,questionFail=maze(lastSquare,linePlace,directions,correctDirections,difficulty,randomQuestionSettings)
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
            linePlace=holdlinePlace.copy()
            print("you made a wrong turn and was placed back at last correct point")
            lastSquare=holdDirections[-1]
                            
start()