import pygame
import math
import os
pygame.init()

pygame.mixer.init()


HEIGTH_display = 600
WIDTH_display = 1280
gravi = (math.pi , 0.002)
choc = 0.8
tir = (None,None)

def load_images(path):
    images = []
    images_grande = []
    for file_name in os.listdir(path="data/courtmariocourt"):
        image = pygame.image.load(path + os.sep + file_name).convert()
        image_petit = pygame.transform.scale(image, (50,60))
        image_grande = pygame.transform.scale(image, (50,80))
        images_grande.append(image_grande)
        images.append(image_petit)
    return images

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
win.blit(fond,(0,0))

balles_sprites = pygame.sprite.Group()

run = True

class balle (pygame.sprite.Sprite):

    def __init__(self , x , y , img, poids):
        pygame.sprite.Sprite.__init__(self,balles_sprites)
        self.image = img
        self.rect = self.image.get_rect()
        self.long = self.rect[2]
        self.larg = self.rect[3]
        self.x = x
        self.y = y
        self.vitesse = 1
        self.angle = 10
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

basket = balle(200,250,baballe,1) 

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    win.blit(fond,(0,0))
    basket.mvmt()
    basket.rebond()
    basket.display()
    pygame.display.update()
    #print(basket.y)