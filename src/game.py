import pygame
import random
from player import Player
from entite import *

class Game():

    def __init__(self,screenWidth,screenHeight,screen):
        

        #creation du stockage d'input
        self.pressed = {}
        
        #creation joueur
        self.player = Player(screenWidth,screenHeight)

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

        self.entity.append(carotte(2000,2000))
        self.entity.append(tomate(1000,1000))
        self.entity.append(carotte(500,500))
        self.entity.append(tomate(600,600))
        self.entity.append(carotte(3000,2000))
        self.entity.append(tomate(1000,2000))
               
    
    def update(self,screenWidth,screenHeight):
        #detection si la touche est enfoncé ou non => deplacement joueur
        self.keyPressed(screenWidth,screenHeight)
        for entite in range(len(self.entity)):
           self.entity[entite].update(self.player.position[0],self.player.position[1])




    #FONCTION D'AFFICHAGE ECRAN
    def render(self,screen,screenWidth,screenHeight):
        
        screen.fill((250,0,0))

        screen.blit(self.background,(self.xOffset,self.yOffset))
        
        for entite in range(len(self.entity)):
            self.entity[entite].render(screen,self.xOffset,self.yOffset)

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
        if(self.pressed.get(pygame.K_RIGHT)):
            self.player.move_right(self.mapBorderRight,self.bordHorizontale) #540 c'est screenWidth/2
        if(self.pressed.get(pygame.K_LEFT)):
            self.player.move_left(self.mapBorderLeft,self.bordHorizontale)
        if(self.pressed.get(pygame.K_DOWN)):
            self.player.move_down(self.mapBorderBottom,self.bordVerticale)
        if(self.pressed.get(pygame.K_UP)):
            self.player.move_up(self.mapBorderTop,self.bordVerticale) #-1640
        
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
                #Lancement de la musique
                pygame.mixer.music.load('../sound/menu.wav')
                pygame.mixer.music.play(-1) #pour tourner a l'infini
                return "menu"
            #enfoncement de touche
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                self.pressed[event.key] = True

            #Soulevement de touche
            elif event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                self.pressed[event.key] = False
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
