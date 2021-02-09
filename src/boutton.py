import pygame


class Boutton:

    def __init__(self,x,y,width,height,message):
        self.image = pygame.transform.scale(pygame.image.load('../textures/wood.jpg'),(width,height)) 
        
        
        self.rect = self.image.get_rect()

        if(message == "Play"):
            self.rect.x = x
            self.rect.y = y
                    
        elif(message == "Quit"):
            self.rect.x = x
            self.rect.y = y
            
        elif(message == "Settings"):
            self.rect.x = x
            self.rect.y = y
            
        else:
            self.rect.x = x
            self.rect.y = y
            

    def render(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
        
        self.image.set_alpha(0)

    def click(self,mos_x,mos_y):
        if (self.rect.x <= mos_x <= self.rect.x+self.rect.width and self.rect.y <= mos_y <= self.rect.y + self.rect.height):
            return True

