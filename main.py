import random
import pygame

avclassses = ["water", "fire", "plant"]
effektivclass = {
    "fire" : "plant",
    "plant" : "water",
    "water" : "fire"
}

class Player():
    def __init__(self, CharacterClass, image):
        if not checkOk(CharacterClass):
            exit()
        self.PC = CharacterClass
        self.PH = 100
        self.level = 1
        self.xp = 0
        self.image = image
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

def loadimage(image, height, width):
    return pygame.transform.scale(pygame.image.load("data/images/" + image), (height, width))

if __name__=="__main__":
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Sans Bold', 32)
    screen = pygame.display.set_mode((800,600))
    applogo = pygame.image.load("data/images/applogo.png")
    clock = pygame.time.Clock()
    pygame.display.set_caption("Hypermux")
    pygame.display.set_allow_screensaver(False)
    pygame.display.set_icon(applogo)
    running = True
    arena1_background = loadimage("arena1.png", 800,600)
    start_background = loadimage("startscreen.png", 800, 600)
    char1 = loadimage("water_mage_idle_1.png", 128, 128)
    char2 = loadimage("fire_mage_idle_1.png", 128, 128)
    char3 = loadimage("plant_mage_idle_1.png", 128, 128)
    startscreen = True
    selectchar = True
    textcharselect = my_font.render('Please Chose a Character', False, (255, 255, 255))
    charselectervar = random.randint(0,2)
    charselecterstringcords = [200, 336, 472]
    while running:
        if startscreen:
            screen.blit(start_background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        startscreen = False
            pygame.display.flip()
            clock.tick(10)
        elif selectchar:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if charselectervar != 0 :
                            charselectervar -= 1
                        else:
                            charselectervar = 2
                    if event.key == pygame.K_RIGHT:
                        if charselectervar != 2:
                            charselectervar += 1
                        else:
                            charselectervar = 0
                    if event.key == pygame.K_RETURN:
                        selectchar = False
                        if charselectervar == 0:
                            klasse = "water"
                            image = char1
                        elif charselectervar == 1:
                            klasse = "fire"
                            image = char2
                        else:
                            klasse = "plant"
                            image = char3
                        Playerclass = Player(klasse, image)
            pygame.draw.rect(screen, (255,255,0), (charselecterstringcords[charselectervar], 300, 128, 128))
            screen.blit(char1, (200,300))
            screen.blit(char2, (336,300))
            screen.blit(char3, (472,300))
            screen.blit(textcharselect, (260, 200))
            pygame.display.flip()
            clock.tick(10)
        else:
            screen.blit(arena1_background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass
                    elif event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_RETURN:
                        pass
            pygame.display.flip()
            clock.tick(60)
    pygame.quit()
    """oPlayer = Player(random.choice(avclassses))
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
            exit()"""