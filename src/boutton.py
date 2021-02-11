import pygame


class Boutton:

    def __init__(self,x,y,width,height,message):
        #self.image = pygame.transform.scale(pygame.image.load('../textures/wood.jpg'),(width,height)) 
        self.rect = pygame.Rect(x,y,width,height)
                    
        

    def render(self,screen):
        #screen.blit(self.image, (self.rect.x,self.rect.y))
        
        self.image.set_alpha(0)

    def click(self,mos_x,mos_y):
        if (self.rect.x <= mos_x <= self.rect.x+self.rect.width and self.rect.y <= mos_y <= self.rect.y + self.rect.height):
            return True

