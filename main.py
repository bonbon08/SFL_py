import random
import pygame

avclassses = ["water", "fire", "plant"]
effektivclass = {
    "fire" : "plant",
    "plant" : "water",
    "water" : "fire"
}

class Player():
    def __init__(self, CharacterClass, idle_image1, idle_image2, ball1_image, ball2_image, ball3_image, sword_image, special_image, Attacknames):
        if not checkOk(CharacterClass):
            exit()
        self.PC = CharacterClass
        self.PH = 100
        self.level = 1
        self.xp = 0
        self.idle_image1 = idle_image1
        self.idle_image2 = idle_image2
        self.ball_image1 = ball1_image
        self.ball_image2 = ball2_image
        self.ball_image3 = ball3_image
        self.sword_image = sword_image
        self.special_image = special_image
        self.Defnse = 1
        self.X = 150
        self.Y = 400
        self.Attacknames = Attacknames

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
        self.X = 600
        self.Y = 400

class Attboard():
    def __init__(self):
        self.counter = 0
        self.posses = [50, 100, 150, 200]

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
    return P1, P2

def gamecheck(P1, P2):
    P1.xp = P1.xp + P2.xp
    if P1.xp >= P1.level*10:
        P1.xp -= P1.level*10
        P1.level += 1
    P1.PH = 100
    return P1

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
    water_ball_1 = loadimage("water_mage_ball_1.png", 128, 128)
    water_ball_2 = loadimage("water_mage_ball_2.png", 128, 128)
    water_ball_3 = loadimage("water_mage_ball_3.png", 128, 128)
    water_sword = loadimage("water_sword.png", 64, 64)
    fire_idle_1 = loadimage("fire_mage_idle_1.png", 128, 128)
    fire_idle_2 = loadimage("fire_mage_idle_2.png", 128, 128)
    fire_ball_1 = loadimage("fire_mage_ball_1.png", 128, 128)
    fire_ball_2 = loadimage("fire_mage_ball_2.png", 128, 128)
    fire_ball_3 = loadimage("fire_mage_ball_3.png", 128, 128)
    fire_sword = loadimage("fire_sword.png", 64, 64)
    plant_idle_1 = loadimage("plant_mage_idle_1.png", 128, 128)
    plant_idle_2 = loadimage("plant_mage_idle_2.png", 128, 128)
    plant_ball_1 = loadimage("plant_mage_ball_1.png", 128, 128)
    plant_ball_2 = loadimage("plant_mage_ball_2.png", 128, 128)
    plant_ball_3 = loadimage("plant_mage_ball_3.png", 128, 128)
    plant_sword = loadimage("plant_sword.png", 64, 64)
    lama_idle_1 = loadimage("lama_idle_1.png", 128, 128)
    lama_idle_2 = loadimage("lama_idle_2.png", 128, 128)
    fireball = loadimage("fire_ball.png", 32, 32)
    grassball = loadimage("grass_ball.png", 32, 32)
    waterball = loadimage("water_ball.png", 32, 32)
    bow = loadimage("bow.png", 64, 64)
    arrow = loadimage("arrow.png", 64, 64)
    shield = loadimage("shield.png", 128, 128)
    shield_sound = pygame.mixer.Sound("data/sound/shield.wav")
    damage_sound = pygame.mixer.Sound("data/sound/damage.wav")
    pygame.mixer.music.load("data/sound/elsemusicloop.wav")
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.3)
    bg = arena1_background
    playanimation = False
    animation_type = 0
    character_mov = False
    character_mov_back = False
    animation_done = False
    startscreen = True
    selectchar = True
    momfight = False
    running = True
    objektX = 220
    objekt_show = False
    won = False
    ticker = 0
    Attboard = Attboard()
    attenemy = 0
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
                            Attacknames = ["Sword", "Arrow", "Waterblob", "Shield"]
                            idle_image1 = water_idle_1
                            idle_image2 = water_idle_2
                            ball1_image = water_ball_1
                            ball2_image = water_ball_2
                            ball3_image = water_ball_3
                            sword_image = water_sword
                            special_image = waterball
                        elif charselectervar == 1:
                            klasse = "fire"
                            Attacknames = ["Sword", "Arrow", "Fireball", "Shield"]
                            idle_image1 = fire_idle_1
                            idle_image2 = fire_idle_2
                            ball1_image = fire_ball_1
                            ball2_image = fire_ball_2
                            ball3_image = fire_ball_3
                            sword_image = fire_sword
                            special_image = fireball
                        else:
                            klasse = "plant"
                            Attacknames = ["Sword", "Arrow", "Dirtball", "Shield"]
                            idle_image1 = plant_idle_1
                            idle_image2 = plant_idle_2
                            ball1_image = plant_ball_1
                            ball2_image = plant_ball_2
                            ball3_image = plant_ball_3
                            sword_image = plant_sword
                            special_image = grassball
                        Player = Player(klasse, idle_image1, idle_image2, ball1_image, ball2_image, ball3_image, sword_image, special_image, Attacknames)
                        Enemy = Enemy("fire", 60, lama_idle_1, lama_idle_2)
                        pygame.mixer.music.load("data/sound/fightmusicloop.wav")
                        pygame.mixer.music.play(-1,0.0)
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
        elif playanimation:
            screen.blit(bg, (0,0))
            screen.blit(playerspr, (Player.X, Player.Y))
            if animation_type == 0 :
                enemyspr = Enemy.idle_image1
                if Attboard.counter == 0:
                    if ticker <= 5:
                        playerspr = Player.idle_image1
                    elif ticker <= 10:
                        playerspr = Player.ball_image1
                    elif ticker <= 15:
                        playerspr = Player.ball_image2
                    elif ticker <= 20:
                        playerspr = Player.ball_image3
                    else:
                        playerspr = Player.ball_image3
                        screen.blit(Player.sword_image, (Player.X+70, Player.Y+25))
                        character_mov = True
                    if character_mov == True:
                        if character_mov_back == False:
                            Player.X += 16
                            if Player.X >= Enemy.X-128:
                                pygame.mixer.Sound.play(damage_sound)
                                character_mov_back = True
                        else:
                            Player.X -= 16
                            if Player.X <= 150:
                                Player.X = 150
                                ticker = 360
                elif Attboard.counter == 1:
                    if ticker <= 5:
                        playerspr = Player.idle_image1
                    elif ticker <= 10:
                        playerspr = Player.ball_image1
                    elif ticker <= 15:
                        playerspr = Player.ball_image2
                    elif ticker <= 20:
                        playerspr = Player.ball_image3
                    else:
                        playerspr = Player.ball_image3
                        screen.blit(bow, (Player.X+70, Player.Y+25))
                        screen.blit(arrow, (objektX, Player.Y+25))
                        objekt_show = True
                        character_mov = True
                    if objekt_show == True:
                        objektX += 16
                        if objektX >= Enemy.X:
                            pygame.mixer.Sound.play(damage_sound)
                            ticker = 360
                elif Attboard.counter == 2:
                    if ticker <= 5:
                        playerspr = Player.idle_image1
                    elif ticker <= 10:
                        playerspr = Player.ball_image1
                    elif ticker <= 15:
                        playerspr = Player.ball_image2
                    elif ticker <= 20:
                        playerspr = Player.ball_image3
                    else:
                        playerspr = Player.ball_image3
                        screen.blit(Player.special_image, (objektX, Player.Y+25))
                        objekt_show = True
                        character_mov = True
                    if objekt_show == True:
                        objektX += 16
                        if objektX >= Enemy.X:
                            pygame.mixer.Sound.play(damage_sound)
                            ticker = 360
                elif Attboard.counter == 3:
                    playerspr = Player.idle_image1
                    if ticker <= 10:
                        pass
                    elif ticker <=40:
                        screen.blit(shield, (Player.X, Player.Y))
                    else:
                        pygame.mixer.Sound.play(shield_sound)
                        ticker = 360
            if animation_type == 1:
                enemyspr = Enemy.idle_image1
                playerspr = Player.idle_image1
                if attenemy == 3:
                    if ticker <= 10:
                        pass
                    elif ticker <=40:
                        screen.blit(shield, (Enemy.X, Enemy.Y))
                    else:
                        pygame.mixer.Sound.play(shield_sound)
                        ticker = 360
                else:
                    character_mov = True
                    if character_mov == True:
                        if character_mov_back == False:
                            Enemy.X -= 16
                            if Enemy.X <= Player.X+100:
                                pygame.mixer.Sound.play(damage_sound)
                                character_mov_back = True
                        else:
                            Enemy.X += 16
                            if Enemy.X >= 600:
                                Enemy.X = 600
                                ticker = 360
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
            screen.blit(enemyspr, (Enemy.X, Enemy.Y))
            pygame.display.flip()
            clock.tick(30)
            if ticker == 360:
                playanimation = False
                animation_done = True
                objektX = 220
                character_mov = False
                character_mov_back = False
                objekt_show = False
                ticker = 0
            else:
                ticker += 1
        elif momfight:
            if animation_done == True and animation_type == 0:
                playanimation = True
                animation_done = False
                animation_type = 1
                Player, Enemy = selattack(Attboard.counter+1, Player, Enemy)
            elif animation_done == True and animation_type == 1:
                animation_done = False
                attenemy = random.randint(0,3)
                Enemy, Player = selattack((attenemy+1), Enemy, Player)
            else:
                pygame.display.set_caption("Hypermux -Fight")
                screen.blit(bg, (0,0))
                pygame.draw.rect(screen, (0,92,152), (50,50,300,200))
                pygame.draw.rect(screen, (70,172,0), (50, Attboard.posses[Attboard.counter], 300,50))
                for i in range(0,4):
                    text  = my_font.render(Player.Attacknames[i], False, (255, 255, 255))
                    screen.blit(text, (50, Attboard.posses[i]))
                if ticker > 30:
                    playerspr = Player.idle_image2
                    enemyspr = Enemy.idle_image2
                else:
                    playerspr = Player.idle_image1
                    enemyspr = Enemy.idle_image1
                screen.blit(enemyspr, (Enemy.X, Enemy.Y))
                screen.blit(playerspr, (Player.X, Player.Y))
                text  = my_font.render(str(Player.PH) + " HP", False, (204, 100, 30))
                screen.blit(text, (180, 300 ))
                text  = my_font.render(str(Enemy.PH) + " HP", False, (204, 100, 30))
                screen.blit(text, (600, 300 ))
                for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    if Attboard.counter == 0:
                                        Attboard.counter = 3
                                    else: 
                                        Attboard.counter -= 1
                                elif event.key == pygame.K_DOWN:
                                    if Attboard.counter == 3:
                                        Attboard.counter = 0
                                    else: 
                                        Attboard.counter += 1
                                elif event.key == pygame.K_RETURN:
                                    playanimation = True
                                    ticker = 1
                                    animation_type = 0
                pygame.display.flip()
                clock.tick(60)
                if ticker == 60:
                    ticker = 0
                else:
                    ticker += 1
            if Player.PH < 1 :
                momfight = False
                won = False
            elif Enemy.PH < 1:
                momfight = False
                won = True
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