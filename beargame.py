#defining first(reusavblity)
def start():
    print("You are in a dark room with 2 doors which door do want to go down: ")
    print('Your options are "Door1" and "Door2" anything else and you will starve to death')
    gh = input("> ")#question then 
    print(gh)
    if gh=="Door1":
        oneafteroneone()
    elif gh=="Door2":
        oneafteronetwo()
    else:
        print("You Starved to death")
        print("Try again")
        start()
    
def oneafteroneone():
    print("There is a bear there eating chese cake what do you do?: ")
    print('Your options are "Take the cheesecake" and "Scream at the bear"')
    hg= input("> ")
    
    if hg=="Take the cheesecake":
        print("You your face becomes a snack for the bear")
        print("Try again")
        start()
    elif hg=="Scream at the bear":
        print("The bear eat's your legs and lets you bleed out")
        print("Try again")
        start()
    else:
        print("The bear smells you and release the stress on your neck")
        print("Try again")
        start()

def oneafteronetwo():
    print("You stare into the abyss of cthulhu retinas, Which insanity level would you like: ")
    print('Your options are "Level 1" "Level 2" "Level 3"')
    ghh= input("> ")
    if ghh=="Level 1":
        twoaftertwoone()
    elif ghh=="Level 2":
        twoaftertwotwo()
    elif ghh=="Level 3":
        twoaftertwothree()
    else:
        print("You had a heart attack and died to being scared")
        print("Try again")
        start()
        
def twoaftertwoone():
    print("It turn's out Cthulhu is acctully jsut blue berries, Do you carry on or turn around: ")
    print('Your options are "Carry on" "Turn back"')
    gh=input("> ")
    if gh=="Carry on":
        print("You fall into a pit and die")
        print("Try again")
        start()
    elif gh=="Turn back":
        print("you get back to the start succsefuly and relise there's a door behind the start to the outside where you excape")
        print("You survived but could you survive a diffrent way")
        print("Try again")
        start()
    else:
        print("Your deathly alergic to blueberries")
        print("Try again")
        start()
        
def twoaftertwotwo():
    print("It turn's out Cthulhu is acctully Yellow jackets, Do you carry on or turn around:")
    print('Your options are "Carry on" "Turn back"')
    gh=input(" ")
    if gh=="Carry on":
        print("You move onto the next room where you slowly move around the side of the pit before coming to another door")
        threeaftertwotwoone()        
    elif gh=="Turn back":
        print("You fall in a pit and die")
        print("Try again")
        start()
    else:
        print("You piss your pants so hard that you drown")
        print("Try again")
        start()
        
def twoaftertwothree():
    print("It turn's out Cthulhu is acctully really annoying medloies, Do you carry on or turn around:")
    print('Your options are "Carry on" "Turn back"')
    gh=input(" ")
    if gh=="Carry on":
        print("You move onto the next room where you slowly move around the side of the pit before coming to another door")
        threeaftertwothreeone()        
    elif gh=="Turn back":
        print("You fall in a pit and die")
        print("Try again")
        start()
    else:
        print("You piss your pants so hard that you drown")
        print("Try again")
        start()

def threeaftertwotwoone():
    print("The door has an ominous symbol on it do you carry on")
    print('Your options are "Carry on" "Turn back"')
    gh=input("> ")
    if gh=="Carry on":
        print("You touch the door and die")
        print("Try again")
        start()
    elif gh=="Turn back":
        print("you get back to the start succsefuly and relise there's a door behind the start to the outside where you excape")
        print("You survived but could you survive a diffrent way")
        print("Try again")
        start()
    else:
        print("You wait until you start coughing so ahrd you die")
        print("Try again")
        start()
        
def threeaftertwothreeone():
    print("The door has an ominous symbol on it do you carry on")
    print('Your options are "Carry on" "Turn back"')
    gh=input("> ")
    if gh=="Carry on":
        print("You touch the door walk through unscathed")
        fourafter2311()
    elif gh=="Turn back":
        print("As soon as you turn your back you trip so hard that you split your skull into and your brain falls out your head")
        print("Try again")
        start()
    else:
        print("You wait until you start coughing so ahrd you die")
        print("Try again")
        start()
        
def fourafter2311():
    print("There is nothing in the room what do you do?")
    print('Your options are "Carry on" "Turn back"')
    gh=input("> ")
    if gh=="Carry on":
        print("You just die suddenly and for semmingly no reason")
        print("Try again")
        start()
    elif gh=="Turn back":
        print("you get back to the start succsefuly and relise there's a door behind the start to the outside where you excape")
        print("You survived but could you survive a diffrent way")
        print("Try again")
        start()
    else:
        print("You wake up you have truly won")
        print("Congratulations you learned it was all just a dream")
        
start()#acctully useit
