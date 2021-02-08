#======================================================================
#Fichier main de notre jeu en Python
#Dernière modification: 0/02/2021
#Developpeur: Jordy Gelb, Alexa Angerman, Mulin Sevan
#======================================================================

import pygame
pygame.init()

from game import Game
from menu import Menu

#génération fenetre de jeu
screenWidth = 1024
screenHeight = 768
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Game")

running = True

#creation du menu
menu = Menu(screenWidth,screenHeight)
#variable contenant le jeu
game = "null"
#etat du launcher : "Quit","menu","Play"
GameState = "menu"

clock = pygame.time.Clock() #très importantnb de frame par tick 

while running:
    
    clock.tick(80) #important
    
    if(GameState == "menu"):

        menu.render(screen) #affichage menu

        pygame.display.flip() #met à jour ce qu'il se trouve à l'écran

        GameState = menu.action(screenWidth,screenHeight)    

    elif(GameState == "Play"):
        if(game == "null"):
            game = Game(screenWidth, screenHeight,screen)
        
        game.render(screen,screenWidth,screenHeight)
        #detection si la touche est enfoncé ou non => deplacement joueur
        game.keyPressed(screenWidth,screenHeight)

        pygame.display.flip() #met à jour ce qu'il se trouve à l'écran

        #Ci dessous gestion des inputs
        GameState = game.action(screenWidth,screenHeight)
        
    elif(GameState == "Quit"):
        #on ferme la fenetre si demande de quit
        running = False
        pygame.quit()

    #print(GameState)