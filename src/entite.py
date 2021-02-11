import pygame
from spritesheet import SpriteSheet
import random

class entite(pygame.sprite.Sprite):

    def __init__(self,typeAttaque,vie,projectile,degats,typpe,xx,yy,sprite):
        super().__init__()
        self.vie=vie
        self.typeAttaque=typeAttaque
        self.projectile=projectile
        self.degats=degats
        self.type=typpe
        self.x = xx
        self.y = yy
        self.current=0
        self.velocity = 1
        self.timer = 0
        self.orientation=0
        self.baseVelocity=0
        self.hitbox=None
        self.alreadyKilled = False
        self.exist = True
        self.image = sprite        

class carotte(entite):

    def __init__(self,xx,yy,sprite,death,vie,damage,vitesse,gold):
        entite.__init__(self,"CAC",10,"NULL",1,"ENNEMIS",xx,yy,sprite)

        #image affiché à la mort de l'entité
        self.imageMort = death

        #a refaire autre part
        self.attack_sound = pygame.mixer.Sound("../sound/hello_carotte.wav")
        self.attack_sound.set_volume(0.1)
        
        #Modification des variables initiale selon la difficulté de jeu
        #or de la carotte : de base = 5
        self.gold=5 + gold
        self.degats = 1 + damage
        self.baseVelocity += vitesse
        self.velocity += vitesse
        self.vie += vie

        #hit box ( anciennement rect )
        self.hitbox = self.image[0].get_rect()
        self.hitbox.x = xx
        self.hitbox.y = yy
        #NE PAS UTILISER RECT POUR AUTRE CHOSE QUE LA GESTION DE COLLISION  + masque
        self.rect = self.hitbox
        self.mask = pygame.mask.from_surface(self.image[0])

        #valeures propre a la carotte:
        self.velocity = 4
        self.drift = 10
        self.driftdirx = 1
        self.driftdiry = 1
        self.baseVelocity=self.velocity



    def render(self,screen,xOffset,yOffset):
        if self.orientation==1:
            screen.blit(self.image[self.current],(xOffset+self.hitbox.x,yOffset+self.hitbox.y)) #affiche l'image de l'entite à la position indiqué par ses coord
        else:
            screen.blit(pygame.transform.flip(self.image[self.current],1,0),(xOffset+self.hitbox.x,yOffset+self.hitbox.y)) #affiche l'image de l'entite à la position indiqué par ses coord

            
    def update(self,entities):
        Xjoueur = entities[0].position[0]
        Yjoueur = entities[0].position[1]
        if not self.alreadyKilled:
            if(self.timer == 10):
                self.current=(self.current+1)%4
                self.timer = 0
            else:
                self.timer +=1
                
            #self.mask = pygame.mask.from_surface(self.image[self.current])

            self.isHittingSomething(entities)
            if self.velocity != 0:
                if self.drift!=0:
                    self.hitbox.x += self.driftdirx*2
                    self.hitbox.y += self.driftdiry*2
                    self.drift-=1
                else:
                    self.drift=random.randrange(20)
                    self.driftdirx = random.choice((-1,1))
                    self.driftdiry = random.choice((-1,1))
                if(Xjoueur < self.hitbox.x):
                    self.hitbox.x -= self.velocity
                    self.orientation=1
                elif(Xjoueur > self.hitbox.x):
                    self.hitbox.x += self.velocity
                    self.orientation=0
                if(Yjoueur < self.hitbox.y):
                    self.hitbox.y -= self.velocity
                elif(Yjoueur > self.hitbox.y):
                    self.hitbox.y += self.velocity
        else:
            self.miseAMort()

    def isHittingSomething(self,entities):
        for i in range(len(entities)):
                    if(i == 0): #on gere le joueur
                        if(self.hitbox.x + self.hitbox.width >= entities[i].position[0] and self.hitbox.x < entities[i].position[0] + entities[i].rect.width) and (self.hitbox.y + self.hitbox.height > entities[i].position[1] and self.hitbox.y < entities[i].position[1] + entities[i].rect.height):
                            if(entities[0].takeDamage(self.degats)):
                                pygame.mixer.Sound.play(self.attack_sound)
                    else: #puis les objets
                        None #faire pour objet plaçable
    
    def miseAMort(self):
        death_sound = pygame.mixer.Sound("../sound/splat.wav")
        if(self.alreadyKilled == False):
            death_sound.set_volume(0.1)
            pygame.mixer.Sound.play(death_sound)
            self.alreadyKilled = True
            self.timer = 0
            self.current = 3

        self.timer += 1
        self.image = self.imageMort
        self.image[self.current].set_alpha(200-self.timer)
        if(self.timer >=50):
            self.exist = False
            


class tomate(entite):


    def __init__(self,xx,yy,sprite,vie,damage,vitesse,gold):
        entite.__init__(self,"CAC",10,"NULL",2,"ENNEMIS",xx,yy,sprite)
        
        #or de la tomate :
        self.gold=10 + gold
        self.degats = 2 + damage
        self.baseVelocity += vitesse
        self.velocity = 3 +vitesse
        self.vie += vie

        #hit box ( anciennement rect )
        self.hitbox = self.image[0].get_rect()
        self.hitbox.height = self.hitbox.height-120
        self.hitbox.x = xx
        self.hitbox.y = yy
        #NE PAS UTILISER RECT POUR AUTRE CHOSE QUE LA GESTION DE COLLISION  + masque
        self.rect = self.hitbox
        self.mask = pygame.mask.from_surface(self.image[1])

        #valeures propre a la tomate:
        self.drift = 10
        self.driftdir = 1
        self.current = 1
        self.baseVelocity=self.velocity
        #a refaire autre part
        self.attack_sound = pygame.mixer.Sound("../sound/hello_carotte.wav")
        self.attack_sound.set_volume(0.1)

        




    def render(self,screen,xOffset,yOffset):
        if self.orientation==0:
            screen.blit(self.image[self.current],(xOffset+self.hitbox.x,yOffset+self.hitbox.y-100)) #affiche l'image de l'entite à la position indiqué par ses coord
        else:
            screen.blit(pygame.transform.flip(self.image[self.current],1,0),(xOffset+self.hitbox.x,yOffset+self.hitbox.y-100)) #affiche l'image de l'entite à la position indiqué par ses coord

    def update(self,entities):
        Xjoueur = entities[0].position[0]
        Yjoueur = entities[0].position[1]
        if not self.alreadyKilled:
            if(self.timer == 10):
                self.current=(self.current+1)%6
                if self.current == 0:
                    self.current += 1
                    
                if self.current>=2 and self.current<=6 or self.current>=9 and self.current<=12:
                    self.velocity=6
                else:
                    self.velocity=0
                self.timer = 0
            else:
                self.timer +=1
                
            #self.mask = pygame.mask.from_surface(self.image[self.current])

            self.isHittingSomething(entities)
            if self.velocity != 0:
                if self.drift==0:
                    self.drift=random.randrange(20)
                    self.driftdir = random.randrange(-5,5)
                else:
                    self.drift-=1
                if self.velocity != 0:
                    if(Xjoueur < self.hitbox.x):
                        self.hitbox.x -= self.velocity
                        self.hitbox.y += self.driftdir
                        self.orientation=1
                    elif(Xjoueur > self.hitbox.x):
                        self.hitbox.x += self.velocity
                        self.hitbox.y += self.driftdir
                        self.orientation=0
                    if(Yjoueur < self.hitbox.y):
                        self.hitbox.y -= self.velocity
                        self.hitbox.x += self.driftdir
                    elif(Yjoueur > self.hitbox.y):
                        self.hitbox.y += self.velocity
                        self.hitbox.x += self.driftdir
        else:
            self.miseAMort()

    def isHittingSomething(self,entities):
        for i in range(len(entities)):
                    if(i == 0): #on gere le joueur
                        if(self.hitbox.x + self.hitbox.width >= entities[i].position[0] and self.hitbox.x < entities[i].position[0] + entities[i].rect.width) and (self.hitbox.y + self.hitbox.height > entities[i].position[1] and self.hitbox.y < entities[i].position[1] + entities[i].rect.height):
                            if(entities[0].takeDamage(self.degats)):
                                pygame.mixer.Sound.play(self.attack_sound)
                    else: #puis les objets
                        None #faire pour objet plaçable

    def miseAMort(self):
        death_sound = pygame.mixer.Sound("../sound/splat.wav")
        if(self.alreadyKilled == False):
            death_sound.set_volume(0.1)
            pygame.mixer.Sound.play(death_sound)
            self.alreadyKilled = True
            self.timer = 0
        self.current= 0
        self.timer += 1
        self.image[self.current].set_alpha(200-self.timer)
        if(self.timer >=50):
            self.exist = False

class banane(entite):
    #Instanciation de l'entité banane
    def __init__(self,xx,yy,sprite,vie,damage,vitesse,gold):
        entite.__init__(self,"CAC",10,"NULL",4,"ENNEMIS",xx,yy,sprite)

        #a refaire autre part
        self.attack_sound = pygame.mixer.Sound("../sound/hello_carotte.wav")
        self.attack_sound.set_volume(0.1)

        self.gold= 20 + gold
        self.degats = 4 + damage
        self.baseVelocity = 1+ vitesse
        self.velocity =1+ vitesse
        self.vie += vie

        #hitbox ( anciennement rect )
        self.hitbox = self.image[0].get_rect()
        self.hitbox.x = xx 
        self.hitbox.y = yy

        self.hitbox.width -= 100
        self.hitbox.height -= 10

        #NE PAS UTILISER RECT POUR AUTRE CHOSE QUE LA GESTION DE COLLISION  + masque
        self.rect = self.hitbox
        self.mask = pygame.mask.from_surface(self.image[0])

        #valeures propre a la banane:
        self.drift = 0
        self.driftdirx = 1
        self.driftdiry = 1
        self.baseVelocity=self.velocity

    def render(self,screen,xOffset,yOffset):
        #Ligne test hitbox
        #pygame.draw.rect(screen,(250,250,250),(self.hitbox.x+xOffset,self.hitbox.y+yOffset,self.hitbox.width, self.hitbox.height))

        if self.orientation==1:
            screen.blit(self.image[self.current],(xOffset+self.hitbox.x - 50,yOffset+self.hitbox.y))                             #affiche l'image de l'entite à la position indiqué par ses coord
        else:
            screen.blit(pygame.transform.flip(self.image[self.current],1,0),(xOffset+self.hitbox.x-50,yOffset+self.hitbox.y))  #affiche l'image de l'entite à la position indiqué par ses coord


    def update(self,entities):

        Xjoueur = entities[0].position[0]
        Yjoueur = entities[0].position[1]

        if not self.alreadyKilled:

            if(self.timer == 10):
                self.current=(self.current+1)%4
                self.timer = 0
            else:
                self.timer +=1

            #self.mask = pygame.mask.from_surface(self.image[self.current])

            self.isHittingSomething(entities)
            if self.velocity != 0:
                if self.drift!=0:
                    self.hitbox.x += self.driftdirx*2
                    self.hitbox.y += self.driftdiry*2
                    self.drift-=1
                else:
                    self.drift=random.randrange(20)
                    self.driftdirx = random.choice((-1,1))
                    self.driftdiry = random.choice((-1,1))
                if(Xjoueur < self.hitbox.x):
                    self.hitbox.x -= self.velocity
                    self.orientation=1
                elif(Xjoueur > self.hitbox.x):
                    self.hitbox.x += self.velocity
                    self.orientation=0
                if(Yjoueur < self.hitbox.y):
                    self.hitbox.y -= self.velocity
                elif(Yjoueur > self.hitbox.y):
                    self.hitbox.y += self.velocity
        else:
            self.miseAMort()


    def isHittingSomething(self,entities):
        for i in range(len(entities)):
                    if(i == 0): #on gere le joueur
                        if(self.hitbox.x + self.hitbox.width >= entities[i].position[0] and self.hitbox.x < entities[i].position[0] + entities[i].rect.width) and (self.hitbox.y + self.hitbox.height > entities[i].position[1] and self.hitbox.y < entities[i].position[1] + entities[i].rect.height):
                            if(entities[0].takeDamage(self.degats)):
                                pygame.mixer.Sound.play(self.attack_sound)
                    else: #puis les objets
                        None #faire pour objet plaçable

    def miseAMort(self):

        death_sound = pygame.mixer.Sound("../sound/splat.wav")

        if(self.alreadyKilled == False):

            death_sound.set_volume(0.1)
            pygame.mixer.Sound.play(death_sound)
            self.alreadyKilled = True
            self.timer = 0
            self.current = 0

        self.timer += 1
        self.image[self.current].set_alpha(200-self.timer)
        if(self.timer >=50):
            self.exist = False