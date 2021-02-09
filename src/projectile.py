import pygame
from spritesheet import SpriteSheet


class Projectile(pygame.sprite.Sprite):

    def __init__(self,x,y,PATH,direction,damage,vitesse_proj,distanceProj):
        super().__init__()
        self.damage = damage
        self.vitesse = vitesse_proj
        self.distance = distanceProj
        self.direction = direction
        self.current=0
        self.hasHit = False
        self.exist = True
        self.timer = 0
        try:
            sprite = SpriteSheet(PATH)

            self.image=[]
            for j in range(17):
                rect = (0,j*200,200,200)
                tempSprite = sprite.image_at(rect)
                self.image.append(pygame.transform.scale(tempSprite,(64,64)))
 

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
       
       
        self.rect = self.image[0].get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self,screen,xOffset,yOffset):
        if(self.exist != False):
            screen.blit(self.image[self.current],(xOffset+self.rect.x,yOffset+self.rect.y))
            self.update("aaa")

    def update(self,entities):
        #for entities check si touché ou non temp = entitie touché
        temp = self.doesHit(entities)
        if(temp != False):
            self.hasHit = True
            #infliger des damage à temp: temp.damage(self.damage)
        if(self.hasHit == True or self.distance <= 0):
            self.current += 1
        else:
            #print(self.distance,self.vitesse)
            self.rect.x += self.vitesse
            self.distance -= self.vitesse
        if(self.current > 16):
            self.exist = False
            self.current = -1

    #check si une entite est touché
    #Renvois l'entité si touché, False sinon
    def doesHit(self,entitie):
        return False
                