import random
def randomquestions():   
    dificulty=3
    number1=0
    number2=0
    operations=["+","-","*","/"]
    operation=random.randint(0,2**dificulty)
    suitableanswer=False
    
    if operation==4 or operation==5:
        answer=random.randint(1,(dificulty-1)*8)
        number1=random.randint(1,(dificulty-1)*8)
        number2=random.randint(1,20)
        number3=eval(f"({number1}*{answer})+{number2}")
        print(str(number1),"x",str(number2),str(number3))
        print(answer)

    if operation==6 or operation==7:
        print("Test")
        
    
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
        while suitableanswer==False:
            number1=random.randint(1,10**dificulty)
            number2=random.randint(1,10**dificulty)
            answer=eval(f"{number1}{operations[operation]}{number2}")
            print(number1,operation,number2)
            print(answer)
            if answer<0 and dificulty==1:
                continue
            suitableanswer+=True
        
randomquestions()