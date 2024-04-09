import random

avclassses = ["water", "fire", "plant"]
effektivclass = {
    "fire" : "plant",
    "plant" : "water",
    "water" : "fire"
}

class Player():
    def __init__(self, CharacterClass):
        if not checkOk(CharacterClass):
            exit()
        self.PC = CharacterClass
        self.PH = 100
        self.level = 1
        self.xp = 0
        self.Defnse = 1

class Enemy():
    def __init__(self, CharacterClass, maxHP):
        if not checkOk(CharacterClass):
            exit()
        self.PC = CharacterClass
        self.xp = random.randint(1,20)
        self.level = 1
        self.PH = random.randint(50, maxHP)
        self.Defnse = 1

def checkOk(Pclass):
    if Pclass in avclassses:
        return True
    else:
        return False

def checkmult(P1C, P2C):
    if effektivclass[P1C] == P2C :
        return 1.3
    elif effektivclass[P2C] == P1C:
        return 0.7
    else:
        return 1

def calcdamage(mult, P1A, P2H, Defnse):
    return round(P2H-((P1A*mult)/Defnse))

def calcDefnse(P1H, Defnse):
    nDefnse = round(Defnse+(100/P1H*0.5))
    if nDefnse<=15:
        return nDefnse
    else:
        return Defnse

def selattack(att, P1, P2):
    mult = checkmult(P1.PC, P2.PC)
    if att == 1:
        P1A = 10*P1.level
        P2H = P2.PH
        Defnse = P2.Defnse
        P2.PH = calcdamage(mult, P1A, P2H, Defnse)
    elif att == 2:
        P1A = 6*P1.level
        mult = mult*2
        P2H = P2.PH
        Defnse = P2.Defnse
        P2.PH = calcdamage(mult, P1A, P2H, Defnse)
    elif att == 3:
        P1A = random.randint(1,20)*P1.level
        mult = mult*random.randint(5, 20)*0.1
        P2H = P2.PH
        Defnse = P2.Defnse
        P2.PH = calcdamage(mult, P1A, P2H, Defnse)
    else:
        P1.Defnse = calcDefnse(P1.PH, P1.Defnse)
    return gamecheck(P1, P2)

def gamecheck(P1, P2):
    if P2.PH <= 0:
        P1.xp = P1.xp + P2.xp
        if P1.xp >= P1.level*10:
            P1.xp -= P1.level*10
            P1.level += 1
        P1.PH = 100
        return True
    else: 
        return False

if __name__=="__main__":
    oPlayer = Player(random.choice(avclassses))
    oEnemy = Enemy(random.choice(avclassses), 60)
    run = True
    print("Start demo")
    while run:
        print("Your live: " + str(oPlayer.PH))
        print("Enemy live: " + str(oEnemy.PH))
        att = int(input("Your Attack\n==> "))
        if att >4 or att <1:
            print("Demo broke")
            exit()
        Won = selattack(att, oPlayer, oEnemy)
        if Won == True:
            print("You Won")
            exit()
        print("Your live: " + str(oPlayer.PH))
        print("Enemy live: " + str(oEnemy.PH))
        Won = selattack(random.randint(1,4), oEnemy, oPlayer)
        if Won == True:
            print("You Lost")
            exit()