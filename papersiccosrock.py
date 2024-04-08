import random
thing=["scissors","paper","rock","lizard","spock"]
history=[]
historry=[]
def start():
    gh=input('Welcome to rock paper scissors game\n Would you like to see instructions?\n  answer with "Yes" or "No"\n> ')
    if gh.lower()=="yes":
        instructions()
    elif gh.lower()=="no":
        pass 
    elif gh.lower()=="xxx":
        exit()
    else:
        print('Please enter "Yes" or "No"')
        start() 
    player1win,player2win=game()
    outro(player1win,player2win)
    
def instructions():
    print("Instructions")

def round():
    while True:
        gh=input('How many rounds would you like to play\n Your options are any plain number e.g. "1" or "2" or "infinite"\n> ')
        if gh.lower()=="infinite":
            rond=-1
            return rond
        elif gh.lower()=="xxx":
            exit()
        else:
            try:
                hg=int(gh)
                rond=hg
                if rond>0:
                    return rond
                else:
                    print("Please use a valid number")
            except Exception:
                print("your input wasn't accepted try again")


def game():
    player1win=0
    player2win=0
    rond=round()
    leftrounds=int(rond)
    displayleftrounds=""
    while True:
        if rond==0:
            return player1win,player2win
        rond=rond-1
        if not leftrounds>=0:
            displayleftrounds="infinite"
        else:
            displayleftrounds=str(rond)
        hg=input("What is your play\n> ")
        guess=0
        if hg.lower()=="scissors" or hg.lower()=="s":
            guess=1
        elif hg.lower()=="paper" or hg.lower()=="p":
            guess=2
        elif hg.lower()=="rock"or hg.lower()=="r": 
            guess=3
        elif hg.lower()=="lizard"or hg.lower()=="l":
            guess=4
        elif hg.lower()=="spock"or hg.lower()=="sp":
            guess=5
        elif hg.lower()=="xxx":
            rond=0
        else:
            print("Invalid input try again")
            rond=rond+1
        gh=random.randint(1,5)
        if guess>=1 and guess<=len(thing):
            if guess+4==gh or guess+2==gh or guess-1==gh or guess-3==gh:
                print(f"You lost\n You Picked {','.join(thing[guess-1:guess])} and the computer picked {','.join(thing[gh-1:gh])}\n  There are {displayleftrounds} rounds left")
                player2win=player2win+1
                history.append(','.join(thing[guess-1:guess]))
                historry.append(','.join(thing[gh-1:gh]))
            if guess+3==gh or guess+1==gh or guess-2==gh or guess-4==gh:
                print(f"You won\n You Picked {','.join(thing[guess-1:guess])} and the computer picked {','.join(thing[gh-1:gh])}\n  There are {displayleftrounds} rounds left")
                player1win=player1win+1
                history.append(','.join(thing[guess-1:guess]))
                historry.append(','.join(thing[gh-1:gh]))
            if guess==gh:
                print(f"You tied\n You Picked {','.join(thing[guess-1:guess])} and the computer picked {','.join(thing[gh-1:gh])}\n  There are {displayleftrounds} rounds left")
                history.append(','.join(thing[guess-1:guess]))
                historry.append(','.join(thing[gh-1:gh]))
                rond=rond+1
    
    
                
def outro(player1win,player2win):
    try:
        winrate=(player1win/(player1win+player2win))*100
    except Exception:
        winrate="Invalid "
    if player1win>player2win:
        print(f"Well done you won {player1win}-{player2win} Thats a {winrate}% win rate")
    elif player1win<player2win:
        print(f"Unfortunatly you lost {player1win}-{player2win}  Thats a {winrate}% win rate")
    else:
        print(f"The final result was {player1win}-{player2win}  Thats a {winrate}% win rate") 
    while True:
        gh=input(" Do you wont to see the history\n> ")
        if gh.lower()=="yes":
            for i in range(len(historry)):
                print(f"Round {i+1} results: you picked {','.join(history[i:i+1])} and the computer picked {','.join(historry[i:i+1])}")
            break
        elif gh.lower()=="no":
            break  
        else:
            print("invalid input")

start()