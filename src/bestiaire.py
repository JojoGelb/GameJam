import pygame
from boutton import Boutton
from spritesheet import SpriteSheet
class bestiaire:

    def __init__(self,screenWidth,screenHeight):
        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        tinyfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',13)
        self.verybigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',100)
        background = pygame.image.load("../textures/fontbestiaire.png")
        self.background = pygame.transform.scale(background,(screenWidth+755,screenHeight+50))
        
        self.carotte = """attaque : au corp a corp !
se déplace :    viiiiite !
vie :           moyenne  !"""
        self.tomate = """attaque : explose        !
se déplace : normalement !
vie :          moyenne+  !"""
        self.ail = """attaque : au corp a corp !
se déplace :   lentement !
vie :           élevée   !"""
        self.bananne = """attaque : 'cune idée     !
se déplace :    idunno   !
vie :           ptetre   !"""       
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
        return "bebes"
