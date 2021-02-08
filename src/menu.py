import pygame
from boutton import Boutton
#from game import Game

class Menu:

    def __init__(self,screenWidth, screenHeight):
        self.buttonPlay = Boutton(290,300,500,80,"Play")
        self.buttonMenu = Boutton(290,400,245,80,"Settings")
        self.buttonQuit = Boutton(545,400,245,80,"Quit")
        self.background = pygame.transform.scale(pygame.image.load('../textures/mountain.jpg'),(screenWidth,screenHeight)) 
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini
    

    def render(self,screen):
        screen.blit(self.background, (0,0))
        self.buttonPlay.render(screen)
        self.buttonMenu.render(screen)
        self.buttonQuit.render(screen)

    def action(self,screenWidth,screenHeight):
        #ici récupération position de la souris
        mos_x, mos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:  
            #if the mouse is clicked on the  
            # button the game is terminated  
                if self.buttonPlay.click(mos_x,mos_y):  
                    pygame.mixer.music.stop()
                    #Lancement de la musique
                    pygame.mixer.music.load('../sound/music.wav')
                    pygame.mixer.music.play(-1) #pour tourner a l'infini
                    return "Play" #lance le jeu
                if self.buttonMenu.click(mos_x,mos_y):
                    pygame.mixer.music.stop()
                    return "Play"
                if self.buttonQuit.click(mos_x,mos_y): 
                    return "Quit"
                    pygame.quit()

        return "menu"