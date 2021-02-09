import pygame
from boutton import Boutton
from spritesheet import SpriteSheet
#from game import Game

class Menu:

    def __init__(self,screenWidth, screenHeight):
        self.buttonPlay = Boutton(430,70,160,80,"Play")
        self.buttonCredit = Boutton(0,708,120,60,"Credit")
        self.buttonRegles = Boutton(914,688,110,80,"regles")
        self.background = pygame.transform.scale(pygame.image.load('../textures/Menu1.png'),(screenWidth,screenHeight)) 
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini
    

    def render(self,screen):
        screen.blit(self.background, (0,0))
        self.buttonPlay.render(screen)
        self.buttonCredit.render(screen)
        self.buttonRegles.render(screen)

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
                    pygame.mixer.music.set_volume(0.05)
                    return "Play" #lance le jeu
                if self.buttonCredit.click(mos_x,mos_y):
                    pygame.mixer.music.stop()
                    return "Credit"
                if self.buttonRegles.click(mos_x,mos_y): 
                    return "Regles"
                    pygame.quit()

        return "menu"

class Pause:

    def __init__(self,screenWidth, screenHeight):
        self.buttonBoire = Boutton(430,70,160,80,"Bu")
        self.buttonPasBu = Boutton(415,180,190,50,"PasBu")
        self.buttonQuit = Boutton(0,703,170,65,"Quit")
        self.buttonUpgrade = Boutton(390,270,90,30,"Upgrade")
        self.buttonBestiaire = Boutton(530,270,110,30,"Bestiare")
        self.background = pygame.transform.scale(pygame.image.load('../textures/Pause.png'),(screenWidth,screenHeight)) 
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini

    def render(self,screen):
        screen.blit(self.background, (0,0))
        self.buttonBestiaire.render(screen)
        self.buttonBoire.render(screen)
        self.buttonPasBu.render(screen)
        self.buttonUpgrade.render(screen)
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
                if self.buttonBoire.click(mos_x,mos_y):  
                    pygame.mixer.music.stop()
                    #Lancement de la musique
                    pygame.mixer.music.load('../sound/music.wav')
                    pygame.mixer.music.play(-1) #pour tourner a l'infini
                    pygame.mixer.music.set_volume(0.05)
                    return "Play" #lance le jeu
                if self.buttonPasBu.click(mos_x,mos_y):
                    pygame.mixer.music.stop()
                    #Lancement de la musique
                    pygame.mixer.music.load('../sound/music.wav')
                    pygame.mixer.music.play(-1) #pour tourner a l'infini
                    pygame.mixer.music.set_volume(0.05)
                    return "Play" #lance le jeu
                if self.buttonBestiaire.click(mos_x,mos_y):
                    return "Bestiare"
                if self.buttonUpgrade.click(mos_x,mos_y):
                    return "Upgrade"
                if self.buttonQuit.click(mos_x,mos_y): 
                    return "Quit"
                    pygame.quit()
                

        return "pause"

class Score:

    def __init__(self,screenWidth, screenHeight):
        self.buttonSave = Boutton(390,332,80,40,"Play")
        self.buttonSkip = Boutton(560,332,70,40,"Quit")
        self.background = pygame.transform.scale(pygame.image.load('../textures/score.png'),(screenWidth,screenHeight)) 
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini

    def render(self,screen):
        screen.blit(self.background, (0,0))
        self.buttonSave.render(screen)
        self.buttonSkip.render(screen)

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
                if self.buttonSave.click(mos_x,mos_y):
                    return "Save"
                if self.buttonSkip.click(mos_x,mos_y):
                    return "Skip"
        
        return "score"

class Credit:

    def __init__(self,screenWidth,screenHeight):
        bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.text0 = bigfont.render("Créateur" , True , (250,250,250))
        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.text1 = smallfont.render("Ingénieur son:                   Julien Houny" , True , (250,250,250))
        self.text2 = smallfont.render("Graphiste et game designer:      Sévan Mulin, Alexa Angermann" , True , (250,250,250))
        self.text3 = smallfont.render("Developpeur Gameplay:            Jordy Gelb" , True , (250,250,250))
        self.text4 = bigfont.render("On Remercie Aussi: " , True , (250,250,250))
        self.text5 = smallfont.render("Pour le graphisme:   \n Mariluz pour ses sur nos couleurs " , True , (250,250,250))
        self.text6 = smallfont.render("                     \n Un gas dans la rue qui semblait gentil" , True , (250,250,250))
        self.text7 = smallfont.render("                     \n La maman de Alexa qui aime les carrotes de Sevan" , True , (250,250,250))
        self.text8 = smallfont.render("Pour la musique  :   \n Des gens randoms que juliens à volé " , True , (250,250,250))
        self.text9 = smallfont.render("                     \n Rick ashley" , True , (250,250,250))
        self.text10 = smallfont.render("                     \n J'aime " , True , (250,250,250))
    
    def render(self,screen):
        screen.fill((20,0,0))
        screen.blit(self.text0,(425,25))
        screen.blit(self.text1,(100,100))
        screen.blit(self.text2,(100,125))
        screen.blit(self.text3,(100,150))

        screen.blit(self.text4,(300,250))

        screen.blit(self.text5,(70,350))
        screen.blit(self.text6,(70,375))
        screen.blit(self.text7,(70,400))

        screen.blit(self.text8,(70,450))
        screen.blit(self.text9,(70,475))
        screen.blit(self.text10,(70,500))


class bestiaire:

    def __init__(self,screenWidth,screenHeight):
        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        tinyfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',13)
        self.verybigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',100)
        background = pygame.image.load("../textures/fontbestiaire.png")
        self.background = pygame.transform.scale(background,(screenWidth+755,screenHeight+50))
        
        self.carotte = """attaque : au corp a corp ! se déplace :    viiiiite ! vie :           moyenne  !"""
        self.tomate = """attaque : explose        ! se déplace : normalement ! vie :          moyenne+  !"""
        self.ail = """attaque : au corp a corp ! se déplace :   lentement ! vie :           élevée   !"""
        self.bananne = """attaque : 'cune idée     ! se déplace :    idunno   ! vie :           ptetre   !"""       
        x=50
        y=150
        i=0
        for ligne in self.carotte.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))
        x=300
        y=150
        i=0
        for ligne in self.tomate.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))
        x=550
        y=150
        i=0
        for ligne in self.ail.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))
        x=800
        y=150
        i=0
        for ligne in self.bananne.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))

        sprite = SpriteSheet('../textures/Carotte.png')
        self.imagecarotte=(pygame.transform.scale(sprite.image_at((416,1024,416,1024)),(64,160)))

        sprite = SpriteSheet('../textures/elTomaty.png')
        self.imagetomate=(pygame.transform.scale(sprite.image_at((350,0,350,500)),(128,256)))



        
        self.text1 = smallfont.render("LA CAROTTE" , True , (250,250,250))
        self.text2 = smallfont.render("LA TOMATE" , True , (250,250,250))
        self.text3 = smallfont.render("L'AIL" , True , (250,250,250))
        self.text4 = smallfont.render("LA BANANNE" , True , (250,250,250))
        self.buttonMenu = Boutton(screenWidth*0.25,screenHeight*0.75,245,80,"Revenir à table")
    

    def render(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.text1,(50,100))
        screen.blit(self.text2,(300,100))
        screen.blit(self.text3,(550,100))
        screen.blit(self.text4,(800,100))
        self.background.blit(self.imagecarotte,(110,260))
        self.background.blit(self.imagetomate,(330,170))
        self.background.blit(self.verybigfont.render("?",1,(200,50,50)),(610,300))
        self.background.blit(self.verybigfont.render("?",1,(200,50,50)),(860,300))
        self.background.blit(self.buttonMenu.text,(1024*0.25,768*0.75))
 
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
        return "Bestiaire"

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

       [un score élevé signifie que vous avez longtemps cauchemardé] """


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
