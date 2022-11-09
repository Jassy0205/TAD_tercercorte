import pygame
pygame.init()

velx = 1
vely = 1
terminar = False

win = pygame.display.set_mode((760,640))

img = pygame.image.load("logo.png")
tam_image = img.get_rect()
tam_image.left = 50
tam_image.top = 100

while not terminar: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT : terminar = True
    tam_image.left+=velx
    tam_image.top+=vely 

    if tam_image.left<0 or tam_image.right>760:
        velx=-velx
    if tam_image.top<0 or tam_image.bottom>640:
        vely=-vely
        
    win.fill((0,0,0))
    win.blit(img, tam_image)
    pygame.display.flip()

pygame.quit