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
        self.velocity = 1
        self.timer = 0


                

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
        self.velocity = 4

        
    def render(self,screen,xOffset,yOffset):

        screen.blit(self.image[self.current],(xOffset+self.rect.x,yOffset+self.rect.y)) #affiche l'image de l'entite à la position indiqué par ses coord
        
            
    def update(self,Xjoueur,Yjoueur):
        
        if(self.timer == 10):
            self.current=(self.current+1)%4
            self.timer = 0
        else:
            self.timer +=1

        if(self.rect.x == Xjoueur and self.rect.y == Yjoueur):
            None
            #self.rect.x -= 400
        else:

            if(Xjoueur < self.rect.x):
                self.rect.x -= self.velocity
            elif(Xjoueur > self.rect.x):
                self.rect.x += self.velocity
            if(Yjoueur < self.rect.y):
                self.rect.y -= self.velocity
            elif(Yjoueur > self.rect.y):
                self.rect.y += self.velocity
            

class tomate(entite):

    def __init__(self,xx,yy):
        entite.__init__(self,"CAC",10,"NULL",1,"ENNEMIS",xx,yy)
        
        try:
            sprite = SpriteSheet('../textures/elTomaty.png')


            self.image=[]
            for i in range(4):
                for j in range(4):
                    rect = (i*1120,j*1600,1120,1600)
                    tempSprite = sprite.image_at(rect)
                    self.image.append(pygame.transform.scale(tempSprite,(128,256)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        self.rect = self.image[0].get_rect()
        self.rect.x = xx
        self.rect.y = yy
        self.velocity = 3


    def render(self,screen,xOffset,yOffset):

        screen.blit(self.image[self.current],(xOffset+self.rect.x,yOffset+self.rect.y)) #affiche l'image de l'entite à la position indiqué par ses coord

    def update(self,Xjoueur,Yjoueur):

        if(self.timer == 10):
            self.current=(self.current+1)%4

            if self.current==2 or self.current==1:
                self.velocity=5
            else:
                self.velocity=0
            self.timer = 0
        else:
            self.timer +=1

        if(self.rect.x == Xjoueur and self.rect.y == Yjoueur):
            None
            #self.rect.x -= 400
        else:

            if(Xjoueur < self.rect.x):
                self.rect.x -= self.velocity
            elif(Xjoueur > self.rect.x):
                self.rect.x += self.velocity
            if(Yjoueur < self.rect.y):
                self.rect.y -= self.velocity
            elif(Yjoueur > self.rect.y):
                self.rect.y += self.velocity






















