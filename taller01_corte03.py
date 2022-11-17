import pygame, sys

class listas: 

    def __init__(self):
        pygame.init()

        self.alto = 430
        self.ancho = 800
        self.terminar = False

        self.base = 'Cantidad de nodos a graficar: '
        self.base_font = pygame.font.Font(None, 32)

        self.win = pygame.display.set_mode((self.ancho, self.alto))
        self.win.fill((0,0,0))

    def input_title(self):
        text_surface = self.base_font.render(self.base, True, (255,255,50))
        self.win.blit(text_surface, (30,10))

    def validar_int(self, numero):
        try:
            conversion = int(numero)
            return conversion
        except:
            return False

    def input_screen(self):
        self.input_title()
        input_rect = pygame.Rect(346, 5, 100, 30)
        color = pygame.Color.b
        user_text = ''

        while not self.terminar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.terminar = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: 
                        user_text = user_text[:-1]
                        self.win.fill((0,0,0))
                        self.input_title()
                    else:
                        user_text += event.unicode
                        r = self.validar_int(user_text)
                        print(r)
                        self.draw_nodes(r)

            pygame.draw.rect(self.win, (255,255,255), input_rect, 2)
            text_surface = self.base_font.render(user_text, True, (0,255,255))
            self.win.blit(text_surface, (350,10))
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

    def draw_nodes(self, nodes):
        x = 50
        y = 90
        i = 0
        cont = self.ancho/7

        while i < nodes:
            pygame.draw.circle(self.win, (100,10,255), (x,y), 20)
            xfinal = x+(cont-25)
            pygame.draw.line(self.win, (100,0,105), (x+25,y), (xfinal,y))
            x += cont
            
            if y > self.alto+6:
                self.out_range()
                i = nodes

            if x >= self.ancho:
                y += 50
                x = 50
            
            i += 1

    def out_range(self):
        text = '------------ NO SPACE ---------------'
        text_surface = self.base_font.render(text, True, (255,0,0))
        self.win.blit(text_surface, (170,self.alto-20))


