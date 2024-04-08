import random
comnum=0
playnum=0
rounds=2
def start():
    game()

def game(comnum,playnum):
        comnum=+dice()
        playnum=+dice()
        return comnum,playnum
        
def dice():
    comguess=random.randint(1,6)
    return comguess
def structure(comnum,playnum,rounds):
    for i in range(2):
        comguess,playguess=game(comnum,playnum)
        comnum=comnum+comguess
        playnum=playnum+playguess
        print(comnum,playnum)
    while rounds!=0:
        rounds=rounds-1
        comnum,playnum=game(comnum,playnum)
structure(comnum,playnum,rounds)
