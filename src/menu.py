import pygame
from boutton import Boutton
from spritesheet import SpriteSheet
#from game import Game

class Menu:

    def __init__(self,screenWidth, screenHeight):
        self.buttonPlay = Boutton(430,70,160,80,"Play")
        self.buttonCredit = Boutton(0,708,120,60,"Credit") #possiblement retirable
        self.buttonRegles = Boutton(914,688,110,80,"regles")
        self.background = pygame.transform.scale(pygame.image.load('../textures/Menu1.png'),(screenWidth,screenHeight)) 
        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini
        pygame.mixer.music.set_volume(0.1)
        scores2 = []
        try:
            fichier = open("../HighScore.txt", "r")
            scores = fichier.readlines()
            #print(scores)
            fichier.close

            for i in range (len(scores)):
                scores2.append(scores[i].split(':'))
            
            trie = False
            self.scoresAffichage = []
            while(trie == False):
                trie = True
                for j in range(len(scores2)-1):
                    val = int(scores2[j][1]) < int(scores2[j+1][1])
                    if val == True:
                        scores2[j],scores2[j+1] = scores2[j+1],scores2[j]
                        trie  = False 
                        break

            val = len(scores2)
            if val > 9 :
                val = 9

            for i in range(val):
                val = scores2[i][0] +" : " + scores2[i][1]
                self.scoresAffichage.append(smallfont.render(val[:-1], True , (250,250,250)))

        except:
            print("Erreur fichier highscore")
                

            
    

    def render(self,screen):
        screen.blit(self.background, (0,0))
        for i in range(len(self.scoresAffichage)):
            screen.blit(self.scoresAffichage[i],(375,i*50 + 300))

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
                    return "Cinematique" #return "Play" #lance le jeu
                if self.buttonCredit.click(mos_x,mos_y):
                    #pygame.mixer.music.stop()
                    return "Credit"
                if self.buttonRegles.click(mos_x,mos_y): 
                    return "Regles"
                    pygame.quit()

        return "menu"

class Pause:

    def __init__(self,screenWidth, screenHeight):
        self.background = pygame.transform.scale(pygame.image.load('../textures/Pause.png'),(screenWidth,screenHeight)) 
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini
        self.Abus = False

        self.clickTips1 = False
        
        self.verybigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',60)
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',18)
        self.tips1 = """ 
        Cliquer sur boire vous 
         permettra de passer 
            une bonne nuit

        Point de vie restauré
    Difficulté cauchemard remis à 0
   Multiplicateur de Gold remis à 0"""

        self.clickTips2 = False

        self.tips2 = """
      Choisissez de ne pas boire
       et votre nuit sera agité

        Point de vie inchangé
    Difficulté augmente doucement
   Multiplicateur de Gold augmente"""
    def render(self,screen):
        screen.blit(self.background, (0,0))

        #pygame.draw.rect (self.background,(250,250,250),(350,75,30,50))
        #pygame.draw.rect (self.background,(250,250,250),(350,175,30,50))

        self.background.blit(self.verybigfont.render("?",1,(200,50,50)),(350,75))
        self.background.blit(self.verybigfont.render("?",1,(200,50,50)),(350,175))
        
        if(self.clickTips1):
            pygame.draw.rect(screen,(250,250,250),(5,50,340,125))
            i=0
            x=-12
            y=25
            for ligne in self.tips1.splitlines():
                i+=1
                screen.blit(self.smallfont.render(ligne,1,(0,0,0)),(x,y+i*15))
        
        if(self.clickTips2):
            pygame.draw.rect(screen,(250,250,250),(5,175,340,125))
            i=0
            x=-20
            y=150
            for ligne in self.tips2.splitlines():
                i+=1
                screen.blit(self.smallfont.render(ligne,1,(0,0,0)),(x,y+i*15))

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
                if mos_x> 430 and mos_x < 590 and mos_y > 70 and mos_y < 150: #Bouton boire 
                    self.Abus =True
                    return "Horloge" #Bouton boire

                elif mos_x> 415 and mos_x < 605 and mos_y > 180 and mos_y < 230: #bouton pas boire
                    return "Play" #lance le jeu
                if mos_x> 530 and mos_x < 640 and mos_y > 270 and mos_y < 300:
                    return "Bestiaire"
                if mos_x> 390 and mos_x < 480 and mos_y > 270 and mos_y < 300:
                    return "Upgrade"
                if mos_x> 0 and mos_x < 170 and mos_y > 703 and mos_y < 768:
                    return "restart"
                if mos_x> 350 and mos_x < 380 and mos_y > 75 and mos_y < 125:
                    if self.clickTips1 == True:
                        self.clickTips1 = False
                    elif self.clickTips1 == False:
                        self.clickTips1=True
                if mos_x> 350 and mos_x < 380 and mos_y > 175 and mos_y < 225:
                    if self.clickTips2 == True:
                        self.clickTips2 = False
                    elif self.clickTips2 == False:
                        self.clickTips2=True
                
                

        return "SoupeScreen"

class Score:

    def __init__(self,screenWidth, screenHeight, score):
        self.background = pygame.transform.scale(pygame.image.load('../textures/score.png'),(screenWidth,screenHeight)) 
        #Lancement de la musique
        pygame.mixer.music.load('../sound/menu.wav')
        pygame.mixer.music.play(-1) #pour tourner a l'infini
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.textName = ""
        self.score = score
        bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.affichageScore = bigfont.render(str(score), True , (250,250,250))
        

    def render(self,screen):
        screen.blit(self.background, (0,0))
        #pygame.draw.rect(screen,(250,0,0),(510,175,80,40))

        affichageName = self.smallfont.render(self.textName, True , (250,250,250))
        
        screen.blit(self.affichageScore,(510,85))
        screen.blit(affichageName,(510,182))
        

        #self.buttonSave.render(screen)
        #self.buttonSkip.render(screen)

    def action(self,screenWidth,screenHeight):
        #ici récupération position de la souris
        mos_x, mos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN:
                if( event.key == pygame.K_ESCAPE):
                    return "restart"
                elif(event.key == pygame.K_BACKSPACE):
                    self.textName = self.textName[:-1]
                else:
                    if(len(self.textName)<12):
                        self.textName += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:  
            #if the mouse is clicked on the  
            # button the game is terminated 
                if mos_x > 390 and mos_x < 470 and mos_y > 332 and mos_y < 372:

                    #ICI POUR SAUVEGARDER LES DONNEES DE JEUX
                    if(self.textName != ""):
                        fichier = open("../HighScore.txt","a")
                        fichier.write(self.textName + ":" + str(self.score) + "\n")
                        fichier.close
                        return "restart"
                if mos_x > 560 and mos_x < 630 and mos_y > 332 and mos_y < 372:
                    return "restart"
        
        return "End"

class Credit:

    def __init__(self,screenWidth,screenHeight):
        bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.text0 = bigfont.render("Créateur" , True , (250,250,250))
        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.text1 = smallfont.render("Ingénieur son:                   Julien Houny" , True , (250,250,250))
        self.text2 = smallfont.render("Graphiste et game designer:      Sévan Mulin, Alexa Angermann" , True , (250,250,250))
        self.text3 = smallfont.render("Developpeur Gameplay:            Jordy Gelb" , True , (250,250,250))
        self.text4 = bigfont.render("On Remercie Aussi: " , True , (250,250,250))
        self.text8 = smallfont.render("Pour la musique  :   \n Kevin MacLeod pour la musique en jeu " , True , (250,250,250))
        self.text9 = smallfont.render(" \n Dar Golan pour celle du menu ",True, (250,250,250))
        self.text10 = smallfont.render(" Les deux étant 'no copyrights' ",True, (250,250,250))
        self.textRetour = bigfont.render("RETOUR" , True , (250,250,250))
    
    def render(self,screen):
        screen.fill((24,24,24))
        screen.blit(self.text0,(425,25))
        screen.blit(self.text1,(100,100))
        screen.blit(self.text2,(100,125))
        screen.blit(self.text3,(100,150))

        screen.blit(self.text4,(300,250))

        screen.blit(self.text8,(70,350))
        screen.blit(self.text9,(350,375))
        screen.blit(self.text10,(300,450))
        

        #pygame.draw.rect(screen,(250,0,0),(410,645,200,50))
        screen.blit(self.textRetour,(425,650))
        
    
    def action(self):

        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"
            
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                mos_x, mos_y = pygame.mouse.get_pos()
                if(mos_x > 410 and mos_x < 610 and mos_y > 645 and mos_y < 695):
                    return "menu"
            
        return "Credit"


class bestiaire:

    def __init__(self,screenWidth,screenHeight):
        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        tinyfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',13)
        self.verybigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',100)
        self.bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        background = pygame.image.load("../textures/fontbestiaire.png")
        self.background = pygame.transform.scale(background,(screenWidth+755,screenHeight+50))
        self.titre = self.bigfont.render("Bestiaire" , True , (250,250,250))
        self.retour = self.bigfont.render("Retour" , True , (250,250,250))
        
        self.carotte = """attaque :  corps à corps !
vitesse :       viiiiite !
vie     :       moyenne  !"""
        self.tomate  = """attaque :        explose !
vitesse :    normalement ! 
vie     :      moyenne+  !"""
        self.ail     = """attaque : au corps à corps !
vitesse :      lentement !
vie     :         Tonk   !"""
        self.bananne = """attaque : 'Très fort       !
vitesse : Lente et saoule  ! 
vie     : Tentacule de fer !"""       
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
        for ligne in self.bananne.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))
        x=800
        y=150
        i=0
        for ligne in self.ail.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))

        sprite = SpriteSheet('../textures/Carotte.png')
        self.imagecarotte=(pygame.transform.scale(sprite.image_at((416,1024,416,1024)),(64,160)))

        sprite = SpriteSheet('../textures/elTomaty.png')
        self.imagetomate=(pygame.transform.scale(sprite.image_at((350,0,350,500)),(128,256)))

        sprite = SpriteSheet('../textures/Banane.png')
        self.imageBanane=(pygame.transform.scale(sprite.image_at((350,0,350,500)),(256,256)))



        
        self.text1 = smallfont.render("LA CAROTTE" , True , (250,250,250))
        self.text2 = smallfont.render("LA TOMATE" , True , (250,250,250))
        self.text3 = smallfont.render("LA BANANNE" , True , (250,250,250))
        self.text4 = smallfont.render("L'AIL" , True , (250,250,250))
        
    

    def render(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.text1,(50,100))
        screen.blit(self.text2,(300,100))
        screen.blit(self.text3,(550,100))
        screen.blit(self.text4,(800,100))
        self.background.blit(self.imagecarotte,(110,260))
        self.background.blit(self.imagetomate,(330,200))
        self.background.blit(self.imageBanane,(510,250))
        self.background.blit(self.verybigfont.render("?",1,(200,50,50)),(860,300))

        pygame.draw.rect(screen,(41,41,41),(750,0,200,50)) #chingchong

        #pygame.draw.rect(screen,(0,0,0),(395,25,260,50))
        screen.blit(self.titre,(400,25))
        #pygame.draw.rect(screen,(0,0,0),(420,575,175,50))
        screen.blit(self.retour,(425,575))
        
 
    def action(self,screenWidth,screenHeight):
        #ici récupération position de la souris
        mos_x, mos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "SoupeScreen"
            if event.type == pygame.MOUSEBUTTONDOWN:  
            #if the mouse is clicked on the  
            # button the game is terminated  
                if  mos_x > 420 and mos_x < 595 and mos_y > 575 and mos_y < 625:
                    return "SoupeScreen" 
        return "Bestiaire"

class regles:

    def __init__(self,screenWidth,screenHeight):
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.titrePage = self.bigfont.render("Règles" , True , (250,250,250))
        self.boutonRetour = self.bigfont.render("RETOUR" , True , (250,250,250))
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

         [ou plutot: le maximum d'argent engrangé dans la partie]

       [un score élevé signifie que vous avez longtemps cauchemardé] """

        

    def render(self,screen):
        screen.fill((20,20,20))
        i=0
        x=-45
        y=100
        for ligne in self.rules.splitlines():
            i+=1
            screen.blit(self.smallfont.render(ligne,1,(200,50,50)),(x,y+i*15))

        screen.blit(self.titrePage,(425,50))
        #pygame.draw.rect(screen,(250,0,0),(410,670,200,50))
        screen.blit(self.boutonRetour,(425,675))

 
    def action(self,screenWidth,screenHeight):
        #ici récupération position de la souris
        mos_x, mos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"
            if event.type == pygame.MOUSEBUTTONDOWN:  
            #if the mouse is clicked on the  
            # button the game is terminated  
                if(mos_x> 425 and mos_x < 610 and mos_y > 670 and mos_y < 720):
                    return "menu"
        return "Regles"

class Upgrade:
    def __init__(self,screenWidth,screenHeight,gold,upgrade):
        self.verybigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',150)
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        tinyfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',13)
        self.retour = self.bigfont.render("Retour" , True , (250,250,250))
        self.gold = gold
        self.upgrade = upgrade


        #generation sprite/images

        background = pygame.image.load("../textures/fontbestiaire.png")
        
        self.background = pygame.transform.scale(background,(screenWidth+755,screenHeight+50))
        self.titre = self.bigfont.render("Upgrade" , True , (250,250,250))


        sprite = SpriteSheet('../textures/BILLY_AVANCE.png')
        rect = (0,0,704,1152)
        tempSprite = sprite.image_at(rect)
        self.billy = pygame.transform.scale(tempSprite,(70,115))

        sprite = SpriteSheet('../textures/MORTIER.png')  
        rect = (0,0,672,672)
        tempSprite = sprite.image_at(rect)
        self.imageMortier = pygame.transform.scale(tempSprite,(125,125))

        spriteMur = SpriteSheet('../textures/Barricade.png')
        rect = (0,0,704,704)
        tempSprite = spriteMur.image_at(rect)
        self.spriteMur =pygame.transform.scale(tempSprite,(125,125))

        sprite = SpriteSheet('../textures/Turret.png')
        rect = (0,0,640,640)
        tempSprite = sprite.image_at(rect)
        self.imageMitra = pygame.transform.scale(tempSprite,(125,125))


        self.text1 = self.smallfont.render("JOUEUR" , True , (250,250,250))
        self.playerUpgrade = """Augmentation du player :  
coût      :  50PO 
Changement: +1PV /1 upgrade
            +1DMG /5 upgrades
            +1VIT /5 upgrades"""

        x=40
        y=150
        i=0
        for ligne in self.playerUpgrade.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))


        self.text2 = self.smallfont.render("BARRICADE" , True , (250,250,250))
        self.barricadeUpgrade = """Augmentation de la barricade :  
coût      :  50PO 
Changement: +100PV /1 upgrade"""
        x=290
        y=150
        i=0
        for ligne in self.barricadeUpgrade.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))


        self.text3 = self.smallfont.render("MORTIER" , True , (250,250,250))
        self.mortierUpgrade = """Augmentation du Mortier :  
coût      :  100PO 
Changement: +1DMG /1 upgrade"""
        x=550
        y=150
        i=0
        for ligne in self.mortierUpgrade.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))
        

        self.text4 = self.smallfont.render("MITRAILLETTE" , True , (250,250,250))
        self.mitraUpgrade = """Augmentation de la Mitraille :  
coût      :  100PO 
Changement: +1DMG /1 upgrade"""
        x=785
        y=150
        i=0
        for ligne in self.mitraUpgrade.splitlines():
            i+=1
            self.background.blit(tinyfont.render(ligne,1,(200,50,50)),(x,y+i*20))



    def render(self,screen):
        self.affichageGold = self.smallfont.render("Gold: "+ str(self.gold) , True , (250,250,250))
        
        screen.fill((20,20,20))
        screen.blit(self.background,(0,0))
        pygame.draw.rect(screen,(41,41,41),(750,0,200,50)) #chingchong
        screen.blit(self.titre,(425,25))
        screen.blit(self.retour,(425,650))

        """pygame.draw.rect(self.background,(0,0,0),(100,490,75,60))
        pygame.draw.rect(self.background,(0,0,0),(350,490,75,60))
        pygame.draw.rect(self.background,(0,0,0),(600,490,75,60))
        pygame.draw.rect(self.background,(0,0,0),(850,490,75,60))"""

        self.background.blit(self.verybigfont.render("+",1,(250,250,250)),(100,450))
        self.background.blit(self.verybigfont.render("+",1,(250,250,250)),(350,450))
        self.background.blit(self.verybigfont.render("+",1,(250,250,250)),(600,450))
        self.background.blit(self.verybigfont.render("+",1,(250,250,250)),(850,450))
        screen.blit(self.affichageGold,(850,10))

        screen.blit(self.billy,(100,300))
        screen.blit(self.text1,(50,100))

        screen.blit(self.spriteMur,(330,300))
        screen.blit(self.text2,(300,100))

        screen.blit(self.imageMortier,(580,300))
        screen.blit(self.text3,(550,100))

        screen.blit(self.imageMitra,(825,300))
        screen.blit(self.text4,(800,100))

        
        
    def action(self,screenWidth,screenHeight):
        mos_x, mos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "SoupeScreen"
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if  mos_x > 100 and mos_x < 175 and mos_y > 490 and mos_y < 550 and self.gold >= 50:
                    self.gold -= 50
                    self.upgrade[0][1] += 1
                elif mos_x > 350 and mos_x < 425 and mos_y > 490 and mos_y < 550 and self.gold >= 50:
                    self.gold -= 50
                    self.upgrade[1][1] += 1
                elif mos_x > 600 and mos_x < 675 and mos_y > 490 and mos_y < 550 and self.gold >= 100:
                    self.gold -= 100
                    self.upgrade[2][1] += 1
                elif mos_x > 850 and mos_x < 925 and mos_y > 490 and mos_y < 550 and self.gold >= 100:
                    self.gold -= 100
                    self.upgrade[3][1] += 1
                elif(mos_x > 425 and mos_x < 610 and mos_y > 650 and mos_y < 700):
                    return "SoupeScreen"

        return "Upgrade"


class horloge:

    def __init__(self,screenWidth,screenHeight):
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',50)
        self.titrePage = self.bigfont.render("Et la nuit se déroula tranquilement" , True , (250,250,250))
        self.spriteclock=[]
        try:
            clo = SpriteSheet("../textures/clock.png")
            for j in range(24):
                rect = (0,j*672,672,672)
                tempSprite = clo.image_at(rect)
                self.spriteclock.append(pygame.transform.rotate(pygame.transform.scale(tempSprite,(500,500)),90))
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def render(self,screen,screenWidth,screenHeight):

        for i in range(24):
            screen.fill((41,41,41))
            screen.blit(self.titrePage,(10,50))
            screen.blit(self.spriteclock[i],(screenWidth/2-220,screenHeight/2-271))
            pygame.display.flip()
            pygame.time.wait(120)
        return "SoupeScreen"

 
class Cinematique:

    def __init__(self,screenWidth,screenHeight):
        self.smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.TriggerFont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',85)
        self.bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',15)
        self.HIPSTER = pygame.image.load("../textures/Hipster.png")
        self.fantome = pygame.image.load("../textures/HOUUUU.png")
        self.billyDODO = pygame.image.load("../textures/BILLY_DODO.png")
        self.billyTriger = pygame.image.load("../textures/TRIGERRED.png")

        self.billyDODO=pygame.transform.scale(self.billyDODO, (1500  - screenHeight, screenHeight))
        
        self.BILLY = pygame.image.load("../textures/BILLYLY.png")
        self.BILLY = pygame.transform.scale(self.BILLY, (1500  - screenHeight, screenHeight))
        self.text = self.bigfont.render("[ESP] Quitter   /   [ESPACE] Suivant" , True , (250,250,250))
        self.etape=0

    def render(self,screen):

        if(self.etape==0):
            screen.fill((41,41,41))
            screen.blit(self.HIPSTER,(0,0))
            screen.blit(self.text,(425,50))

            temptext=self.smallfont.render("MANGE TA SOUPE BILLY !" , True , (250,250,250))
            screen.blit(temptext,(425,200))

        if(self.etape==1):
            screen.fill((41,41,41))
            screen.blit(self.BILLY,(0,0))
            
            
            temptext=self.smallfont.render("mais, mais j'ai pas faim !" , True , (250,250,250))
            screen.blit(temptext,(425,200))
        if(self.etape==2):
            screen.fill((41,41,41))
            screen.blit(self.HIPSTER,(0,0))
            
            
            temptext=self.smallfont.render("MANGE TA SOUPE, ou tu subira des conséquences huahaha" , True , (250,250,250))
            screen.blit(temptext,(50,200))
        if(self.etape==3):
            screen.fill((41,41,41))
            
            
            temptext=self.smallfont.render("*sort de la chambre*" , True , (250,250,250))
            screen.blit(temptext,(425,200))
        if(self.etape==4):
            screen.fill((41,41,41))
            
            screen.blit(self.BILLY,(0,0))
            temptext=self.smallfont.render("allé, zou, à la poubelle, jvais dodo" , True , (250,250,250))
            screen.blit(temptext,(425,200))
        if(self.etape==5):
            screen.fill((41,41,41))
            screen.blit(self.billyDODO,(0,0))
            
            
            temptext=self.smallfont.render("[Mais, la nuiiit, les fantômes se réveillent]" , True , (250,250,250))
            screen.blit(temptext,(100,200))
        if(self.etape==6):
            screen.fill((41,41,41))
            screen.blit(self.fantome,(0,0))
            
            
            temptext=self.smallfont.render("hooou, nous sommes des légumes morts pour rien" , True , (250,250,250))
            temptext2=self.smallfont.render("Nous venons te hanter !" , True , (250,250,250))
            screen.blit(temptext,(25,450))
            screen.blit(temptext2,(40,500))
        if(self.etape==7):
            screen.fill((41,41,41))
            screen.blit(self.billyTriger,(0,0))
            
            
            temptext=self.TriggerFont.render("NON RENDORMEZ VOUS !" , True , (200,10,10))
            screen.blit(temptext,(30,200))

        
    def action(self,screenWidth,screenHeight):
        mos_x, mos_y = pygame.mouse.get_pos()

        if self.etape > 7:
            self.etape =0
            return "SoupeScreen"

        for event in pygame.event.get():
            #ragequit
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.etape =0
                return "SoupeScreen"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.etape+=1
        return "Cinematique"    
        