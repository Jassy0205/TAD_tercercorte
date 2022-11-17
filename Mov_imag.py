import pygame
pygame.init()

velx = 1
vely = 1
terminar = False
x = 50
y = 100
activar = False
cont = 0
mov = False

win = pygame.display.set_mode((760,640))
img = pygame.image.load("logo.png")
img2 = pygame.image.load("10mod.jpg")
tam_image = img2.get_rect()
tam_image.left = 50
tam_image.top = 100

while not terminar: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT : terminar = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if cont == 0:
                activar = True
            else: 
                if cont%2 == 0: 
                    activar = True
                    mov = False
                else: 
                    activar = False
            cont += 1
            print(cont)

    win.fill((0,0,0))
    mouse_pos = pygame.mouse.get_pos()
    if activar == True: 
        if mov == False and tam_image.collidepoint(pygame.mouse.get_pos()): 

            tam_image = img2.get_rect()
            tam_image.left = mouse_pos[0]
            tam_image.top = mouse_pos[1]
            mov = True
            win.blit(img2, tam_image)
        elif mov == True: 
            tam_image = img2.get_rect()
            tam_image.left = mouse_pos[0]
            tam_image.top = mouse_pos[1]

            win.blit(img2, tam_image)
        else: 
            win.blit(img2, tam_image)
    else:
        win.blit(img2, tam_image)

    pygame.display.flip()

pygame.quit

