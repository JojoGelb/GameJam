import pygame
from spritesheet import SpriteSheet
import random
from entite import *
from projectile import *


class mortier(entite):

    def __init__(self,xx,yy,cooldown,degats,rangge,vie):
        entite.__init__(self,"DIST",vie,"NULL",degats,"ALLIE",xx,yy,[])

        try:
            sprite = SpriteSheet('../textures/MORTIER.png')

            self.image=[]
            
            rect = (0*672,0,672,672)
            tempSprite = sprite.image_at(rect)
            self.image.append(pygame.transform.scale(tempSprite,(50,50)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        self.hitbox = self.image[0].get_rect()
        self.hitbox.height
        self.hitbox.x = xx
        self.hitbox.y = yy
        self.current = 0

        #NE PAS UTILISER RECT POUR AUTRE CHOSE QUE LA GESTION DE COLLISION
        self.rect = self.hitbox
        #NE PAS UTILISER RECT POUR AUTRE CHOSE QUE LA GESTION DE COLLISION

        self.mask = pygame.mask.from_surface(self.image[0])
        self.range=rangge
        self.range=600
        self.cooldown=100
        self.degats=1
        self.vie=10
        self.projectiles = []
        self.exist = True

    def render(self,screen,xOffset,yOffset):
        #pygame.draw.rect(screen,(250,100,100),(self.hitbox.x+xOffset,self.hitbox.y+yOffset,self.hitbox.width, self.hitbox.height))
        #pygame.draw.rect(screen,(250,100,100),(self.hitbox.x-self.range+xOffset,self.hitbox.y-self.range+yOffset,self.range*2+self.hitbox.height, self.range*2+self.hitbox.height))
        screen.blit(self.image[self.current],(xOffset+self.hitbox.x,yOffset+self.hitbox.y)) #affiche l'image de l'entite à la position indiqué par ses coord
        for i in range(len(self.projectiles)):
            self.projectiles[i].render(screen,xOffset,yOffset)
    
    def update(self,entities):
        
        self.clearProjectiles()
        if not self.alreadyKilled:
            if self.timer==self.cooldown:
                for entite in entities:
                    if entite.hitbox.x>(self.hitbox.x-self.range) and  entite.hitbox.x<(self.hitbox.x+self.range) and entite.hitbox.y>(self.hitbox.y-self.range) and  entite.hitbox.y<(self.hitbox.y+self.range):
                        if not (entite.hitbox.x>(self.hitbox.x-self.range*0.5) and  entite.hitbox.x<(self.hitbox.x+self.range*0.5) and entite.hitbox.y>(self.hitbox.y-self.range*0.5) and  entite.hitbox.y<(self.hitbox.y+self.range*0.5)):
                            shoot = ProjectileMortier(self.hitbox.x + self.hitbox.width/2,self.hitbox.y + self.hitbox.height/2,5,3,entite.hitbox.x,entite.hitbox.y)
                            self.projectiles.append(shoot)
                            break
                self.timer=0
            else:
                self.timer+=1               
        else:
            self.timer+=1
            self.miseAMort()

        for i in range(len(self.projectiles)):
            self.projectiles[i].update(entities)
        


    def miseAMort(self):
        if(self.alreadyKilled == False):
            self.alreadyKilled = True
            self.timer = 0
        self.current= 0
        self.timer += 1
        if(self.timer >=50):
            self.exist = False

    def clearProjectiles(self):
        #print(self.projectiles)
        if (self.projectiles):
            for i in range(len(self.projectiles)):
                if(self.projectiles[i].exist == False):
                    del self.projectiles[i]
                    break




























