if __name__=='__main__':
    def start():
        while True:
            try:
                gh=int(input("> "))
                if 19>=gh>=13:
                    print("yay")
                    dowhat()
                else:
                    print("nay")
                    start()
            except ValueError:
                print("?")
                start()

    time=[]
    routine=[]
        
    def dowhat(): 
        gh=input("What do you want to improve on \nSleep, Money, Food, Hydration, exsistentialisim \n> ")
        if gh=="Sleep":
            print("deal with it who needs sleep anyway become a caffeine addict")
        elif gh=="Money":
            print("Get money")
        elif gh=="Food":
            print("stress eat")
        elif gh=="Hydration":
            print("try compete with youself for the clearest piss")
        elif gh=="exsistentialisim":
            print("there is nothing to do here you are invetibly going to die anyway nothing you do can fix this your life will be meaningless")
        else:
            print("English please")
            dowhat()
    
    start()