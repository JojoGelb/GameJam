#======================================================================
#Fichier main de notre jeu en Python
#Dernière modification: 0/02/2021
#Developpeur: Jordy Gelb, Alexa Angerman, Mulin Sevan
#======================================================================

import pygame
pygame.init()

from game import Game
from menu import *

#génération fenetre de jeu
screenWidth = 1024
screenHeight = 768
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Game")

running = True
primeravez=0

#creation du menu
menu = Menu(screenWidth,screenHeight)
#variable contenant le jeu
game = "null"
#etat du launcher : "Quit","menu","Play",Bestiaire,Pause,Score,Credit
GameState = "menu"

credit = Credit(screenWidth,screenHeight)

menuRegle = regles(screenWidth,screenHeight)

menuSoupe = Pause(screenWidth,screenHeight)

bestiaire = bestiaire(screenWidth,screenHeight)

menuEnd = "null"

playerScore = 0

clock = pygame.time.Clock() #très importantnb de frame par tick 

while running:

    pygame.display.flip() #met à jour ce qu'il se trouve à l'écran
    
    clock.tick(80) #important
    
    if(GameState == "menu"):

        menu.render(screen) #affichage menu

        GameState = menu.action(screenWidth,screenHeight)    

    elif(GameState == "Play"):
        primeravez=1
        if(game == "null"):
            game = Game(screenWidth, screenHeight,screen)
        
        game.render(screen,screenWidth,screenHeight)

        game.update(screenWidth,screenHeight)

        #Ci dessous gestion des inputs
        GameState = game.action(screenWidth,screenHeight)
        
    elif(GameState == "Quit"):
        #on ferme la fenetre si demande de quit
        running = False
        pygame.quit()
    elif(GameState == "Bestiaire"):
        bestiaire.render(screen)
        GameState = bestiaire.action(screenWidth,screenHeight)

    elif(GameState == "Credit"):
        credit.render(screen)
        GameState=  credit.action()

    elif(GameState == "Regles"):
        menuRegle.render(screen)
        GameState = menuRegle.action(screenWidth,screenHeight)

    elif(GameState == "SoupeScreen"):
   
        menuSoupe.render(screen)
        if primeravez==1:
            if playerScore<game.score:
                playerScore=game.score
        GameState = menuSoupe.action(screenWidth,screenHeight)


    elif(GameState == "End"):

        if playerScore<game.score:
            playerScore=game.score
        if(menuEnd == "null"):
            menuEnd = Score(screenWidth,screenHeight,playerScore)
        menuEnd.render(screen)
        GameState = menuEnd.action(screenWidth,screenHeight)
    elif(GameState == "restart"):
        #Enclencher la sauvegarde
        game = "null"
        primeravez=0
        menu = Menu(screenWidth,screenHeight)
        menuSoupe = Pause(screenWidth,screenHeight)
        menuEnd = "null"
        GameState = "menu"


    
    #print(GameState)