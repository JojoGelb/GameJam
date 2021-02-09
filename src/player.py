#classe joueur

import pygame
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):



    def __init__(self,screenWidth,screenHeight):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.attack = 10
        self.velocity = 20
        self.playerXoffset = 0
        self.playerYoffset = 0
        self.current = 0

        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False

        #position du joueur par rapport à la carte [x,y] 0,0 = spawn
        self.position = [2000,2000]
        
        #generation image
        self.generationSprite()
        


        self.rect = self.billy_Droite[0].get_rect()
        self.rect.x = screenWidth/2 + self.rect.width/2
        self.rect.y = screenHeight/2 + self.rect.height/2

    def render(self,screen):
        if(self.moveRight ==False and self.moveDown==False and self.moveUp==False and self.moveLeft==False):
            self.current = 0
            screen.blit(self.billy_Gauche[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
        if(self.moveUp == True):
            screen.blit(self.billy_Monte[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            self.moveUp = False
        elif(self.moveLeft == True):
            screen.blit(self.billy_Gauche[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            self.moveLeft = False
        elif(self.moveRight == True):
            screen.blit(self.billy_Droite[self.current],(self.rect.x+self.playerXoffset,self.rect.y + self.playerYoffset))
            self.moveRight = False
        
        #hitbox
        #pygame.draw.rect(screen,(250,250,250),(self.rect.x+self.playerXoffset,self.rect.y+self.playerYoffset,self.rect.width, self.rect.height))

        

    def move_left(self,mapBorderLeft,bord):
        self.moveSprite("Left")
        self.moveLeft = True
        if(self.position[0] > mapBorderLeft - 30): #30 est une valeur arbitraire
            if(bord == True):
                self.playerXoffset -= self.velocity
            self.position[0] -= self.velocity
        else:
            print("can't left")

    def move_right(self,mapBorderRight,bord):
        self.moveSprite("Right")
        self.moveRight = True
        if(self.position[0] + self.rect.width*2 < mapBorderRight + 30): #30 est une valeur arbitraire
            if(bord == True):
                self.playerXoffset += self.velocity
            self.position[0] += self.velocity
        else:
            print("can't right")
            
    
    def move_up(self,mapBorderTop,bord):

        self.moveSprite("Up")
        self.moveUp = True
        if(self.position[1] > mapBorderTop -30): # 30 est une valeur arbitraire
            if(bord == True):
                self.playerYoffset -= self.velocity

            self.position[1] -= self.velocity
        else:
            print("can't up")
    
    def move_down(self,mapBorderBottom,bord):

        if(self.position[1]+self.rect.height*2 < mapBorderBottom + 50 ): # 50 est une valeur arbitraire
            self.position[1] += self.velocity
            if(bord == True):
                self.playerYoffset += self.velocity
        else:
            print("can't down")

    def moveSprite(self,direction):
        if(direction == "Up"):
            if(self.moveLeft ==True or self.moveDown == True or self.moveRight == True):
                self.current = 0
                self.moveLeft =False
                self.moveDown= False
                self.moveUp= False
            if(self.current > 4):
                self.current = 0
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
    def generationSprite(self):
        try:
            sprite = SpriteSheet('../textures/BILLY_AVANCE.png')

            self.billy_Droite=[]
            for i in range(8):
                rect = (i*704,0,704,1152)
                tempSprite = sprite.image_at(rect)
                self.billy_Droite.append(pygame.transform.scale(tempSprite,(70,115)))

            sprite.flipHorizontaly()
            self.billy_Gauche=[]
            for i in range(8):
                rect = (i*704,0,704,1152)
                tempSprite = sprite.image_at(rect)
                self.billy_Gauche.append(pygame.transform.scale(tempSprite,(70,115)))
            
            sprite = SpriteSheet('../textures/BILLY_MONTE.png')
            self.billy_Monte=[]
            for i in range(4):
                rect = (i*576,0,576,1152)
                tempSprite = sprite.image_at(rect)
                self.billy_Monte.append(pygame.transform.scale(tempSprite,(70,115)))

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

