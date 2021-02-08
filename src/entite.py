import pygame
from spritesheet import SpriteSheet


class entite(pygame.sprite.Sprite):

    def __init__(self,typeAttaque,vie,projectile,degats,typpe,xx,yy):
        super().__init__()
        self.vie=vie
        self.typeAttaque=typeAttaque
        self.projectile=projectile
        self.degats=degats
        self.type=typpe
        self.x = xx
        self.y = yy
        self.current=0


                

class carotte(entite):

    def __init__(self,xx,yy):
        entite.__init__(self,"CAC",10,"NULL",1,"ENNEMIS",xx,yy)
       
        try:
            sprite = SpriteSheet('../textures/Carotte.png')


            self.image=[]
            for i in range(2):
                for j in range(2):
                    rect = (i*416,j*1024,416,1024)
                    tempSprite = sprite.image_at(rect)
                    self.image.append(pygame.transform.scale(tempSprite,(64,160)))
 

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
       
       
        self.rect = self.image[0].get_rect()
        self.rect.x = xx
        self.rect.y = yy

        
    def render(self,screen,xOffset,yOffset):
        self.rect = self.image[self.current].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y   
        screen.blit(self.image[self.current],(xOffset+self.rect.x,yOffset+self.rect.y)) #affiche l'image de l'entite à la position indiqué par ses coord
        self.current=(self.current+1)%4
            


class tomate(entite):

    def __init__(self,typeAttaque,vie,projectile,degats,typpe,x,y):
        entite.__init__(self,typeAttaque,vie,projectile,degats,typpe,x,y)






















