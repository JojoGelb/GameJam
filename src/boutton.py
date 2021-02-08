import pygame


class Boutton:

    def __init__(self,x,y,width,height,message):
        self.image = pygame.transform.scale(pygame.image.load('textures/wood.jpg'),(width,height)) 
        smallfont = pygame.font.Font('freesansbold.ttf',50)
        self.text = smallfont.render(message , True , (250,250,250))
        self.rect = self.image.get_rect()

        if(message == "Play"):
            self.rect.x = x
            self.rect.y = y
            self.textpos = (self.rect.x+200,self.rect.y + 20)
        elif(message == "Quit"):
            self.rect.x = x
            self.rect.y = y
            self.textpos = (self.rect.x+60,self.rect.y + 20)
        elif(message == "Settings"):
            self.rect.x = x
            self.rect.y = y
            self.textpos = (self.rect.x+15,self.rect.y + 20)
        else:
            self.rect.x = x
            self.rect.y = y
            self.textpos = (self.rect.x+60,self.rect.y + 20)

    def render(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
        screen.blit(self.text, self.textpos)

    def click(self,mos_x,mos_y):
        if (self.rect.x <= mos_x <= self.rect.x+self.rect.width and self.rect.y <= mos_y <= self.rect.y + self.rect.height):
            return True

