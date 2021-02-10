import pygame
import random
from player import Player
from entite import *
from build import *

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
        self.chargementGame(screen,screenWidth,screenHeight)
        self.chargementSprite()
        #self.entity.append(carotte(2000,2000))
        #self.entity.append(tomate(1000,1000))
        #self.entity.append(carotte(500,500))
        #self.entity.append(tomate(600,600))
        #self.entity.append(carotte(3000,2000))
        #self.entity.append(tomate(1000,2000))

        self.listempo = []
        self.listempo.append(self.player)
        #Array de build
        self.builds = []
        #Gérer les vagues
        self.wavesStat = [[ 5, 2 , 1],[ 5, 1 , 0],[0, 5, 0],[3, 3, 0],[10, 0, 0],[3, 5, 1],[5, 3, 2],[7, 2, 1],[1, 8, 1],[3, 5, 2],[0, 6, 3],[0, 0, 5],[5, 5, 2]]
        self.waves = 0
        self.current_wave = self.wavesStat[self.waves]
        self.engame = True
        #Liste des entités mortes au combat
        self.deadList = []
        
    def gen_enemies(self):
        
        if sum(self.current_wave) == 0: #Tout les entity on été créer  
            if len(self.entity) == 0: #Tous les entity sont 
                if self.waves == 12:
                    self.current_wave = self.wavesStat[self.waves]
                    self.engame = False 
                else:    
                    self.waves +=1 #vague suivante
                    self.current_wave = self.wavesStat[self.waves]
                    self.engame = False        
        else:
            wave_enemies = [carotte(random.randrange(0,4000),0,self.spriteCarrote,self.spriteCarroteDeath),tomate(0,random.randrange(0,4000),self.spriteTomate),banane(random.randrange(0,4000),3500,self.spriteBanane)] #définition des types d'énemies et point d'apparition
            for i in range(len(self.current_wave)):
                if self.current_wave[i] != 0:
                    self.entity.append(wave_enemies[i]) #ajout
                    self.current_wave[i] = self.current_wave[i]-1
                    break
                    


    def update(self,screenWidth,screenHeight):
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "SoupeScreen"
            #nouvelle vague
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.engame = True
            #Créer un build
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                if self.player.barreCompetence.morClicable:
                    self.player.gold -= 200
                    self.builds.append(mortier(self.player.position[0],self.player.position[1],0,0,0,0))
                    
            #elif event.type == pygame.KEYDOM and event.key == pygame.K_e:
            #    self.builds.append(mur(self.player.position[0],self.player.position[1],0,0,0,0))
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
                text = font.render("chargement : "+str(compteur)+" % ", 1, (200,50,50))
                screen.fill((20,20,20))
                screen.blit(text, ((screenWidth/2)-text.get_rect().width, (screenHeight/2)-text.get_rect().height))
                pygame.display.flip()

    def chargementSprite(self):
        
        self.spriteCarrote=[]
        self.spriteCarroteDeath=[]
        self.spriteTomate=[]
        self.spriteBanane=[]
        self.spriteMur=[]
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

            for i in range(4):
                rect = (0,i*1024,416,1024)
                tempSprite = spriteCarroteDeath.image_at(rect)
                self.spriteCarroteDeath.append(pygame.transform.scale(tempSprite,(64,160)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
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
