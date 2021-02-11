#classe joueur

import pygame
from spritesheet import SpriteSheet
from projectile import Projectile
from barreComp import *

class Player(pygame.sprite.Sprite):



    def __init__(self,screenWidth,screenHeight):
        super().__init__()
        self.vie = 10
        self.maxhealth = 10
        self.attack = 2
        self.velocity = 10
        self.playerXoffset = 0
        self.playerYoffset = 0
        self.cooldown = 30
        self.gold = 1000
        self.isDead = False
        self.invincibility = False
        self.TimerInvincibility = 0
        #variable de gestion de l'animation des sprites
        self.current = 0

        #Variable d'enregistrement des actions joueurs: permet de reprendre les mouvements à current = 0
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False

        #position du joueur par rapport à la carte [x,y] 0,0 = spawn
       
        
        #generation images
        self.generationSprite()
        
        self.rect = self.billy_Droite[0].get_rect()
        self.rect.x = screenWidth/2 #-1/2*self.rect.width
        self.rect.y = screenHeight/2 #- 1/2*self.rect.height

        self.position = [2000,2000]

        self.projectilPath = "../textures/Rolling_Stone.png"

        #Projectile
        self.projectiles = []
        self.timer = 0

        #affichage gold
        self.bigfont = pygame.font.Font('../textures/Perfect DOS VGA 437 Win.ttf',35)
        self.affichageGold = self.bigfont.render("Gold: "+ str(self.gold) , True , (250,250,250))

        self.barreCompetence=barreComp(screenWidth,screenHeight,self.vie)


        

    def render(self,screen,xOffset,yOffset):


        if(self.moveRight ==False and self.moveDown==False and self.moveUp==False and self.moveLeft==False):
            self.current = 0
            if(self.TimerInvincibility != 0):
                screen.blit(self.billy_Gauche_Trans[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            else:
                screen.blit(self.billy_Gauche[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
        if(self.moveUp == True):
            if(self.TimerInvincibility != 0):
                screen.blit(self.billy_Monte_Trans[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            else:
                screen.blit(self.billy_Monte[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            self.moveUp = False
        elif(self.moveLeft == True):
            if(self.TimerInvincibility != 0):
                screen.blit(self.billy_Gauche_Trans[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            else:
                screen.blit(self.billy_Gauche[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            self.moveLeft = False
        elif(self.moveRight == True):
            if(self.TimerInvincibility != 0):
                screen.blit(self.billy_Droite_Trans[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            else:
                screen.blit(self.billy_Droite[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            self.moveRight = False
        #hitbox
        #pygame.draw.rect(screen,(250,250,250),(self.rect.x+self.playerXoffset,self.rect.y+self.playerYoffset,self.rect.width, self.rect.height))
        for i in range(len(self.projectiles)):
            self.projectiles[i].render(screen,xOffset,yOffset)

        self.affichageGold = self.bigfont.render("Gold: "+ str(self.gold) , True , (250,250,250))
        screen.blit(self.affichageGold,(825,10))

        self.barreCompetence.render(screen,self.vie)
        

    def update(self,entities):

        self.TimerInvincibilityUpdate()

        self.barreCompetence.update(self.gold)

        self.clearProjectiles()

        self.timer +=1
        for i in range(len(self.projectiles)):
            self.projectiles[i].update(entities)


    
    def shoot_right(self,mapBorderRight):
        if(self.timer >= self.cooldown):
            shoot = Projectile(self.position[0],self.position[1],self.projectilPath,"right",10,12,1500)
            self.projectiles.append(shoot)
            self.timer = 0
        
    def shoot_left(self,mapBorderLeft):
        if(self.timer >= self.cooldown):
            shoot = Projectile(self.position[0],self.position[1],self.projectilPath,"left",10,12,1500)
            self.projectiles.append(shoot)
            self.timer = 0

    def shoot_up(self,mapBorderDown):
        if(self.timer >= self.cooldown):

            shoot = Projectile(self.position[0],self.position[1],self.projectilPath,"up",10,12,1500)
            self.projectiles.append(shoot)
            self.timer = 0

    def shoot_down(self,mapBorderUp):
        if(self.timer >= self.cooldown):
            shoot = Projectile(self.position[0],self.position[1],self.projectilPath,"down",10,12,1500)
            self.projectiles.append(shoot)
            self.timer = 0

    def move_left(self,mapBorderLeft,bord):
        self.moveSprite("Left")
        self.moveLeft = True
        if(self.position[0] > mapBorderLeft -10): #-10 est une valeur arbitraire
            if(bord == True):
                self.playerXoffset -= self.velocity
            else:
                self.playerXoffset = 0
            self.position[0] -= self.velocity
        else:
            pass
            #print("can't left")

    def move_right(self,mapBorderRight,bord):
        self.moveSprite("Right")
        self.moveRight = True
        if(self.position[0] + self.rect.width*2 < mapBorderRight + 80): #80 est une valeur arbitraire
            if(bord == True):
                self.playerXoffset += self.velocity
            else:
                self.playerXoffset = 0
            self.position[0] += self.velocity
        else:
            pass
            #print("can't right")
            
    
    def move_up(self,mapBorderTop,bord):

        self.moveSprite("Up")
        self.moveUp = True
        if(self.position[1] > mapBorderTop ):
            if(bord == True):
                self.playerYoffset -= self.velocity
            else:
                self.playerYoffset = 0

            self.position[1] -= self.velocity
        else:
            pass
            #print("can't up")
    
    def move_down(self,mapBorderBottom,bord):

        if(self.position[1]+self.rect.height < mapBorderBottom -5): # 4 est une valeur arbitraire
            self.position[1] += self.velocity
            if(bord == True):
                self.playerYoffset += self.velocity
            else:
                self.playerYoffset = 0
        else:
            pass
            #print("can't down")



    #gere le timer invincibilité
    def TimerInvincibilityUpdate(self):
        if(self.TimerInvincibility != 0):
            self.TimerInvincibility += 1
            if(self.TimerInvincibility >= 50):
                #print("endInvincibilité")
                self.velocity -=5
                self.TimerInvincibility = 0
                self.invincibility = False



    def clearProjectiles(self):
        #print(self.projectiles)
        if (self.projectiles):
            for i in range(len(self.projectiles)):
                if(self.projectiles[i].exist == False):
                    del self.projectiles[i]
                    break
    
    #cette fonction gere le numero et type de sprite affiché dans render
    def moveSprite(self,direction):
        if(direction == "Up"):
            if(self.moveLeft ==True or self.moveDown == True or self.moveRight == True):
                self.current 
                self.moveLeft =False
                self.moveDown= False
                self.moveUp= False
            if(self.current > 2):
                self.current = 0
            else:
                self.current += 1
        elif(direction == "Right"):
            if(self.moveLeft ==True or self.moveDown == True or self.moveUp == True):
                self.current = 0
                self.moveLeft =False
                self.moveDown= False
                self.moveUp= False

            if(self.current < 7):
                self.current += 1
            else:
                self.current = 0
        elif(direction == "Left"):
            if(self.moveRight ==True or self.moveDown == True or self.moveUp == True):
                self.current = 0
                self.moveRight =False
                self.moveDown= False
                self.moveUp= False

            if(self.current <7):
                self.current +=1
            else:
                self.current = 0


    #generation des sprites et stockage 
    def generationSprite(self):
        try:

            sprite = SpriteSheet('../textures/BILLY_AVANCE.png')
            self.billy_Droite_Trans= []
            self.billy_Droite=[]
            for i in range(8):
                rect = (i*704,0,704,1152)
                tempSprite = sprite.image_at(rect)
                self.billy_Droite.append(pygame.transform.scale(tempSprite,(70,115)))
                self.billy_Droite_Trans.append(pygame.transform.scale(tempSprite,(70,115)))
                self.billy_Droite_Trans[i].set_alpha(75)

            sprite.flipHorizontaly()

            self.billy_Gauche_Trans = []
            self.billy_Gauche=[]
            for i in range(8):
                rect = (i*704,0,704,1152)
                tempSprite = sprite.image_at(rect)
                self.billy_Gauche.append(pygame.transform.scale(tempSprite,(70,115)))
                self.billy_Gauche_Trans.append(pygame.transform.scale(tempSprite,(70,115)))
                self.billy_Gauche_Trans[i].set_alpha(75)

            sprite = SpriteSheet('../textures/BILLY_MONTE.png')
            self.billy_Monte_Trans= []
            self.billy_Monte=[]
            for i in range(4):
                rect = (i*576,0,576,1152)
                tempSprite = sprite.image_at(rect)
                self.billy_Monte.append(pygame.transform.scale(tempSprite,(70,115)))
                self.billy_Monte_Trans.append(pygame.transform.scale(tempSprite,(70,115)))
                self.billy_Monte_Trans[i].set_alpha(75)
            

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        

    #fonction importante: applique les changements de vie externe + rend le joueur invincible sur une periode de temps
    def takeDamage(self,amount):
        if(self.invincibility ==False):
            self.vie -= amount
            self.velocity += 5
            if(self.vie <= 0):
                #ici pour animation mort
                self.isDead = True
            else:
                self.invincibility = True
                self.TimerInvincibility =1
            return True
        else:
            #sous invincibilité les dmgs sont annulé
            return False

