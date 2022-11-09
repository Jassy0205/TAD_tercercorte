import random
import pygame

class juego: 

    def __init__(self):
        pygame.init()

        self.alto = 500
        self.ancho = 320
        self.terminar = False

        self.win = pygame.display.set_mode((self.alto, self.ancho))
        self.win.fill((0,0,0))

    def crear_circulos(self):

        y = 100
        x = 140

        pri = 0
        seg = 0
        ter = 255

        circulo = pygame.draw.circle(self.win, (pri, seg, ter), (100,y), 20, 10)

        while not self.terminar:
            pygame.time.delay(200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.terminar = True

            circulo = pygame.draw.circle(self.win, (pri,seg,ter), (x,y), 20, 10)
            #recta = pygame.draw.line
            pygame.display.update()
            
            if x >= self.ancho:
                x = random.randrange(20, self.ancho-50, 1)
                y = random.randrange(20, self.alto-150, 1)
                self.win.fill((0,0,0))
                pri = random.randrange(0, 255, 1)
                seg = random.randrange(0, 255, 1)
                ter = random.randrange(0, 255, 1)
            else:
                x = x+40

        pygame.quit()
