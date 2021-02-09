import pygame
from spritesheet import SpriteSheet


class Projectile(pygame.sprite.Sprite):

    def __init__(self,x,y,PATH,damage,vitesse_proj):
        super().__init__()
        self.damage = damage
        self.vitesse = vitesse_proj
        self.current=0
        self.hitted = False
        self.exist = True
        self.timer = 0
        try:
            sprite = SpriteSheet(PATH)

            self.image=[]
            for j in range(17):
                rect = (0,j*1664,1664,1664)
                tempSprite = sprite.image_at(rect)
                self.image.append(pygame.transform.scale(tempSprite,(64,64)))
 

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
       
       
        self.rect = self.image[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit("aaa")

    def render(self,screen,xOffset,yOffset):
        screen.blit(self.image[self.current],(xOffset+self.rect.x,yOffset+self.rect.y))

    def update(self,entities):
        temp = self.hit(entities)
        if(temp != False and self.hit == False):
            #infliger damage
            self.hit = True
            self.current += 1
            #entities.damage
        elif(self.hit == True):
            if(self.current == 17):
                self.exist = False
            else:
                if(self.timer == 10):
                    self.current=(self.current+1)%4
                    self.timer = 0
                else:
                    self.timer +=1
                    self.current += 1
    
    def hit(self,entities):
        return True
                