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

        #position du joueur par rapport à la carte [x,y] 0,0 = spawn
        self.position = [2000,2000]
        
        #generation image
        try:
            sprite = SpriteSheet('../textures/character_001_isaac.png')

            rect = (0,192,64,64)
            sprite = sprite.image_at(rect)
            self.image = pygame.transform.scale(sprite,(128,128))
            

        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        self.rect = self.image.get_rect()
        self.rect.x = screenWidth/2
        self.rect.y = screenHeight/2

    def render(self,screen):
        screen.blit(self.image,(1080/2 -64+self.playerXoffset,720/2 -64 + self.playerYoffset)) #affiche l'image du joueur à la position indiqué par le rectangle
        #print(self.position)

    def move_left(self,mapBorderLeft,bord):
        if(self.position[0] > mapBorderLeft):
            if(bord == True):
                self.playerXoffset -= self.velocity
            self.position[0] -= self.velocity
        else:
            print("can't left")

    def move_right(self,mapBorderRight,bord):
        if(self.position[0] + self.rect.width/2 < mapBorderRight):
            if(bord == True):
                self.playerXoffset += self.velocity
            self.position[0] += self.velocity
        else:
            print("can't right")
            
    
    def move_up(self,mapBorderTop,bord):

        if(self.position[1] > mapBorderTop):
            if(bord == True):
                self.playerYoffset -= self.velocity

            self.position[1] -= self.velocity
        else:
            print("can't up")
    
    def move_down(self,mapBorderBottom,bord):

        if(self.position[1]+self.rect.height/2 < mapBorderBottom):
            self.position[1] += self.velocity
            if(bord == True):
                self.playerYoffset += self.velocity
        else:
            print("can't down")

  #  def changePlayerXOffset(self,value):
  #      self.playerXoffset += value

   # def changePlayerYOffset(self,value):
   #     self.playerYoffset += value
