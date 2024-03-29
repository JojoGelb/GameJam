#======================================================================
#Fichier main de notre jeu en Python
#Dernière modification: 0/02/2021
#Developpeur: Jordy Gelb, Alexa Angerman, Mulin Sevan
#======================================================================

import pygame
pygame.init()
import copy

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

horloge = horloge(screenWidth,screenHeight)

cinematique = Cinematique(screenWidth,screenHeight)

menuEnd = "null"

begining = False

#menuUpgrade = Upgrade(screenWidth,screenHeight,0)

instantiate = False



clock = pygame.time.Clock() #très importantnb de frame par tick 

while running:

    pygame.display.flip() #met à jour ce qu'il se trouve à l'écran
    
    clock.tick(80) #important
    
    if(GameState == "menu"):

        menu.render(screen) #affichage menu

        GameState = menu.action(screenWidth,screenHeight)    

    elif(GameState == "Cinematique"):
        cinematique.render(screen)
        GameState = cinematique.action(screenWidth,screenHeight)
    elif(GameState == "Play"):
        if(game == "null"):
            game = Game(screenWidth, screenHeight,screen)
        if(menuSoupe.Abus == True):
            menuSoupe.Abus = False
            game.reset = True
        
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
        GameState = menuSoupe.action(screenWidth,screenHeight)


    elif(GameState == "End"):

        if(menuEnd == "null"):
            menuEnd = Score(screenWidth,screenHeight,game.score)
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
        
    elif(GameState == "Horloge"):
        GameState = horloge.render(screen,screenWidth,screenHeight)

    elif(GameState == "Upgrade"):
        if(game == "null" ):
            if(instantiate != True):
                menuUpgrade = Upgrade(screenWidth,screenHeight,0,None)
                instantiate = True
                begining = True
        else:
            if (instantiate != True):
                menuUpgrade = Upgrade(screenWidth,screenHeight,game.player.gold,game.upgrade)
                instantiate = True

        GameState = menuUpgrade.action(screenWidth,screenHeight)
        menuUpgrade.render(screen)

        if(GameState != "Upgrade"):
            instantiate = False
            if begining == False:
                val =  copy.deepcopy(menuUpgrade.upgrade) 
                game.player.gold = menuUpgrade.gold
                game.applyUpgrade(val)

            else:
                begining = False
