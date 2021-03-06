import pygame
import math
import os
import time

pygame.init()

pygame.mixer.init()


HEIGTH_display = 600
WIDTH_display = 1280
gravi = (math.pi , 0.002)
choc = 0.8
tir = (None,None)

def CombiVect (tup1,tup2):
    x  = math.sin(tup1[0]) * tup1[1] + math.sin(tup2[0]) * tup2[1]
    y  = math.cos(tup1[0]) * tup1[1] + math.cos(tup2[0]) * tup2[1]
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    long  = math.hypot(x, y)

    return (angle, long)
  
def tir_click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            tir = event.pos
            return tir
    return (None,None)

win = pygame.display.set_mode((WIDTH_display,HEIGTH_display))
pygame.display.set_caption("Basket")

baballe = pygame.image.load("data/balls/baballe.png").convert_alpha()
baballe = pygame.transform.scale(baballe,(30,30))
fond =  pygame.image.load("data/fond.png").convert()
fond = pygame.transform.scale(fond,(1280,600))
time_img = pygame.image.load("data/time.png").convert_alpha()
time_img = pygame.transform.scale(time_img,(30,30))

win.blit(fond,(0,0))

balles_sprites = pygame.sprite.Group()
panier = pygame.sprite.Group()

myfont = pygame.font.SysFont("monospace",30)

run = True


class balle (pygame.sprite.Sprite):

    def __init__(self , x , y , img):
        pygame.sprite.Sprite.__init__(self,balles_sprites)
        self.image = img
        self.rect = self.image.get_rect()
        self.long = self.rect[2]
        self.larg = self.rect[3]
        self.x = x
        self.y = y
        self.vitesse = 1
        self.angle = 2
        self.tiree = True

    def display(self):
        win.blit(self.image,(self.x,self.y))
    
    def mvmt(self):
        if self.tiree:
            vit = (self.angle, self.vitesse)
            (self.angle, self.vitesse) = CombiVect(vit,gravi)
            self.x += math.sin(self.angle) * self.vitesse
            self.y -= math.cos(self.angle) * self.vitesse
        #self.vitesse *= frott

    def rebond(self):
        if self.x > WIDTH_display - self.long:
            self.x = 2*(WIDTH_display - self.long) - self.x
            self.angle = - self.angle
            self.vitesse *= choc

        elif self.x < 0:
            self.x =  - self.x
            self.angle = - self.angle
            self.vitesse *= choc

        if self.y > HEIGTH_display - self.larg - 185:
            self.y = 2*(HEIGTH_display - self.larg - 185) - self.y
            self.angle = math.pi - self.angle
            self.vitesse *= choc   

class timer():

    def __init__(self):
        self.debut_timer = time.time()
        self.temps = 40
        self.maxtime = int(self.debut_timer) + self.temps
        self.new_time = 0
        self.temps_restant = 0
    def timer(self):
        self.new_time = int(time.time())
        self.temps_restant = self.maxtime - self.new_time
        if self.temps_restant == 0:
            print("GAMEOVER Temps ecoulé")
            return False
        else:
            return True
        print(self.temps_restant)
    def affichage(self):
        temps = myfont.render(str(self.temps_restant),3,(255,0,0))
        win.blit(temps,(1240,5))
        win.blit(time_img,(1200,5))

basket = balle(200,250,baballe) 
timy = timer()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    win.blit(fond,(0,0))
    tir = tir_click()
    basket.mvmt()
    basket.rebond()
    basket.display()
    run = timy.timer()
    timy.affichage()
    pygame.display.update()
    #print(basket.y)