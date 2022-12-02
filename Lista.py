import pygame 

class DropDown():
    
    def __init__(self):
        self.color_menu = (255, 255, 255)
        self.color_option = (0, 0, 0)
        self.rect_combo = pygame.Rect(500, 50, 100, 25) 
        self.font = pygame.font.Font(None, 32)
        self.main = "Hola"
        self.options = ['jiji', 'ijii', 'njnjnni']
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.terminar_combo = False
        self.rectas_options = []
        self.eleccion = None
        alto = 500
        ancho = 910
        self.base_font = pygame.font.Font(None, 32)
        self.win = pygame.display.set_mode((ancho, alto))
        self.win.fill((0,0,0))

    def combo_draw(self):
        pygame.draw.rect(self.win, self.color_menu, self.rect_combo, 0)
        self.img = pygame.image.load("descarga.png")
        self.rect_2 = pygame.Rect(500, 50, 100, 25) 
        self.rect_2.left += 100
        self.win.blit(self.img, self.rect_2)

    def draw(self):
        self.combo_draw()
        cont = 0

        while not self.terminar_combo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.terminar_combo = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos() 
                    if mouse_pos[0] >= self.rect_2.left and mouse_pos[0] <= self.rect_2.left+25:
                        if cont == 0 or cont%2 == 0:
                            self.draw_menu = True
                        else:
                            self.win.fill((0,0,0))
                            self.draw_menu = False
                        cont+= 1

                    else:
                        if self.draw_menu == True:
                            for i in range(len(self.rectas_options)):
                                actual = self.rectas_options[i]
                                if mouse_pos[1] <= actual.top+20 and mouse_pos[1] >= actual.top and mouse_pos[0] <= actual.left+90 and mouse_pos[0] >= actual.left:
                                    self.eleccion = self.options[i]
                                    self.win.fill((0,0,0))
                                    self.borrar_informacion_combobox(True)

                    print(self.eleccion)

            if self.draw_menu:
                for i, text in enumerate(self.options):
                    rect = self.rect_combo.copy()

                    rect.y += (i+1) * self.rect_combo.height
                    self.rectas_options.insert(i, rect)
                    if len(self.rectas_options) > i+1:
                        self.rectas_options.pop(i+1)

                    pygame.draw.rect(self.win, self.color_menu, rect, 0)
                    msg = self.font.render(text, 1, self.color_option)
                    self.win.blit(msg, rect)
            else:
                self.borrar_informacion_combobox(False)

            pygame.display.flip()

    def borrar_informacion_combobox(self, desplegado):
        self.combo_draw()

        if desplegado == True: 
            for i, text in enumerate(self.options):
                rect = self.rect_combo.copy()

                rect.y += (i+1) * self.rect_combo.height
                self.rectas_options.insert(i, rect)
                if len(self.rectas_options) > i+1:
                    self.rectas_options.pop(i+1)

                pygame.draw.rect(self.win, self.color_menu, rect, 0)
                msg = self.font.render(text, 1, self.color_option)
                self.win.blit(msg, rect)

        if self.eleccion != None: 
            msg = self.base_font.render(self.eleccion, 1, (0, 0, 0))
            self.win.blit(msg, self.rect_combo)
