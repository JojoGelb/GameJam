import pygame
from player import Player


class Game():

    def __init__(self,screenWidth,screenHeight):
        #creation du stockage d'input
        self.pressed = {}

        #creation joueur
        self.player = Player(screenWidth,screenHeight)

        #Bordure de la map
        self.mapBorderLeft = -2000
        self.mapBorderRight = 2000
        self.mapBorderTop = -2000
        self.mapBorderBottom = 2000 #pbm
        self.xOffset = self.mapBorderLeft - self.player.position[0] + screenWidth/2
        self.yOffset = self.mapBorderTop - self.player.position[1] + screenHeight/2

        
        background = pygame.image.load("../textures/fondEcran.png")
        self.background = pygame.transform.scale(background,(self.mapBorderRight - self.mapBorderLeft,self.mapBorderBottom-self.mapBorderTop))




    #FONCTION D'AFFICHAGE ECRAN
    def render(self,screen,screenWidth,screenHeight):
        
        screen.fill((250,0,0))
        if not(self.player.position[0] < self.mapBorderLeft + screenWidth/2 or self.player.position[0] > self.mapBorderRight - screenWidth/2):
            self.xOffset = self.mapBorderLeft - self.player.position[0] + screenWidth/2

        if not(self.player.position[1] < self.mapBorderTop + screenHeight/2 or self.player.position[1] > self.mapBorderBottom - screenHeight/2):
            self.yOffset = self.mapBorderTop - self.player.position[1] + screenHeight/2
        
        screen.blit(self.background,(self.xOffset,self.yOffset))
        self.player.render(screen)
    
    #Fonction de verification des inputs
    def keyPressed(self):

        #input de deplacement: on bouge le joueur
        if(self.pressed.get(pygame.K_RIGHT)):
            self.player.move_right(self.mapBorderRight,self.mapBorderLeft + 540 ) #540 c'est screenWidth/2
        if(self.pressed.get(pygame.K_LEFT)):
            self.player.move_left(self.mapBorderLeft,self.mapBorderRight - 540)
        if(self.pressed.get(pygame.K_DOWN)):
            self.player.move_down(self.mapBorderBottom,self.mapBorderBottom - 360)
        if(self.pressed.get(pygame.K_UP)):
            self.player.move_up(self.mapBorderTop,self.mapBorderTop + 360) #-1640

    #Fonction d'enregistrement/gestion des inputs
    #La valeur retourné sera traité par le main afin qu'il puisse fermer le jeu correctement/remettre le menu
    def action(self,screenWidth,screenHeight):
        for event in pygame.event.get():
            #rage quit
            if event.type == pygame.QUIT:
                return "Quit"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"
            #enfoncement de touche
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                self.pressed[event.key] = True

            #Soulevement de touche
            elif event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                self.pressed[event.key] = False
        return "Play"