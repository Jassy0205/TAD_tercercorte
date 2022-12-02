from anytree import Node, RenderTree
import pygame
import sys
import random

class grafo():
    def __init__(self):
        pygame.init()

        self.alto = 850
        self.ancho = 920
        self.terminar_grafo= False

        self.user_text = ''
        self.value_input = ''

        self.base = 'Cantidad de nodos del arbol: '
        self.value = 'Valor del nodo: '
        self.input_rect = pygame.Rect(346, 5, 160, 30)

        self.img_mapa = pygame.image.load("MapaColombia.jpg")
        self.tam_mapa_rect =  None
        self.base_font = pygame.font.Font(None, 32)
        self.base_font_2 = pygame.font.Font(None, 23)

        self.win = pygame.display.set_mode((self.ancho, self.alto))
        self.win.fill((0,0,0))

        self.root = None
        self.length = None

        self.combo_1 = 'Ciudad origen'
        #self.options_1 = ['Villavicencio', 'Leticia', 'Pasto']
        self.draw_menu_1 = False
        self.rect_combo_1 = pygame.Rect(30, 70, 100, 25) 
        self.eleccion_1 = None
        self.rectas_options_1 = []

        self.combo_2 = 'Ciudad destino'
        #self.options_2 = ['San Andrés', 'Armenia', 'Leticia']
        self.draw_menu_2 = False
        self.rect_combo_2 = pygame.Rect(190, 70, 100, 25) 
        self.eleccion_2 = None
        self.rectas_options_2 = []

        self.color_menu = (255, 255, 255)
        self.color_option = (0, 0, 0)

        self.ciudades = ['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena',
                            'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Riohacha',
                            'Santa Marta', 'Valledupar', 'Villavicencio']
        self.relaciones = []
        #self.rectas_ciudades = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.rectas_ciudades = []
        self.grafos = []
        self.otros = []

        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.rojo = (100,30,22)

    def recorre_2(self):
        index = self.ciudades.index(self.eleccion_1)
        actual = self.relaciones[index]

        for i in range(len(actual)):
            actual_2 = actual[i]
            index_2 = self.ciudades.index(actual_2)
            
            actual_2_relaciones = self.relaciones[index_2]
            for i in range(len(actual_2_relaciones)):
                if actual_2_relaciones[i] == self.eleccion_2:
                    x = [actual_2, self.eleccion_2]
                    self.otros.append(x)

        print('HEllo', self.otros)

    def recorre(self):
        origen = self.ciudades.index(self.eleccion_1)
        destino = self.ciudades.index(self.eleccion_2)

        ciudades_origen = self.relaciones[origen]
        prev = []

        def busqueda(vector, prev):
            grafos = []
            estaba = False

            for i in range(len(vector)):
                actual = vector[i]
                if actual != self.eleccion_1:
                    if actual == self.eleccion_2:
                        grafos.append(actual)
                    else:
                        for i in range(len(prev)):
                            if actual == prev[i]:
                                estaba = True
                        
                        if estaba == False and len(prev) != 18:
                            index = self.ciudades.index(actual)
                            prev.insert(0, actual)
                            grafos.append(actual)
                            grafos.append(busqueda(self.relaciones[index], prev))
            return grafos
            
        self.grafos = busqueda(ciudades_origen, prev)
        self.recorre_2()
        self.dibujar_recorridos()
        self.dibujar_recorridos_2()
    
    def dibujar_recorridos_2(self):
        index = self.ciudades.index(self.eleccion_1)
        rect_inicial = self.rectas_ciudades[index]
        
        for i in range(len(self.otros)):
            actual_vector = self.otros[i]
            segundo_punto = actual_vector[0]
            tercer_punto = actual_vector[1]

            index_2 = self.ciudades.index(str(segundo_punto))
            index_3 = self.ciudades.index(str(tercer_punto))

            rect_2 = self.rectas_ciudades[index_2]
            rect_3 = self.rectas_ciudades[index_3]
            
            if i%2 == 0 or i == 0:
                pygame.draw.line(self.win, (230, 126, 34), (rect_inicial.left, rect_inicial.top), (rect_2.left,rect_2.top), 4)
                pygame.draw.line(self.win, (230, 126, 34), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)
            else: 
                pygame.draw.line(self.win, (136, 78, 160), (rect_inicial.left, rect_inicial.top), (rect_2.left,rect_2.top), 4)
                pygame.draw.line(self.win, (136, 78, 160), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)

    def dibujar_recorridos(self): 
        index = self.ciudades.index(self.eleccion_1)
        rect_inicial = self.rectas_ciudades[index]
        print(self.grafos, index)
        cont = 0

        for i in range(len(self.grafos)):
            print(type(self.grafos[0]))
            if cont == 0 and type(self.grafos[i]) is str:
                index_2 = self.ciudades.index(self.grafos[i])
                rect = self.rectas_ciudades[index_2]
                print('Hola', index_2, rect_inicial, rect)

                pygame.draw.line(self.win, (20,143, 119), (rect_inicial.left,rect_inicial.top), (rect.left,rect.top), 4)
                
                if type(self.grafos[i+1]) != str:
                    actual_2 = self.grafos[i+1]
                    for i in range(len(actual_2)):
                        if type(actual_2[i]) is str:
                            index_3 = self.ciudades.index(actual_2[i])
                            rect_2 = self.rectas_ciudades[index_3]
                            print('Hola', index_3, rect_inicial, rect_2)

                            pygame.draw.line(self.win, (20,143, 119), (rect.left,rect.top), (rect_2.left,rect_2.top), 4)
                        else: 
                            index_4 = self.ciudades.index(self.eleccion_2)
                            rect_3 = self.rectas_ciudades[index_4]
                            print('Hola', index_3, rect_inicial, rect_2)

                            pygame.draw.line(self.win, (20,143, 119), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)

                cont+=1
            elif type(self.grafos[i]) is str:
                index_2 = self.ciudades.index(self.grafos[i])
                rect = self.rectas_ciudades[index_2]
                print('Hola', index_2, rect_inicial, rect)

                pygame.draw.line(self.win, (46,134, 193), (rect_inicial.left,rect_inicial.top), (rect.left,rect.top), 4)
                
                if i != len(self.grafos)-1:
                    if type(self.grafos[i+1]) != str:
                        actual_2 = self.grafos[i+1]
                        for i in range(len(actual_2)):
                            if type(actual_2[i]) is str:
                                index_3 = self.ciudades.index(actual_2[i])
                                rect_2 = self.rectas_ciudades[index_3]
                                print('Hola', index_3, rect_inicial, rect_2)

                                pygame.draw.line(self.win, (46,134, 193), (rect.left,rect.top), (rect_2.left,rect_2.top), 4)
                            else: 
                                index_4 = self.ciudades.index(self.eleccion_2)
                                rect_3 = self.rectas_ciudades[index_4]
                                print('Hola', index_3, rect_inicial, rect_2)

                                pygame.draw.line(self.win, (46,134, 193), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)
            pygame.display.flip()

    def mapa_fondo(self):
        if self.tam_mapa_rect == None:
            tam_image = self.img_mapa.get_rect()
            tam_image.left += 360
            tam_image.top += 20
            self.tam_mapa_rect = tam_image

        self.win.blit(self.img_mapa, self.tam_mapa_rect)

    def combo_origen(self):
        pygame.draw.rect(self.win, self.color_menu, self.rect_combo_1, 0)
        self.img_1 = pygame.image.load("descarga.png")
        self.rect_mov1 = pygame.Rect(30, 70, 100, 25) 
        self.rect_mov1.left += 100
        self.win.blit(self.img_1, self.rect_mov1)

    def combo_destino(self):
        pygame.draw.rect(self.win, self.color_menu, self.rect_combo_2, 0)
        self.img_2 = pygame.image.load("descarga.png")
        self.rect_mov2 = pygame.Rect(190, 70, 100, 25) 
        self.rect_mov2.left += 100
        self.win.blit(self.img_2, self.rect_mov2)

    def inicio_juego(self):
        cont_1 = 0
        cont_2 = 0

        self.mapa_fondo()
        self.dibujar_nodos_mapa()
        self.combo_origen()
        self.combo_destino()
        self.relaciones_ciudades()

        while not self.terminar_grafo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  self.terminar_grafo = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos() 
                    if mouse_pos[0] >= self.rect_mov2.left and mouse_pos[0] <= self.rect_mov2.left+25:
                        if cont_1 == 0 or cont_1%2 == 0:
                            self.draw_menu_2 = True
                        else:
                            self.win.fill((0,0,0))
                            self.borrar_info_grafo()
                            self.draw_menu_2 = False
                        cont_1+= 1
                    elif mouse_pos[0] >= self.rect_mov1.left and mouse_pos[0] <= self.rect_mov1.left+25:
                        if cont_2 == 0 or cont_2%2 == 0:
                            self.draw_menu_1 = True
                        else:
                            self.win.fill((0,0,0))
                            self.borrar_info_grafo()
                            self.draw_menu_1 = False
                        cont_2+= 1
                    else:
                        if self.draw_menu_1 == True:
                            i = 0
                            while i <= len(self.rectas_options_1)-1:
                                actual = self.rectas_options_1[i]
                                if mouse_pos[1] <= actual.top+20 and mouse_pos[1] >= actual.top and mouse_pos[0] <= actual.left+90 and mouse_pos[0] >= actual.left:
                                    self.win.fill((0,0,0))
                                    self.eleccion_1 = self.ciudades[i]
                                    print(self.eleccion_1)
                                    self.borrar_info_grafo()
                                    self.draw_menu_1 = False
                                i+=1
                        if self.draw_menu_2 == True:
                            i = 0
                            while i <= len(self.rectas_options_2)-1:
                                actual = self.rectas_options_2[i]
                                if mouse_pos[1] <= actual.top+20 and mouse_pos[1] >= actual.top and mouse_pos[0] <= actual.left+90 and mouse_pos[0] >= actual.left:
                                    self.win.fill((0,0,0))
                                    self.eleccion_2 = self.ciudades[i]
                                    print(self.eleccion_2)
                                    self.borrar_info_grafo()
                                    self.draw_menu_2 = False
                                i+=1

                        if self.eleccion_1 != None and self.eleccion_2 != None:
                            self.grafos = []
                            self.recorre()

                if self.draw_menu_1:
                    for i, text in enumerate(self.ciudades):
                        rect = self.rect_combo_1.copy()

                        rect.y += (i+1) * self.rect_combo_1.height
                        self.rectas_options_1.insert(i, rect)
                        if len(self.rectas_options_1) > i+1:
                            self.rectas_options_1.pop(i+1)

                        pygame.draw.rect(self.win, self.color_menu, rect, 0)
                        msg = self.base_font_2.render(text, 1, self.color_option)
                        self.win.blit(msg, rect)
                elif self.draw_menu_2:
                    for i, text in enumerate(self.ciudades):
                        rect = self.rect_combo_2.copy()

                        rect.y += (i+1) * self.rect_combo_2.height
                        self.rectas_options_2.insert(i, rect)
                        if len(self.rectas_options_2) > i+1:
                            self.rectas_options_2.pop(i+1)

                        pygame.draw.rect(self.win, self.color_menu, rect, 0)
                        msg = self.base_font_2.render(text, 1, self.color_option)
                        self.win.blit(msg, rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def borrar_info_grafo(self):
        self.mapa_fondo()
        self.dibujar_nodos_mapa()
        self.combo_origen()
        self.combo_destino()
        self.dibujar_recorridos()

        if self.eleccion_1 != None: 
            msg = self.base_font_2.render(self.eleccion_1, 1, (0, 0, 0))
            rect = self.rect_combo_1.copy()
            rect.top += 7
            self.win.blit(msg, rect)
        if self.eleccion_2 != None: 
            msg = self.base_font_2.render(self.eleccion_2, 1, (0, 0, 0))
            rect = self.rect_combo_2.copy()
            rect.top += 7
            self.win.blit(msg, rect)

    def relaciones_ciudades(self):
        self.relaciones.append(('Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Neiva', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Pereira', 'Santa Marta'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Valledupar', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Villavicencio'))
        self.relaciones.append(('San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar'))

    def dibujar_nodos_mapa(self):
        tam_image_1 = self.img_mapa.get_rect()

        tam_image_1.top += 50
        tam_image_1.left += 405

        self.rectas_ciudades.insert(0, tam_image_1)
        if len(self.rectas_ciudades) > 1:
            self.rectas_ciudades.pop(1)
        pygame.draw.circle(self.win, self.rojo, (tam_image_1.left, tam_image_1.top), 4, 5)
        
        tam_image_2 = tam_image_1.copy()
        tam_image_2.left += 108
        tam_image_2.top += 331
        self.rectas_ciudades.insert(1, tam_image_2)
        if len(self.rectas_ciudades) > 2:
            self.rectas_ciudades.pop(2)
        pygame.draw.circle(self.win, self.rojo, (tam_image_2.left, tam_image_2.top), 4, 5)

        tam_image_3 = tam_image_2.copy()
        tam_image_3.left += 41
        tam_image_3.top -= 285
        self.rectas_ciudades.insert(2, tam_image_3)
        if len(self.rectas_ciudades) > 3:
            self.rectas_ciudades.pop(3)
        pygame.draw.circle(self.win, self.rojo, (tam_image_3.left, tam_image_3.top), 4, 5)

        tam_image_4 = tam_image_3.copy()
        tam_image_4.left += 73
        tam_image_4.top += 172
        self.rectas_ciudades.insert(3, tam_image_4)
        if len(self.rectas_ciudades) > 4:
            self.rectas_ciudades.pop(4)
        pygame.draw.circle(self.win, self.rojo, (tam_image_4.left, tam_image_4.top), 4, 5)

        tam_image_5 = tam_image_4.copy()
        tam_image_5.left -= 44
        tam_image_5.top += 108
        self.rectas_ciudades.insert(4, tam_image_5)
        if len(self.rectas_ciudades) > 5:
            self.rectas_ciudades.pop(5)
        pygame.draw.circle(self.win, self.rojo, (tam_image_5.left, tam_image_5.top), 4, 5)

        tam_image_6 = tam_image_5.copy()
        tam_image_6.left -= 108
        tam_image_6.top += 56
        self.rectas_ciudades.insert(5, tam_image_6)
        if len(self.rectas_ciudades) > 6:
            self.rectas_ciudades.pop(6)
        pygame.draw.circle(self.win, self.rojo, (tam_image_6.left, tam_image_6.top), 4, 5)

        tam_image_7 = tam_image_6.copy()
        tam_image_7.left += 49
        tam_image_7.top -= 313
        self.rectas_ciudades.insert(6, tam_image_7)
        if len(self.rectas_ciudades) > 7:
            self.rectas_ciudades.pop(7)
        pygame.draw.circle(self.win, self.rojo, (tam_image_7.left, tam_image_7.top), 4, 5)

        tam_image_8 = tam_image_7.copy()
        tam_image_8.left += 131
        tam_image_8.top += 113
        self.rectas_ciudades.insert(7, tam_image_8)
        if len(self.rectas_ciudades) > 8:
            self.rectas_ciudades.pop(8)
        pygame.draw.circle(self.win, self.rojo, (tam_image_8.left, tam_image_8.top), 4, 5)

        tam_image_9 = tam_image_8.copy()
        tam_image_9.left += 114
        tam_image_9.top += 535
        self.rectas_ciudades.insert(8, tam_image_9)
        if len(self.rectas_ciudades) > 9:
            self.rectas_ciudades.pop(9)
        pygame.draw.circle(self.win, self.rojo, (tam_image_9.left, tam_image_9.top), 4, 5)

        tam_image_10 = tam_image_9.copy()
        tam_image_10.left -= 250
        tam_image_10.top -= 463
        self.rectas_ciudades.insert(9, tam_image_10)
        if len(self.rectas_ciudades) > 10:
            self.rectas_ciudades.pop(10)
        pygame.draw.circle(self.win, self.rojo, (tam_image_10.left, tam_image_10.top), 4, 5)

        tam_image_11 = tam_image_10.copy()
        tam_image_11.left -= 15
        tam_image_11.top -= 110
        self.rectas_ciudades.insert(10, tam_image_11)
        if len(self.rectas_ciudades) > 11:
            self.rectas_ciudades.pop(11)
        pygame.draw.circle(self.win, self.rojo, (tam_image_11.left, tam_image_11.top), 4, 5)

        tam_image_12 = tam_image_11.copy()
        tam_image_12.left += 30
        tam_image_12.top += 257
        self.rectas_ciudades.insert(11, tam_image_12)
        if len(self.rectas_ciudades) > 12:
            self.rectas_ciudades.pop(12)
        pygame.draw.circle(self.win, self.rojo, (tam_image_12.left, tam_image_12.top), 4, 5)

        tam_image_13 = tam_image_12.copy()
        tam_image_13.left -= 22
        tam_image_13.top -= 82
        self.rectas_ciudades.insert(12, tam_image_13)
        if len(self.rectas_ciudades) > 13:
            self.rectas_ciudades.pop(13)
        pygame.draw.circle(self.win, self.rojo, (tam_image_13.left, tam_image_13.top), 4, 5)

        tam_image_14 = tam_image_13.copy()
        tam_image_14.left -= 67
        tam_image_14.top += 160
        self.rectas_ciudades.insert(13, tam_image_14)
        if len(self.rectas_ciudades) > 14:
            self.rectas_ciudades.pop(14)
        pygame.draw.circle(self.win, self.rojo, (tam_image_14.left, tam_image_14.top), 4, 5)

        tam_image_15 = tam_image_14.copy()
        tam_image_15.left += 191
        tam_image_15.top -= 457
        self.rectas_ciudades.insert(14, tam_image_15)
        if len(self.rectas_ciudades) > 15:
            self.rectas_ciudades.pop(15)
        pygame.draw.circle(self.win, self.rojo, (tam_image_15.left, tam_image_15.top), 4, 5)

        tam_image_16 = tam_image_15.copy()
        tam_image_16.left -= 55
        tam_image_16.top += 14
        self.rectas_ciudades.insert(15, tam_image_16)
        if len(self.rectas_ciudades) > 16:
            self.rectas_ciudades.pop(16)
        pygame.draw.circle(self.win, self.rojo, (tam_image_16.left, tam_image_16.top), 4, 5)

        tam_image_17 = tam_image_16.copy()
        tam_image_17.left += 40
        tam_image_17.top += 35
        self.rectas_ciudades.insert(16, tam_image_17)
        if len(self.rectas_ciudades) > 17:
            self.rectas_ciudades.pop(17)
        pygame.draw.circle(self.win, self.rojo, (tam_image_17.left, tam_image_17.top), 4, 5)

        tam_image_18 = tam_image_17.copy()
        tam_image_18.left -= 18
        tam_image_18.top += 280
        self.rectas_ciudades.insert(17, tam_image_18)
        if len(self.rectas_ciudades) > 18:
            self.rectas_ciudades.pop(18)
        pygame.draw.circle(self.win, self.rojo, (tam_image_18.left, tam_image_18.top), 4, 5)
