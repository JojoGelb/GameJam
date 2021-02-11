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
            self.image.append(pygame.transform.scale(tempSprite,(100,100)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        self.hitbox = self.image[0].get_rect()
        
        self.hitbox.x = xx
        self.hitbox.y = yy
        self.current = 0

        self.mask = pygame.mask.from_surface(self.image[0])
        self.range=rangge
        self.range=600
        self.cooldown=100
        self.degats= degats
        self.vie=500
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
                            shoot = ProjectileMortier(self.hitbox.x + self.hitbox.width/2,self.hitbox.y + self.hitbox.height/2,self.degats,5,entite.hitbox.x,entite.hitbox.y)
                            self.projectiles.append(shoot)
                            break
                self.timer=0
            else:
                self.timer+=1     

            for i in range(len(entities)):

                if(self.hitbox.x + self.hitbox.width >= entities[i].hitbox.x and self.hitbox.x < entities[i].hitbox.x + entities[i].hitbox.width) and (self.hitbox.y + self.hitbox.height > entities[i].hitbox.y and self.hitbox.y < entities[i].hitbox.y + entities[i].hitbox.height):
                    entities[i].velocity = 0
                    self.takeDamage(entities[i].degats)          
        else:
            self.timer+=1
            self.miseAMort()

        for i in range(len(self.projectiles)):
            self.projectiles[i].update(entities)
        
        if(self.vie <= 0):
            for i in range(len(entities)):
                entities[i].velocity = entities[i].baseVelocity
        


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

    def takeDamage(self,amount):
        self.vie -= amount
        if(self.vie <= 0):
            self.miseAMort()
#=================================================================================================================================================
class mur(entite):

    def __init__(self,x,y,pointDeVie, spriteMur):

        entite.__init__(self,"DIST",pointDeVie,"NULL",0,"ALLIE",x,y, spriteMur)

        self.coutGold = 100
        self.hitbox = self.image[0].get_rect()
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        self.VieMax = int(pointDeVie)


    def update(self,entities):

        #print(self.vie)
        if self.vie > 0:

            #La collision entre la hitbox du mur et la hitbox des enemies
            for i in range(len(entities)):

                if(self.hitbox.x + self.hitbox.width >= entities[i].hitbox.x and self.hitbox.x < entities[i].hitbox.x + entities[i].hitbox.width) and (self.hitbox.y + self.hitbox.height > entities[i].hitbox.y and self.hitbox.y < entities[i].hitbox.y + entities[i].hitbox.height):
                    #print("Contact !")
                    entities[i].velocity = 0
                    self.takeDamage(entities[i].degats)
                    if self.vie<=(4-self.current)*int(self.VieMax/5):
                        self.current+=1

        else:
            self.exist = False
            for i in range(len(entities)):
                entities[i].velocity = entities[i].baseVelocity
        


    def render(self,screen,xOffset,yOffset):


        if self.exist:

            #pygame.draw.rect(screen,(250,250,250),(xOffset +  self.hitbox.x, yOffset + self.hitbox.y ,100, 100)) #pour tester
            screen.blit(self.image[self.current],(xOffset + self.hitbox.x, yOffset + self.hitbox.y))

    def takeDamage(self,amount):
        self.vie -= amount
        pass

#=================================================================================================================================================
class mitraillette(entite):

    def __init__(self,xx,yy,cooldown,degats,rangge,vie,spriteRollin):
        entite.__init__(self,"DIST",vie,"NULL",degats,"ALLIE",xx,yy,[])

        self.spritetir=spriteRollin
        
        try:
            sprite = SpriteSheet('../textures/Turret.png')

            self.image=[]

            for j in range(4):
                rect = (0,j*640,640,640)
                tempSprite = sprite.image_at(rect)
                self.image.append(pygame.transform.scale(tempSprite,(100,100)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        self.hitbox = self.image[0].get_rect()
        
        self.hitbox.x = xx
        self.hitbox.y = yy
        self.current = 0

        self.mask = pygame.mask.from_surface(self.image[0])
        self.range=rangge
        self.range=600
        self.cooldown=10
        self.degats=degats
        self.vie=500
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
                    if entite.vie>0:
                        if entite.hitbox.x>(self.hitbox.x-self.range) and  entite.hitbox.x<(self.hitbox.x+self.range) and entite.hitbox.y>(self.hitbox.y-self.range) and  entite.hitbox.y<(self.hitbox.y+self.range) and not entite.alreadyKilled:
                            shoot = ProjectileMitraille(self.hitbox.x + self.hitbox.width/2, self.hitbox.y + self.hitbox.height/2, self.degats,10,entite.hitbox.x ,entite.hitbox.y,self.spritetir)
                            self.projectiles.append(shoot)
                            if(entite.hitbox.x<self.hitbox.x):
                                if(entite.hitbox.y<self.hitbox.y):
                                    self.current=1
                                else:
                                    self.current=2
                            else:
                                if(entite.hitbox.y<self.hitbox.y):
                                    self.current=0
                                else:
                                    self.current=3
                            break
                self.timer=0
            else:
                self.timer+=1     

            for i in range(len(entities)):

                if(self.hitbox.x + self.hitbox.width >= entities[i].hitbox.x and self.hitbox.x < entities[i].hitbox.x + entities[i].hitbox.width) and (self.hitbox.y + self.hitbox.height > entities[i].hitbox.y and self.hitbox.y < entities[i].hitbox.y + entities[i].hitbox.height):
                    entities[i].velocity = 0
                    self.takeDamage(entities[i].degats)          
        else:
            self.timer+=1
            self.miseAMort()



        for i in range(len(self.projectiles)):
            self.projectiles[i].update(entities)
        
        if(self.vie <= 0):
            for i in range(len(entities)):
                entities[i].velocity = entities[i].baseVelocity
        


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

    def takeDamage(self,amount):
        self.vie -= amount
        if(self.vie <= 0):
            self.miseAMort()
























