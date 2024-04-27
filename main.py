import random
import pygame

avclassses = ["water", "fire", "plant"]
effektivclass = {
    "fire" : "plant",
    "plant" : "water",
    "water" : "fire"
}

class Player():
    def __init__(self, CharacterClass, idle_image1, idle_image2):
        if not checkOk(CharacterClass):
            exit()
        self.PC = CharacterClass
        self.PH = 100
        self.level = 1
        self.xp = 0
        self.idle_image1 = idle_image1
        self.idle_image2 = idle_image2
        self.Defnse = 1
        self.X = 200
        self.Y = 200

class Enemy():
    def __init__(self, CharacterClass, maxHP, idle_image1, idle_image2):
        if not checkOk(CharacterClass):
            exit()
        self.PC = CharacterClass
        self.xp = random.randint(1,20)
        self.level = 1
        self.idle_image1 = idle_image1
        self.idle_image2 = idle_image2
        self.PH = random.randint(50, maxHP)
        self.Defnse = 1
        self.X = 200
        self.Y = 200

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
    arena1_background = loadimage("arena1.png", 800,600)
    start_background = loadimage("startscreen.png", 800, 600)
    water_idle_1 = loadimage("water_mage_idle_1.png", 128, 128)
    water_idle_2 = loadimage("water_mage_idle_2.png", 128, 128)
    fire_idle_1 = loadimage("fire_mage_idle_1.png", 128, 128)
    fire_idle_2 = loadimage("fire_mage_idle_2.png", 128, 128)
    plant_idle_1 = loadimage("plant_mage_idle_1.png", 128, 128)
    plant_idle_2 = loadimage("plant_mage_idle_2.png", 128, 128)
    lama_idle_1 = loadimage("lama_idle_1.png", 128, 128)
    lama_idle_2 = loadimage("lama_idle_2.png", 128, 128)
    fireball = loadimage("fireball.png", 32, 32)
    grassbob = loadimage("grass.png", 32, 32)
    bg = arena1_background
    startscreen = True
    selectchar = True
    momfight = False
    running = True
    ticker = 0
    charselectervar = random.randint(0,2)
    charselecterstringcords = [200, 336, 472]
    textcharselect = my_font.render('Please Chose a Character', False, (255, 255, 255))
    starttext1 = my_font.render('Game by Bonbon, Jakob, Patrick', False, (255, 255, 255))
    starttext2 = my_font.render('In Corparation with', False, (255, 255, 255))
    starttext3 = my_font.render('Special Thank to arGameplay', False, (255, 255, 255))
    while running:
        if startscreen:
            pygame.display.set_caption("Hypermux -Startscreen")
            screen.blit(start_background, (0,0))
            screen.blit(starttext1, (50,300))
            screen.blit(starttext2, (200, 400))
            screen.blit(starttext3, (50, 350))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        startscreen = False
            pygame.display.flip()
            clock.tick(10)
        elif selectchar:
            pygame.display.set_caption("Hypermux -Character Selection")
            screen.fill((0,0,0))
            if ticker >= 6:
                momsprite1 = water_idle_2
                momsprite2 = fire_idle_2
                momsprite3 = plant_idle_2
            else:
                momsprite1 = water_idle_1
                momsprite2 = fire_idle_1
                momsprite3 = plant_idle_1
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
                        momfight = True
                        if charselectervar == 0:
                            klasse = "water"
                            idle_image1 = water_idle_1
                            idle_image2 = water_idle_2
                        elif charselectervar == 1:
                            klasse = "fire"
                            idle_image1 = fire_idle_1
                            idle_image2 = fire_idle_2
                        else:
                            klasse = "plant"
                            idle_image1 = plant_idle_1
                            idle_image2 = plant_idle_2
                        Player = Player(klasse, idle_image1, idle_image2)
                        Enemy = Enemy("fire", 60, lama_idle_1, lama_idle_2)
            pygame.draw.rect(screen, (100,255,0), (charselecterstringcords[charselectervar], 300, 128, 128))
            if charselectervar == 0:
                screen.blit(momsprite1, (200,300))
                screen.blit(fire_idle_1, (336,300))
                screen.blit(plant_idle_1, (472,300))
            elif charselectervar == 1:
                screen.blit(water_idle_1, (200,300))
                screen.blit(momsprite2, (336,300))
                screen.blit(plant_idle_1, (472,300))
            elif charselectervar == 2:
                screen.blit(water_idle_1, (200,300))
                screen.blit(fire_idle_1, (336,300))
                screen.blit(momsprite3, (472,300))
            screen.blit(textcharselect, (260, 200))
            pygame.display.flip()
            clock.tick(10)
            if ticker == 10 :
                ticker = 0
            else: 
                ticker += 1
        elif momfight:
            pygame.display.set_caption("Hypermux -Fight")
            screen.blit(bg, (0,0))
            if ticker > 30:
                playerspr = Player.idle_image2
                enemyspr = Enemy.idle_image2
            else:
                playerspr = Player.idle_image1
                enemyspr = Enemy.idle_image2
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                pass
                            elif event.key == pygame.K_DOWN:
                                pass
                            elif event.key == pygame.K_RETURN:
                                pass
            pygame.display.flip()
            clock.tick(60)
            if ticker == 60:
                ticker = 0
            else:
                ticker += 1
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