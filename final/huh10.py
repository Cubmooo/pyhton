import random
import math
def randomquestions():   
    dificulty=3
    number1=0
    number2=0
    operations=["+","-","*","/"]
    units=["cm","mm","m"]
    operation=random.randint(0,(2**dificulty)-1)
    
    if operation==4 or operation==5:
        answer=random.randint(1,(dificulty-1)*8)
        number1=random.randint(1,(dificulty-1)*8)
        number2=random.randint(1,20)
        number3=eval(f"({number1}*{answer})+{number2}")
        print(f"If {number1}x + {number2} = {number3} what does X equal?")

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
            print(f"If a train departed from its station at {number1hour}:{number1min} and arrived at its desination at {number2hour}:{number2min} how long did the ride take?")
        
        if wordquestion==1:
            unit=units[random.randint(0,2)]
            geometrytype=random.randint(0,1)
            
            if geometrytype==0:
                number1=random.randint(1,20)
                number2=random.randint(1,math.floor(20-number1/2))
                answer=round((number1*number2)/2)
                print(f"What is the volume of a TRIANGLE with a height of {number1}{unit} a width of {number2}{unit}?")
            if geometrytype==1:
                maxcombinednumbervalue=20
                number1=random.randint(1,maxcombinednumbervalue-2)
                maxcombinednumbervalue-=number1
                number2=random.randint(1,maxcombinednumbervalue-1)
                maxcombinednumbervalue-=number2
                number3=random.randint(1,maxcombinednumbervalue)
                answer=number1*number2*number3
                print(f"What is the volume of a CUBE with a height of {number1}{unit} a width of {number2}{unit} and a depth of {number3}{unit}?")
    
    if operation==2 or operation==3:
        number1=random.randint(1,(dificulty-1)*8)
        number2=random.randint(1,dificulty*8)
        answer=eval(f"{number1}*{number2}")
        if operation==3:
            numberhold=answer
            answer=number1
            number1=numberhold
        print(f"What is {number1} {operations[operation]} {number2}?")

    if operation==0 or operation==1:
        while True:
            number1=random.randint(1,10**dificulty)
            number2=random.randint(1,10**dificulty)
            answer=eval(f"{number1}{operations[operation]}{number2}")
            print(f"What is {number1} {operations[operation]} {number2}?")
            if answer<0 and dificulty==1:
                continue
            break
        
    checkmathsanswer(answer)

def checkmathsanswer(answer):
    
        
randomquestions()