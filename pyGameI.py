import pygame
pygame.init()
win = pygame.display.set_mode((760,640))

img = pygame.image.load("2mod.jpg")

tam_image = img.get_rect()
tam_image.left = 50
tam_image.top = 0

win.fill((0,0,0))
win.blit(img, tam_image)
pygame.display.flip()
pygame.time.wait(5000)


