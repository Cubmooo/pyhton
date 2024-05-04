import random
import math
def randomquestions():   
    dificulty=3
    number1=0
    number2=0
    operations=["+","-","*","/"]
    operation=random.randint(0,2**dificulty)
    
    if operation==4 or operation==5:
        answer=random.randint(1,(dificulty-1)*8)
        number1=random.randint(1,(dificulty-1)*8)
        number2=random.randint(1,20)
        number3=eval(f"({number1}*{answer})+{number2}")
        print(str(number1),"x",str(number2),str(number3))
        print(answer)

    if operation==6 or operation==7:
        wordquestion=random.randint(0,1)
        if wordquestion==0:
            while True:
                number1hour=str(random.randint(0,20)).zfill(2)
                number1min=str(random.randint(0,59)).zfill(2)
                number2hour=str(int(number1hour)+random.randint(0,3)).zfill(2)
                number2min=str(random.randint(0,59)).zfill(2)
                answer=(60-int(number1min)+int(number2min))+60*(int(number2hour)-int(number1hour)-1)
                if answer<0:
                    continue
                break
            print(f"{number1hour}:{number1min} --> {number2hour}:{number2min}")
            print(answer)
        
        if wordquestion==1:
            geometrytype=random.randint(0,1)
            if geometrytype==0:
                number1=random.randint(1,20)
                number2=random.randint(1,math.floor(20-number1/2))
                answer=round((number1*number2)/2)
                print(number1,number2)
                print(answer)
            if geometrytype==1:
                maxcombinednumbervalue=20
                number1=random.randint(1,maxcombinednumbervalue-2)
                maxcombinednumbervalue-=number1
                number2=random.randint(1,maxcombinednumbervalue-1)
                maxcombinednumbervalue-=number2
                number3=random.randint(1,maxcombinednumbervalue)
                answer=number1*number2*number3
                print(number1,number2,number3)
                print(answer)
    
    if operation==2 or operation==3:
        number1=random.randint(1,(dificulty-1)*8)
        number2=random.randint(1,dificulty*8)
        answer=eval(f"{number1}*{number2}")
        print(number1,operation,number2)
        print(answer)
        if operation==3:
            numberhold=answer
            answer=number1
            number1=numberhold
            print(number1,operation,number2)
            print(answer)

    if operation==0 or operation==1:
        while True:
            number1=random.randint(1,10**dificulty)
            number2=random.randint(1,10**dificulty)
            answer=eval(f"{number1}{operations[operation]}{number2}")
            print(number1,operation,number2)
            print(answer)
            if answer<0 and dificulty==1:
                continue
            break
    checkmathsanswer(answer)
    
def checkmathsanswer(answer):
    pass
        
randomquestions()