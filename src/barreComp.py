import pygame
from spritesheet import SpriteSheet
import random
from boutton import *



class barreComp(pygame.sprite.Sprite):




    def __init__(self,screenWidth,screenHeight,vie):
        super().__init__()        
        try:
            self.image=pygame.transform.scale(pygame.image.load('../textures/barreComp.png'),(int(screenWidth*0.85),int(screenHeight*0.15))) 
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
        self.pos=(int(screenWidth*0.075),int(screenHeight*0.85))

        smallfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',25)
        self.mormor = smallfont.render("Mortier" , True , (250,250,250))
        self.mormorT = smallfont.render("200g  [E]" , True , (250,250,250))        
        self.murmur = smallfont.render("Mur" , True , (250,250,250))
        self.murmurT = smallfont.render("50g   [A]" , True , (250,250,250))
        self.morClicable = True
        self.murClicable = True
        self.VieMax=vie
        self.screenHeight=screenHeight
        self.screenWidth=screenWidth

    def render(self,screen,vie):

        screen.blit(self.image, self.pos)
        screen.blit(self.murmur,(int(self.screenWidth*0.12),int(self.screenHeight*0.89)))
        screen.blit(self.murmurT,(int(self.screenWidth*0.12),int(self.screenHeight*0.92)))
        screen.blit(self.mormor,(int(self.screenWidth*0.29),int(self.screenHeight*0.89)))
        screen.blit(self.mormorT,(int(self.screenWidth*0.29),int(self.screenHeight*0.92)))
        viepourc=100-int(((vie*100)/self.VieMax))
        pygame.draw.rect(screen,(41,41,41),(self.screenWidth*0.90-viepourc*2.4,self.screenHeight*0.88,viepourc*2.4,70))

        
    def update(self,gold):
        
        #murOK?
        if gold<50:
            self.murmur.set_alpha(50)
            self.murmurT.set_alpha(50)
            self.murClicable=False
        else:
            self.murmur.set_alpha(255)
            self.murmurT.set_alpha(255)            
            self.murClicable=True

        #mortierOK?        
        if gold<200:
            self.mormorT.set_alpha(50)            
            self.mormor.set_alpha(50)
            self.morClicable=False
        else:
            self.mormorT.set_alpha(255)            
            self.mormor.set_alpha(255)
            self.morClicable=True
        
