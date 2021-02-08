import pygame

class Game():

    def __init__(self,screenWidth,screenHeight):
        #creation du stockage d'input
        self.pressed = {}


    #FONCTION D'AFFICHAGE ECRAN
    def render(self,screen):
        
        screen.fill((250,0,0))
    
    #Fonction de verification des inputs
    def keyPressed(self,screenWidth, screenHeight):

        #input de deplacement: on bouge le joueur
        if(self.pressed.get(pygame.K_RIGHT)):
            print("right")
        if(self.pressed.get(pygame.K_LEFT)):
            print("left")
        if(self.pressed.get(pygame.K_DOWN)):
            print("down")
        if(self.pressed.get(pygame.K_UP)):
            print("up")

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