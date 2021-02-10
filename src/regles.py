import pygame
from boutton import Boutton
from spritesheet import SpriteSheet
class regles:

    def __init__(self,screenWidth,screenHeight):
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.tinyfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',13)
        self.verybigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.rules = """
                    [utilisez Z-Q-S-D pour vous déplacer]

                      [utilisez les fleches pour tirer]

                 [Pour lancer la partie appuyez sur start] 

              [en premier lieu, boire la soupe n'a aucun effets]

            [Quand vous ne buvez pas la soupe la partie est lancée] 

                          [enfin, votre cauchemar] 

               [Plus vous restez, plus vous accumulez des malus]

    [mais vous gagnez un multiplicateur sur l'argent donné par les légumes]

         [toutes les minutes le jeu vous proposera de vous réveiller] 

         [si vous acceptez, vous pourrez alors dépenser votre argent]

    [Dans ce cas la Boire la soupe vous garantira une bonne nuit de sommeil] 

        [Vous perdrez ainsi vos malus, mais aussi votre multiplicateur]

        [Ne pas boire la soupe aura pour effet de conserver les effets]

            [Bah ouais, mal dormir n'est pas bon pour la santé]

               [votre score se calcule sur l'argent gagné]

                 [mais se réinitialise à chaque réveil]

       [un score élevé signifie que vous avez longtemps cauchemardé]
"""


        self.buttonMenu = Boutton(screenWidth*0.25,screenHeight*0.75,245,80,"Revenir à table")
    

    def render(self,screen):
        screen.fill((20,20,20))
        i=0
        x=-45
        y=5
        for ligne in self.rules.splitlines():
            i+=1
            screen.blit(self.smallfont.render(ligne,1,(200,50,50)),(x,y+i*20))


        screen.blit(self.buttonMenu.text,(1024*0.25,768*0.75))
 
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
                if self.buttonMenu.click(mos_x,mos_y):  
                    return "menu" #lance le jeu
        return "bebes"
