import pygame
import random
from player import Player
from entite import *
from build import *
import copy

# waves are in form
# frequency of enemies
# (# carrote, # tomate, # banane, # oignion)


class Game():

    def __init__(self,screenWidth,screenHeight,screen):
        

        #creation du stockage d'input
        self.pressed = {}
        
        #creation joueur
        self.player = Player(screenWidth,screenHeight)
        #Argent joueur
        self.modifGold = 1
        self.modifDeg = 1
        self.modifPV = 1

        self.score=0
        #array de mobs
        self.entity=[]
        #Bordure de la map
        self.mapBorderLeft = 0
        self.mapBorderRight = 4000
        self.mapBorderTop = 0
        self.mapBorderBottom = 4000


        #décalage caméra
        self.xOffset = self.mapBorderLeft - self.player.position[0] + screenWidth/2
        self.yOffset = self.mapBorderTop - self.player.position[1] + screenHeight/2

        #Pour gerer la camera du joueur
        self.bordVerticale=False
        self.bordHorizontale=False
        
        background = pygame.image.load("../textures/fondEcran.png")
        self.background = pygame.transform.scale(background,(self.mapBorderRight - self.mapBorderLeft,self.mapBorderBottom-self.mapBorderTop))
     
        #Chargement
        #self.chargementGame(screen,screenWidth,screenHeight)
        self.chargementSprite(screen,screenWidth,screenHeight)


        self.listempo = []
        self.listempo.append(self.player)
        #Array de build + stat pour upgrade
        self.builds = []
        self.PvMur = 1000
        self.DmgMitraille = 2
        self.DmgMortier = 10
        #Gérer les vagues
        self.wavesStat = [[ 3, 0 , 0],[ 5, 1 , 0],[0, 5, 0],[5, 5, 0],[10, 0, 0],[5, 5, 5]]
        self.waves = 0
        self.current_wave = []
        self.engame = True
        self.difficult = 1
        self.compVague = 0
        self.reset = False
        #Liste des entités mortes au combat
        self.deadList = []

        bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.affichageEntrevague = bigfont.render("Vague finit", True , (250,250,250))
        self.affichageEntre1vague = bigfont.render("Tappez sur ESPACE pour lancer", True , (250,250,250))
        self.affichageEntre2vague = bigfont.render("la vague suivante", True , (250,250,250))
        self.affichageEntre3vague = bigfont.render("Tappez sur ECHAP pour vous réveiller", True , (250,250,250))
        self.affichageEntre4vague = bigfont.render("et ameliorer vos constructions", True , (250,250,250))

        self.upgrade = [["Joueur",0],["Barricade",0],["Mortier",0],["Mitraillette",0]]
        self.dejaupgrade = [["Joueur",0],["Barricade",0],["Mortier",0],["Mitraillette",0]]
    def gen_enemies(self):


        if len(self.entity) == 0: #Tous les entity sont 
            if self.waves == 6:
                self.waves = 0
                self.difficult += 1
                self.current_wave = self.wavesStat[self.waves]
                self.engame = False 
                print(self.waves)
            else:   
                self.current_wave = self.wavesStat[self.waves]
                if self.difficult >=5:
                    for i in range(len(self.current_wave)):
                        self.current_wave[i] = self.current_wave[i]*(self.difficult-3)
                for i in range(len(self.current_wave)):
                    for j in range(self.current_wave[i]):
                        if self.difficult == 1:
                            if i == 0:
                                val = carotte(random.randrange(0,4000),0,self.spriteCarrote,self.spriteCarroteDeath,0,0,0,0)
                            elif i == 1:
                                val = tomate(0,random.randrange(0,4000),self.spriteTomate,0,0,0,0)
                            elif i == 2:
                                val = banane(random.randrange(0,4000),3500,self.spriteBanane,0,0,0,0)
                        else:
                            if i == 0:
                                val = carotte(random.randrange(0,4000),0,self.spriteCarrote,self.spriteCarroteDeath,(self.compVague%5+(self.difficult-1)),self.difficult,0,self.compVague%2)
                            elif i == 1:
                                val = tomate(0,random.randrange(0,4000),self.spriteTomate,(self.compVague%5+(self.difficult-1)),self.difficult,0,self.compVague%2)
                            elif i == 2:
                                val = banane(random.randrange(0,4000),3500,self.spriteBanane,(self.compVague%5+(self.difficult-1)),self.difficult,0,self.compVague%2)
                        self.entity.append(val)
                self.engame = False
                print(self.waves)
                self.compVague += 1  
                self.waves +=1 #vague suivante      
                    
                    
                    


    def update(self,screenWidth,screenHeight):

        if self.reset:
            self.difficult = 1
            self.player.vie = self.player.maxhealth
            self.reset = False
        
        if self.engame:
            self.gen_enemies()
       
       
        #detection si la touche est enfoncé ou non => deplacement joueur
        self.keyPressed(screenWidth,screenHeight)

        for i in range(len(self.entity)):
            if(self.entity[i].exist == False):
                del self.entity[i]
                break
        
        #update des construction
        for build in self.builds:
            build.update(self.entity)

        #destruction des construction
        for i in range(len(self.builds)):
            if(self.builds[i].exist == False):
                del self.builds[i]
                break
        
        #Dans la fonction upgrade
        EntiteDead = []

        for i in range(len(self.entity)):
            self.entity[i].update(self.listempo)
        
            #Détection des collisions des ennemis avec le joueurs : NE MARCHE PAS ENCORE
            #if pygame.sprite.collide_mask(self.player, self.entity[i]):
            #print(pygame.sprite.collide_mask(self.entity[2], self.entity[i]))


        #Si dans la liste des entités, une entités est morte en jeu, on l'ajoute dans la liste des entités mortes + on l'enlève de la liste des entités vivantes
            if not self.entity[i].exist:
                self.deadList.append(self.entity[i])
                EntiteDead.append(self.entity[i])
                self.player.gold +=  self.entity[i].gold*self.modifGold
                self.score += self.entity[i].gold*self.modifGold
                

        for entite in EntiteDead:
            self.entity.remove(entite)

        EntiteDead.clear()


        self.player.update(self.entity)





    #FONCTION D'AFFICHAGE ECRAN
    def render(self,screen,screenWidth,screenHeight):
        
        screen.fill((250,0,0))

        screen.blit(self.background,(self.xOffset,self.yOffset))
        
        for entite in range(len(self.entity)):
            self.entity[entite].render(screen,self.xOffset,self.yOffset)

        for deadEntite in range(len(self.deadList)):
            self.deadList[deadEntite].render(screen,self.xOffset,self.yOffset)
        
        for build in self.builds:
            build.render(screen,self.xOffset,self.yOffset)

        self.player.render(screen,self.xOffset,self.yOffset)

        if not(self.entity):
            screen.blit(self.affichageEntrevague,(375,50))
            screen.blit(self.affichageEntre1vague,(125,100))
            screen.blit(self.affichageEntre2vague,(275,150))
            screen.blit(self.affichageEntre3vague,(10,200))
            screen.blit(self.affichageEntre4vague,(100,250))

    #Fonction de verification des inputs
    def keyPressed(self,screenWidth,screenHeight):

        if not(self.player.position[0] < self.mapBorderLeft + screenWidth/2 or self.player.position[0] > self.mapBorderRight - screenWidth/2):
            self.xOffset = self.mapBorderLeft - self.player.position[0] + screenWidth/2
        
        else: 
            self.bordHorizontale = True
        if not(self.player.position[1] < self.mapBorderTop + screenHeight/2 or self.player.position[1] > self.mapBorderBottom - screenHeight/2):
            self.yOffset = self.mapBorderTop - self.player.position[1] + screenHeight/2
        else:
            self.bordVerticale = True

        #input de deplacement: on bouge le joueur
        if(self.pressed.get(pygame.K_d)):
            self.player.move_right(self.mapBorderRight,self.bordHorizontale) #540 c'est screenWidth/2
        if(self.pressed.get(pygame.K_q)):
            self.player.move_left(self.mapBorderLeft,self.bordHorizontale)
        if(self.pressed.get(pygame.K_s)):
            self.player.move_down(self.mapBorderBottom,self.bordVerticale)
        if(self.pressed.get(pygame.K_z)):
            self.player.move_up(self.mapBorderTop,self.bordVerticale)

        if(self.pressed.get(pygame.K_RIGHT)):
            self.player.shoot_right(self.mapBorderRight)
        if(self.pressed.get(pygame.K_LEFT)):
            self.player.shoot_left(self.mapBorderLeft)
        if(self.pressed.get(pygame.K_DOWN)):
            self.player.shoot_down(self.mapBorderBottom)
        if(self.pressed.get(pygame.K_UP)):
            self.player.shoot_up(self.mapBorderTop)
        
        
        self.bordVerticale = False
        self.bordHorizontale = False

    #Fonction d'enregistrement/gestion des inputs
    #La valeur retourné sera traité par le main afin qu'il puisse fermer le jeu correctement/remettre le menu
    def action(self,screenWidth,screenHeight):
        for event in pygame.event.get():
            #rage quit
            if event.type == pygame.QUIT:
                return "Quit"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.entity:
                return "SoupeScreen"
            #nouvelle vague
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.entity:
                self.engame = True
            #Créer un build
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if self.player.barreCompetence.morClicable:
                    self.player.gold -= 200
                    self.builds.append(mortier(self.player.position[0],self.player.position[1],0,self.DmgMortier,0,0))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                if self.player.barreCompetence.murClicable:
                    self.player.gold -= 50
                    self.builds.append(mur(self.player.position[0],self.player.position[1],self.PvMur,self.spriteMur))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if self.player.barreCompetence.mitrClicable:
                    self.player.gold -= 100
                    self.builds.append(mitraillette(self.player.position[0],self.player.position[1],0,self.DmgMitraille,0,0,self.spriteRolling))

            #enfoncement de touche
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_d or event.key == pygame.K_q or event.key == pygame.K_s or event.key == pygame.K_z or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                self.pressed[event.key] = True
            #Soulevement de touche
            elif event.type == pygame.KEYUP and (event.key == pygame.K_d or event.key == pygame.K_q or event.key == pygame.K_s or event.key == pygame.K_z or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                self.pressed[event.key] = False

        if(self.player.isDead == True):
            return "End"
        return "Play"

    def chargementGame(self,screen,screenWidth,screenHeight):

        lesDecors = SpriteSheet("../textures/decor.png")

        screen.fill((20,20,20))
        compteur=0
        font = pygame.font.Font("../textures/Perfect DOS VGA 437 Win.ttf", 36)
        fontiny = pygame.font.Font("../textures/Perfect DOS VGA 437 Win.ttf", 20)
        randomessage=["LE SAVIEZ-VOUS : Les Carottes sont polies, elle disent toujours bonjour","LE SAVIEZ-VOUS : Les Bannanes sont très dangeureuse, mais très lentes","ATTENTION les tomates exploses en mourant et font très mal","Dormez bien, pour un rythme plus sain","Mangez 5 fruits et légumes par jours !","La guerre c'est la paix","Ce jeu vous est proposé par Soviet entertainment","Jordy est salé","ET DIS MOI JAMMY !","Pour poser un mur taper [E] quand vous possèdez 50 gold","Pour poser un mortier taper [A] quand vous possèdez 200 gold"]
        texxxt=fontiny.render(randomessage[random.randrange(len(randomessage))], 1, (200,50,50))
        
        for undecor in range(1250):
            rand=random.randrange(5)
            if rand<2:
                rand=random.randrange(4)
            else:
                rand=20-random.randrange(5,20)

                self.background.blit( pygame.transform.scale( pygame.transform.flip(lesDecors.image_at( (0,rand*1024,1024,1024) ),random.choice([True, False]),0) ,(128,128) ), (random.randrange(4000),random.randrange(4000)) )            
            if undecor%12==0:
                compteur+=1
                if compteur > 100 : compteur = 100
                text = font.render("génération du terrain : "+str(compteur)+" % ", 1, (200,50,50))
                screen.fill((20,20,20))
                screen.blit(text, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
                screen.blit(texxxt, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height-100))
                pygame.display.flip()

    def chargementSprite(self,screen,screenWidth,screenHeight):
        
        #ecran charge
        font = pygame.font.Font("../textures/Perfect DOS VGA 437 Win.ttf", 36)
        text = font.render("chargement des sprites : "+str(0)+" % ", 1, (200,50,50))
        fontiny = pygame.font.Font("../textures/Perfect DOS VGA 437 Win.ttf", 20)
        texxxt=fontiny.render("Preparez vous !", 1, (200,50,50))
        screen.blit(texxxt, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height-100))
        screen.fill((20,20,20))
        screen.blit(text, (((int(screenWidth*0.75)))-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
        pygame.display.flip()
        pygame.time.wait(300)
        #ecran charge

        self.spriteCarrote=[]
        self.spriteCarroteDeath=[]
        self.spriteTomate=[]
        self.spriteBanane=[]
        self.spriteMur=[]
        self.spriteRolling=[]
        #self.spriteTomateDeath=[]

        
        #Sprite Carotte
        try:
            spriteCarrote = SpriteSheet('../textures/Carotte.png')
            spriteCarroteDeath = SpriteSheet('../textures/Carottedodo.png') 

            for i in range(2):
                for j in range(2):
                    rect = (i*416,j*1024,416,1024)
                    tempSprite = spriteCarrote.image_at(rect)
                    self.spriteCarrote.append(pygame.transform.scale(tempSprite,(64,160)))

            #ecran charge
            text = font.render("chargement des sprites : "+str(20)+" % ", 1, (200,50,50))
            screen.fill((20,20,20))
            screen.blit(text, (((int(screenWidth*0.75)))-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
            screen.blit(texxxt, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height-100))
            pygame.display.flip()
            pygame.time.wait(300)
            #ecran charge

            for i in range(4):
                rect = (0,i*1024,416,1024)
                tempSprite = spriteCarroteDeath.image_at(rect)
                self.spriteCarroteDeath.append(pygame.transform.scale(tempSprite,(64,160)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        #ecran charge
        text = font.render("chargement des sprites : "+str(40)+" % ", 1, (200,50,50))
        screen.fill((20,20,20))
        screen.blit(text, (((int(screenWidth*0.75)))-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
        screen.blit(texxxt, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height-100))
        pygame.display.flip()
        pygame.time.wait(300)
        #ecran charge

        #Sprite Tomate
        try:
            spriteTomate = SpriteSheet('../textures/elTomaty.png')

            for i in range(14):
                rect = (i*350,0,350,500)
                tempSprite = spriteTomate.image_at(rect)
                self.spriteTomate.append(pygame.transform.scale(tempSprite,(128,256)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        #ecran charge
        text = font.render("chargement des sprites : "+str(60)+" % ", 1, (200,50,50))
        screen.fill((20,20,20))
        screen.blit(text, (((int(screenWidth*0.75)))-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
        screen.blit(texxxt, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height-100))      
        pygame.display.flip()
        pygame.time.wait(300)
        #ecran charge

        #Sprite Banane
        try:
            spriteBanane = SpriteSheet('../textures/Banane.png')

            for i in range(4):
                rect = (i*350,0,350,350)
                tempSprite = spriteBanane.image_at(rect)
                self.spriteBanane.append(pygame.transform.scale(tempSprite,(256,256)))
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
       
        #Sprite mur
        try:
            spriteMur = SpriteSheet('../textures/Barricade.png')

            for i in range(6):
                rect = (0,i*704,704,704)
                tempSprite = spriteMur.image_at(rect)
                self.spriteMur.append(pygame.transform.scale(tempSprite,(100,100)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        try:
            spriteRollin = SpriteSheet("../textures/Rolling_Stone.png")

            for j in range(10):
                rect = (j*200,0,200,200)
                tempSprite = spriteRollin.image_at(rect)
                self.spriteRolling.append(pygame.transform.scale(tempSprite,(64,64)))
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


        #ecran charge
        wololo=60
        while wololo<=100:
            pygame.time.wait(28)
            text = font.render("chargement des sprites : "+str(wololo)+" % ", 1, (200,50,50))
            screen.fill((20,20,20))
            screen.blit(text, (((int(screenWidth*0.75)))-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
            screen.blit(texxxt, ((int(screenWidth*0.75))-text.get_rect().width, (screenHeight/2)-text.get_rect().height-100))           
            pygame.display.flip()
            wololo+=1
        #ecran charge


    def applyUpgrade(self,Upgrade):

        val = []
  
        for i in  range(len(self.upgrade)):
            val.append(Upgrade[i][1] - self.dejaupgrade[i][1])

        

        for i in range(len(self.upgrade)):
            if i == 0:
                self.player.maxhealth = self.player.maxhealth + val[i]
                self.player.barreCompetence.VieMax += val[i]
                self.player.vie += val[i]
                if val[i]%5 == 0:
                   self.player.attack = self.player.attack + (val[i]/5)
                   self.player.velocity = self.player.velocity + (val[i]/5)
            elif i == 1:
                self.PvMur = self.PvMur + (val[i]*100)
                for i in range(len(self.builds)):
                    if self.builds[i].__class__.__name__ == "mur":
                        self.builds[i].vie = self.PvMur
            elif i == 2:
                self.DmgMortier = self.DmgMortier + val[i]
                for i in range(len(self.builds)):
                    if self.builds[i].__class__.__name__== "mortier":
                        self.builds[i].degats = self.DmgMortier
            elif i ==3:
                self.DmgMitraille = self.DmgMitraille + val[i]
                for i in range(len(self.builds)):
                    if self.builds[i].__class__.__name__== "mitraillette":
                        self.builds[i].degats = self.DmgMitraille

        self.upgrade = copy.deepcopy(Upgrade)
        self.dejaupgrade = copy.deepcopy(Upgrade)
        
                
