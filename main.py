#======================================================================
#Fichier main de notre jeu en Python
#Dernière modification: 0/02/2021
#Developpeur: Jordy Gelb, Alexa Angerman, Mulin Sevan
#======================================================================

import pygame
pygame.init()

#génération fenetre de jeu

pygame.display.set_caption("Game")
pygame.display.set_mode((1080,720))

running = True

while running:

    #fermeture fenetre

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()