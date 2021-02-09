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
        self.mask = pygame.mask.from_surface(self.image[0])
        
    def render(self,screen,xOffset,yOffset):
        if(self.exist != False):
            screen.blit(self.image[self.current],(xOffset+self.rect.x,yOffset+self.rect.y))
            

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
            self.move()
        if(self.current > 16):
            self.exist = False
            self.current = -1

    #check si une entite est touché
    #Renvois l'entité si touché, False sinon
    def doesHit(self,entitie):
        if self.hasHit == False :
            ennemisTouches = pygame.sprite.spritecollide(self, entitie, False)
            if ennemisTouches :
                for entite in ennemisTouches:
                    entite.vie -= self.damage
                    if entite.vie <= 0:
                        entite.miseAMort() # tout va bien carotte n'a pas encore de mise à mort
                        print("Dead")

                return True
            else:

                return False
        else:
            return True
    
    def move(self):
        if(self.direction == "up"):
            self.rect.y -= self.vitesse
            self.distance -= self.vitesse
        elif(self.direction == "down"):
            self.rect.y += self.vitesse
            self.distance -= self.vitesse
        elif(self.direction == "left"):
            self.rect.x -= self.vitesse
            self.distance -= self.vitesse
        elif(self.direction == "right"):
            self.rect.x += self.vitesse
            self.distance -= self.vitesse
