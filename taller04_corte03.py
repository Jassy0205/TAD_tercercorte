from anytree import Node, RenderTree
import pygame
import sys
import random
import unicodedata

class grafo():
    def __init__(self):
        pygame.init()

        self.alto = 850
        self.ancho = 950
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
        self.base_font_3 = pygame.font.Font(None, 26)

        self.win = pygame.display.set_mode((self.ancho, self.alto))
        self.win.fill((0,0,0))

        self.root = None
        self.length = None

        self.text_dijktra = 'Dijktra'
        self.rect_dijk = pygame.Rect(30, 60, 125, 25) 
        self.algorithm_dijktra = False
        self.recorrido_corto = None

        self.text_rutas = 'rutas'
        self.rect_rutas = pygame.Rect(190, 60, 125, 25) 
        self.mostrar_rutas = False

        self.combo_1 = 'Origen:'
        self.draw_menu_1 = False
        self.rect_combo_1 = pygame.Rect(30, 100, 100, 25) 
        self.eleccion_1 = None
        self.rectas_options_1 = []

        self.combo_2 = 'Destino:'
        self.draw_menu_2 = False
        self.rect_combo_2 = pygame.Rect(190, 100, 100, 25) 
        self.eleccion_2 = None
        self.rectas_options_2 = []

        self.combo_3 = 'Arista:'
        self.input_rect_origen = pygame.Rect(115, 817, 115, 25) 
        self.user_text_origen = ""
        self.input_rect_destino = pygame.Rect(372, 817, 115, 25) 
        self.user_text_destino = ""
        self.input_rect_arista = pygame.Rect(607, 817, 70, 25) 
        self.user_text_arista = ""

        self.combo_4 = "Selected"
        self.rect_select_arista = pygame.Rect(760, 817, 115, 25) 

        self.color_menu = (255, 255, 255)
        self.color_option = (0, 0, 0)

        self.ciudades = ['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena',
                            'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Riohacha',
                            'Santa Marta', 'Valledupar', 'Villavicencio']
        self.relaciones = []
        self.dictionary_relations = None
        self.rectas_ciudades = []
        self.grafos = []
        self.otros = []

        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.rojo = (100,30,22)

    def crear_cajas_texto(self):
        text_surface = self.base_font.render(self.combo_1, True, (255, 255, 255))
        self.win.blit(text_surface, (30, 817))
        pygame.draw.rect(self.win, (255,255,255), self.input_rect_origen, 2)

        text_surface = self.base_font.render(self.combo_2, True, (255, 255, 255))
        self.win.blit(text_surface, (281, 817))
        pygame.draw.rect(self.win, (255,255,255), self.input_rect_destino, 2)

        text_surface = self.base_font.render(self.combo_3, True, (255, 255, 255))
        self.win.blit(text_surface, (525, 817))
        pygame.draw.rect(self.win, (255,255,255), self.input_rect_arista, 2)

    def crear_botones_grafo(self):
        pygame.draw.rect(self.win, (255,255,255), self.rect_dijk)
        pygame.draw.rect(self.win, (255,255,255), self.rect_rutas)
        pygame.draw.rect(self.win, (255,255,255), self.rect_select_arista)

        text_surface = self.base_font.render(self.text_dijktra, True, (0,0,0))
        self.win.blit(text_surface, (self.rect_dijk.x + (self.rect_dijk.width - text_surface.get_width()) / 2, (self.rect_dijk.y + (self.rect_dijk.height - text_surface.get_height())/2)))

        text_surface = self.base_font.render(self.text_rutas, True, (0,0,0))
        self.win.blit(text_surface, (self.rect_rutas.x + (self.rect_rutas.width - text_surface.get_width()) / 2, (self.rect_rutas.y + (self.rect_rutas.height - text_surface.get_height())/2)))

        self.crear_cajas_texto()
        text_surface = self.base_font.render(self.combo_4, True, (0,0,0))
        self.win.blit(text_surface, (self.rect_select_arista.x + (self.rect_select_arista.width - text_surface.get_width()) / 2, (self.rect_select_arista.y + (self.rect_select_arista.height - text_surface.get_height())/2)))

    def recorre(self):
        origen = self.ciudades.index(self.eleccion_1)
        destino = self.ciudades.index(self.eleccion_2)

        ciudades_origen = self.relaciones[origen].copy()
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
        
        while ciudades_origen:
            self.grafos.append(busqueda(ciudades_origen, prev))
            ciudades_origen.pop(0)
            prev = []

        self.dibujar_recorridos()

    def dibujar_recorridos(self): 
        index = self.ciudades.index(self.eleccion_1)
        rect_inicial = self.rectas_ciudades[index]
        cont = 0

        for i in range(len(self.grafos)):
            #print(type(self.grafos[0]))
            vector = self.grafos[i]

            for j in range(len(vector)):
                if cont == 0 and type(vector[j]) is str:
                    index_2 = self.ciudades.index(vector[j])
                    rect = self.rectas_ciudades[index_2]

                    pygame.draw.line(self.win, (255, 25, 255), (rect_inicial.left,rect_inicial.top), (rect.left,rect.top), 4)
                    
                    if type(vector[j+1]) != str and vector[j+1] != self.recorrido_corto:
                        actual_2 = vector[j+1]
                        for i in range(len(actual_2)):
                            if type(actual_2[i]) is str:
                                index_3 = self.ciudades.index(actual_2[i])
                                rect_2 = self.rectas_ciudades[index_3]

                                pygame.draw.line(self.win, (20,143, 119), (rect.left,rect.top), (rect_2.left,rect_2.top), 4)
                            else: 
                                index_4 = self.ciudades.index(self.eleccion_2)
                                rect_3 = self.rectas_ciudades[index_4]

                                pygame.draw.line(self.win, (20,143, 119), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)

                    cont+=1
                elif type(vector[j]) is str:
                    index_2 = self.ciudades.index(vector[j])
                    rect = self.rectas_ciudades[index_2]

                    pygame.draw.line(self.win, (255, 25, 255), (rect_inicial.left,rect_inicial.top), (rect.left,rect.top), 4)
                    
                    if j != len(vector)-1:
                        if type(vector[j+1]) != str and vector[j+1] != self.recorrido_corto:
                            actual_2 = vector[j+1]
                            for i in range(len(actual_2)):
                                if type(actual_2[i]) is str:
                                    index_3 = self.ciudades.index(actual_2[i])
                                    rect_2 = self.rectas_ciudades[index_3]

                                    pygame.draw.line(self.win, (46,134, 193), (rect.left,rect.top), (rect_2.left,rect_2.top), 4)
                                else: 
                                    index_4 = self.ciudades.index(self.eleccion_2)
                                    rect_3 = self.rectas_ciudades[index_4]

                                    pygame.draw.line(self.win, (46,134, 193), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)
                pygame.display.flip()

    def mapa_fondo(self):
        if self.tam_mapa_rect == None:
            tam_image = self.img_mapa.get_rect()
            tam_image.left += 360
            tam_image.top += 35
            self.tam_mapa_rect = tam_image

        self.win.blit(self.img_mapa, self.tam_mapa_rect)

    def combo_origen(self):
        pygame.draw.rect(self.win, self.color_menu, self.rect_combo_1, 0)
        self.img_1 = pygame.image.load("descarga.png")
        self.rect_mov1 = pygame.Rect(30, 100, 100, 25) 
        self.rect_mov1.left += 100
        self.win.blit(self.img_1, self.rect_mov1)

    def combo_destino(self):
        pygame.draw.rect(self.win, self.color_menu, self.rect_combo_2, 0)
        self.img_2 = pygame.image.load("descarga.png")
        self.rect_mov2 = pygame.Rect(190, 100, 100, 25) 
        self.rect_mov2.left += 100
        self.win.blit(self.img_2, self.rect_mov2)

    def inicio_juego(self):
        cont_1 = 0
        cont_2 = 0
        cont_3 = 0
        cont_4 = 0

        self.mapa_fondo()
        self.dibujar_nodos_mapa()
        self.combo_origen()
        self.combo_destino()
        self.relaciones_ciudades()
        self.crear_botones_grafo()

        while not self.terminar_grafo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  self.terminar_grafo = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos() 
                    if mouse_pos[0] >= self.rect_mov2.left and mouse_pos[0] <= self.rect_mov2.left+25 and mouse_pos[1] >= self.rect_mov2.top and mouse_pos[1] <= self.rect_mov2.top+20:
                        if cont_1 == 0 or cont_1%2 == 0:
                            self.draw_menu_2 = True
                        else:
                            self.win.fill((0,0,0))
                            self.borrar_info_grafo()
                            self.draw_menu_2 = False
                        cont_1+= 1
                    elif mouse_pos[0] >= self.rect_mov1.left and mouse_pos[0] <= self.rect_mov1.left+25 and mouse_pos[1] >= self.rect_mov1.top and mouse_pos[1] <= self.rect_mov1.top+20:
                        if cont_2 == 0 or cont_2%2 == 0:
                            self.draw_menu_1 = True
                        else:
                            self.win.fill((0,0,0))
                            self.borrar_info_grafo()
                            self.draw_menu_1 = False
                        cont_2+= 1
                    elif mouse_pos[0] >= self.rect_dijk.left and mouse_pos[0] <= self.rect_dijk.left+100 and mouse_pos[1] >= self.rect_dijk.top and mouse_pos[1] <= self.rect_dijk.top+20:
                        if cont_3 == 0 or cont_3%2 == 0:
                            self.algorithm_dijktra = True
                        else:
                            self.win.fill((0,0,0))
                            self.algorithm_dijktra = False
                            self.borrar_info_grafo()
                            cont_3 += 1
                        print('dij', self.algorithm_dijktra, cont_3)
                    elif mouse_pos[0] >= self.rect_rutas.left and mouse_pos[0] <= self.rect_rutas.left+100 and mouse_pos[1] >= self.rect_rutas.top and mouse_pos[1] <= self.rect_rutas.top+20:
                        if cont_4 == 0 or cont_4%2 == 0:
                            self.mostrar_rutas = True
                        else:
                            self.win.fill((0,0,0))
                            self.mostrar_rutas = False
                            self.borrar_info_grafo()
                        print('ru', self.mostrar_rutas)
                        cont_4 += 1
                    elif mouse_pos[0] >= self.input_rect_origen.left and mouse_pos[0] <= self.input_rect_origen.left+100 and mouse_pos[1] >= self.input_rect_origen.top and mouse_pos[1] <= self.input_rect_origen.top+20:
                        self.ingreso_ciudad_origen()
                    elif mouse_pos[0] >= self.input_rect_destino.left and mouse_pos[0] <= self.input_rect_destino.left+100 and mouse_pos[1] >= self.input_rect_destino.top and mouse_pos[1] <= self.input_rect_destino.top+20:
                        self.ingreso_ciudad_destino()
                    elif mouse_pos[0] >= self.input_rect_arista.left and mouse_pos[0] <= self.input_rect_arista.left+100 and mouse_pos[1] >= self.input_rect_arista.top and mouse_pos[1] <= self.input_rect_arista.top+20:
                        self.ingreso_distancia_arista()
                    elif mouse_pos[0] >= self.rect_select_arista.left and mouse_pos[0] <= self.rect_select_arista.left+100 and mouse_pos[1] >= self.rect_select_arista.top and mouse_pos[1] <= self.rect_select_arista.top+20:
                        self.cambio_aristas()

                    self.eleccion_combobox(mouse_pos)

                if self.algorithm_dijktra == True and self.eleccion_1 != None and self.eleccion_2 != None:
                    if cont_3 == 0 or cont_3%2 == 0:
                        recorrido = self.dijkstra(self.dictionary_relations, self.eleccion_1)
                        self.definir_recorrido_corto(recorrido)
                        cont_3 += 1
                
                if self.eleccion_1 != None and self.eleccion_2 != None and self.mostrar_rutas == True:
                    self.grafos = []
                    self.recorre()

                self.mostrar_combobox()
                self.mostrar_rutas_pant()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def cambio_aristas(self):
        if self.user_text_origen != "" and self.user_text_destino != "" and self.user_text_arista != "": 
            origen_in = unicodedata.normalize('NFKD', self.user_text_origen).encode('ASCII', 'ignore').strip().lower()
            destino_in = unicodedata.normalize('NFKD', self.user_text_destino).encode('ASCII', 'ignore').strip().lower()

            if origen_in == b'santamarta':
                origen_in = b'santa marta'
            elif origen_in == b'sanandres':
                origen_in = b'san andres'
            
            for clave in self.dictionary_relations: 
                if unicodedata.normalize('NFKD', clave).encode('ASCII', 'ignore').strip().lower() == origen_in:
                    print(unicodedata.normalize('NFKD', self.user_text_origen).encode('ASCII', 'ignore').strip().lower())
                    valor = self.dictionary_relations[clave]
                    for clave_2 in self.dictionary_relations[clave]:
                        if unicodedata.normalize('NFKD', clave_2).encode('ASCII', 'ignore').strip().lower() == destino_in:
                            print(self.dictionary_relations[clave][clave_2])
                            self.dictionary_relations[clave][clave_2] = int(self.user_text_arista)
                            print(unicodedata.normalize('NFKD', self.user_text_destino).encode('ASCII', 'ignore').strip().lower(), self.dictionary_relations[clave_2])

    def ingreso_ciudad_origen(self):
        terminar = False

        while terminar == False: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  terminar = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: 
                        self.user_text_origen = self.user_text_origen[:-1]
                        self.win.fill((0,0,0))
                        self.borrar_info_grafo()
                    elif event.key == pygame.K_SPACE:
                        terminar = True
                    else:
                        self.user_text_origen += event.unicode

            text_surface = self.base_font_3.render(self.user_text_origen, True, (0,255,255))
            self.win.blit(text_surface, (120,820))
            pygame.display.flip()

    def ingreso_ciudad_destino(self):
        terminar = False

        while terminar == False: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  terminar = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: 
                        self.user_text_destino = self.user_text_destino[:-1]
                        self.win.fill((0,0,0))
                        self.borrar_info_grafo()
                    elif event.key == pygame.K_SPACE:
                        terminar = True
                    else:
                        self.user_text_destino += event.unicode

            text_surface = self.base_font_3.render(self.user_text_destino, True, (0,255,255))
            self.win.blit(text_surface, (377,819))
            pygame.display.flip()

    def ingreso_distancia_arista(self):
        terminar = False

        while terminar == False: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  terminar = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: 
                        self.user_text_arista = self.user_text_arista[:-1]
                        self.win.fill((0,0,0))
                        self.borrar_info_grafo()
                    elif event.key == pygame.K_SPACE:
                        terminar = True
                    else:
                        r = self.validar_int(event.unicode)
                        print(r)

                        if r != False: 
                            self.user_text_arista += event.unicode

            text_surface = self.base_font_3.render(self.user_text_arista, True, (0,255,255))
            self.win.blit(text_surface, (612,819))
            pygame.display.flip()

    def validar_int(self, numero):
        try:
            conversion = int(numero)
            return conversion
        except:
            return False

    def definir_recorrido_corto(self, recorrido):
        for actual in recorrido: 
            f = len(actual)-1

            if actual[f] == self.eleccion_2:
                self.recorrido_corto = actual
                cont = self.recorrido_corto.count(self.eleccion_1)

                while cont > 1: 
                    self.recorrido_corto.pop(0)
                    cont -= 1
        
        self.visualizar_recorrido_corto()

    def visualizar_recorrido_corto (self):
        i = 0
        rect_recorrido_corto = pygame.Rect(150, 10, 100, 25) 

        if self.recorrido_corto != None:
            while i < len(self.recorrido_corto)-1:
                actual = self.recorrido_corto[i]
                index = self.ciudades.index(actual)
                rect = self.rectas_ciudades[index]

                i+=1
                actual_1 = self.recorrido_corto[i]
                index_1 = self.ciudades.index(actual_1)
                rect_1 = self.rectas_ciudades[index_1]

                pygame.draw.line(self.win, (0, 0, 0), (rect.left,rect.top), (rect_1.left,rect_1.top), 8)

            text_surface = self.base_font_2.render(str(self.recorrido_corto), True, (255,255,255))
        else:
            text_surface = self.base_font_2.render(self.eleccion_1, True, (255,255,255))

        self.win.blit(text_surface, (rect_recorrido_corto.x + (rect_recorrido_corto.width - text_surface.get_width()) / 2, (rect_recorrido_corto.y + (rect_recorrido_corto.height - text_surface.get_height())/2)))

    def mostrar_combobox(self):
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

    def mostrar_rutas_pant(self):
        if self.eleccion_1 != None and self.eleccion_2 != None and self.mostrar_rutas == True:
            self.dibujar_recorridos()

    def eleccion_combobox(self, mouse_pos):
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

        if self.algorithm_dijktra == True:
            self.algorithm_dijktra = False
            self.win.fill((0,0,0))
            self.borrar_info_grafo()
            self.algorithm_dijktra = True
            recorrido = self.dijkstra(self.dictionary_relations, self.eleccion_1)
            self.definir_recorrido_corto(recorrido)

    def dijkstra(self, Grafo, salida):
        dist, prev = {}, {}
        result = []
        recorrido = []

        for vertice in Grafo:
            dist[vertice] = float("inf")
            prev[vertice] = None
        dist[salida] = 0

        vertice_visited = [vertice for vertice in Grafo]

        while vertice_visited:
            u = min(vertice_visited, key=dist.get)
            vertice_visited.remove(u)
            result.append(u)

            for vecino in Grafo[u]:
                vector = []
                if vecino in vertice_visited and dist[vecino] > dist[u] + Grafo[u][vecino]:
                    real = None
                    index = -1
                    for vertice in recorrido: 
                        actual_vector = vertice
                        i = len(actual_vector)
                        for valores in actual_vector:
                            if valores == u and actual_vector[i-1] == valores:
                                real = actual_vector
                            elif valores == vecino:
                                index = recorrido.index(actual_vector)
                    if index != -1:
                        recorrido.pop(index)
                        index = -1
                    
                    if u != salida:
                        if real != None: 
                            vector = [salida]
                            vector.extend(real)
                            vector.append(vecino)
                        else: 
                            vector = [salida, u, vecino]
                    else:
                        vector = [salida, vecino]

                    recorrido.append(vector)
                    dist[vecino] = dist[u] + Grafo[u][vecino]
                    prev[vecino] = u

        return recorrido

    def borrar_info_grafo(self):
        self.mapa_fondo()
        self.dibujar_nodos_mapa()
        self.combo_origen()
        self.combo_destino()
        self.mostrar_rutas_pant()
        self.crear_botones_grafo()
        if self.algorithm_dijktra == True: 
            self.visualizar_recorrido_corto()

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
        self.relaciones.append(['Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Neiva', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Pereira', 'Santa Marta'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Valledupar', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Villavicencio'])
        self.relaciones.append(['San Andrés', 'Armenia', 'Barranquilla', 'Bucaramanga', 'Bogotá', 'Cali', 'Cartagena', 'Cúcuta', 'Leticia', 'Medellin', 'Monteria', 'Neiva', 'Pereira', 'Pasto', 'Santa Marta', 'Valledupar'])
        self.valores_recorridos()

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

    def valores_recorridos(self):
        self.dictionary_relations = {
            self.ciudades[0] : {vertice: random.randint(16, 580) for vertice in self.relaciones[0]},
            self.ciudades[1] : {vertice: random.randint(1, 400) for vertice in self.relaciones[1]},
            self.ciudades[2] : {vertice: random.randint(8, 500) for vertice in self.relaciones[2]},
            self.ciudades[3] : {vertice: random.randint(9, 980) for vertice in self.relaciones[3]},
            self.ciudades[4] : {vertice: random.randint(20, 50) for vertice in self.relaciones[4]},
            self.ciudades[5] : {vertice: random.randint(35, 190) for vertice in self.relaciones[5]},
            self.ciudades[6] : {vertice: random.randint(18, 200) for vertice in self.relaciones[1]},
            self.ciudades[7] : {vertice: random.randint(29, 60) for vertice in self.relaciones[1]},
            self.ciudades[8] : {vertice: random.randint(72, 324) for vertice in self.relaciones[1]},
            self.ciudades[9] : {vertice: random.randint(269, 412) for vertice in self.relaciones[1]},
            self.ciudades[10] : {vertice: random.randint(1, 25) for vertice in self.relaciones[1]},
            self.ciudades[11] : {vertice: random.randint(5, 59) for vertice in self.relaciones[1]},
            self.ciudades[12] : {vertice: random.randint(80, 1000) for vertice in self.relaciones[1]},
            self.ciudades[13] : {vertice: random.randint(15, 24) for vertice in self.relaciones[1]},
            self.ciudades[14] : {vertice: random.randint(860, 870) for vertice in self.relaciones[1]},
            self.ciudades[15] : {vertice: random.randint(1, 9) for vertice in self.relaciones[1]},
            self.ciudades[16] : {vertice: random.randint(56, 70) for vertice in self.relaciones[1]},
            self.ciudades[17] : {vertice: random.randint(6, 15) for vertice in self.relaciones[1]},
        }

#------------------------------ No útil ya -----------------------------------
    def dibujar_recorridos_2(self):
        index = self.ciudades.index(self.eleccion_1)
        rect_inicial = self.rectas_ciudades[index]
        print(self.otros)
        for i in range(len(self.otros)):
            actual_vector = self.otros[i]
            segundo_punto = actual_vector[0]
            tercer_punto = actual_vector[1]

            index_2 = self.ciudades.index(str(segundo_punto))
            index_3 = self.ciudades.index(str(tercer_punto))

            rect_2 = self.rectas_ciudades[index_2]
            rect_3 = self.rectas_ciudades[index_3]
            
            if i%2 == 0 or i == 0:
                pygame.draw.line(self.win, (255, 25, 255), (rect_inicial.left, rect_inicial.top), (rect_2.left,rect_2.top), 4)
                pygame.draw.line(self.win, (255, 25, 255), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)
            else: 
                pygame.draw.line(self.win, (255, 25, 255), (rect_inicial.left, rect_inicial.top), (rect_2.left,rect_2.top), 4)
                pygame.draw.line(self.win, (255, 25, 255), (rect_2.left,rect_2.top), (rect_3.left,rect_3.top), 4)

        pygame.display.flip()

    def recorre_2(self):
        index = self.ciudades.index(self.eleccion_1)
        actual = self.relaciones[index]
        print(self.relaciones[index], 'aja')

        for i in range(len(actual)):
            actual_2 = actual[i]
            index_2 = self.ciudades.index(actual_2)
            
            actual_2_relaciones = self.relaciones[index_2]
            for i in range(len(actual_2_relaciones)):
                if actual_2_relaciones[i] == self.eleccion_2:
                    x = [actual_2, self.eleccion_2]
                    self.otros.append(x)

        print(self.otros, 'hello')

'''     self.relaciones.append({'Armenia': 100, 'Barranquilla': 50, 'Bucaramanga': 1000, 'Bogotá': 29, 'Cali': 880, 'Cartagena': 1096, 'Cúcuta': 12, 'Leticia': 959, 'Medellin': 215, 'Monteria': 758, 'Neiva': 345, 'Pereira': 958, 'Pasto': 648, 'Santa Marta': 1055, 'Valledupar': 648, 'Villavicencio': 364})
        self.relaciones.append({'San Andrés': 560, 'Barranquilla': 215, 'Bucaramanga':1025, 'Bogotá': 325, 'Cali': 648, 'Cartagena': 645, 'Cúcuta': 36, 'Medellin': 13, 'Monteria': 564, 'Neiva': 659, 'Pasto': 326, 'Santa Marta': 158, 'Valledupar': 458, 'Villavicencio': 478})
        self.relaciones.append({'San Andrés': 254, 'Armenia': 854, 'Bucaramanga': 515, 'Bogotá': 5447, 'Cali': 645, 'Cartagena': 887, 'Cúcuta': 5487, 'Leticia': 2154, 'Medellin': 325, 'Monteria': 169, 'Neiva': 698, 'Pereira': 57, 'Pasto': 13, 'Santa Marta': 125, 'Valledupar': 256, 'Villavicencio': 36})
        self.relaciones.append({'San Andrés': 547, 'Armenia': 215, 'Barranquilla':255, 'Bogotá': 1025, 'Cali': 987, 'Cartagena': 985, 'Cúcuta': 745, 'Leticia': 652, 'Medellin': 324, 'Monteria': 329, 'Neiva': 603, 'Pereira': 569, 'Pasto': 763, 'Santa Marta': 1156, 'Valledupar': 378, 'Villavicencio': 906})
        self.relaciones.append({'San Andrés': 129, 'Armenia': 1048, 'Barranquilla': 895, 'Bucaramanga': 645, 'Cali': 516, 'Cartagena': 19, 'Cúcuta': 325, 'Leticia': 22, 'Medellin': 658, 'Monteria': 756, 'Neiva': 1548, 'Pereira': 453, 'Pasto': 1001, 'Santa Marta': 132, 'Valledupar': 326, 'Villavicencio': 856})
        self.relaciones.append({'San Andrés': 632, 'Armenia': 157, 'Barranquilla': 908, 'Bucaramanga': 564, 'Bogotá': 36, 'Cartagena': 75, 'Cúcuta': 504, 'Leticia': 95, 'Medellin': 958, 'Monteria': 345, 'Neiva': 632, 'Pereira': 623, 'Pasto': 632, 'Santa Marta': 1007, 'Valledupar': 1096, 'Villavicencio': 563})
        self.relaciones.append({'San Andrés': 38, 'Armenia': 57, 'Barranquilla': 62, 'Bucaramanga': 79, 'Bogotá': 81, 'Cali': 1078, 'Cúcuta': 655, 'Leticia': 245, 'Medellin': 31, 'Monteria': 458, 'Neiva': 625, 'Pereira': 326, 'Pasto': 932, 'Santa Marta': 1013, 'Valledupar': 459, 'Villavicencio': 263})
        self.relaciones.append({'San Andrés': 1058, 'Armenia': 954, 'Barranquilla': 325, 'Bucaramanga': 423, 'Bogotá': 1053, 'Cali': 64, 'Cartagena': 139, 'Leticia': 52, 'Medellin': 695, 'Monteria': 425, 'Neiva': 319, 'Pereira': 769, 'Pasto': 632, 'Santa Marta': 546, 'Valledupar': 692, 'Villavicencio': 752})
        self.relaciones.append({'San Andrés': 236, 'Barranquilla': 875, 'Bucaramanga': 489, 'Bogotá': 605, 'Cali': 986, 'Cartagena': 365, 'Cúcuta': 1011, 'Medellin': 750, 'Monteria': 465, 'Pereira': 1069, 'Santa Marta': 1056})
        self.relaciones.append({'San Andrés': 1023, 'Armenia': 782, 'Barranquilla': 752, 'Bucaramanga': 512, 'Bogotá': 983, 'Cali': 129, 'Cartagena': 638, 'Cúcuta': 615, 'Leticia': 365, 'Monteria': 1098, 'Neiva': 857, 'Pereira': 745, 'Pasto': 632, 'Santa Marta': 706, 'Valledupar': 632, 'Villavicencio': 201})
        self.relaciones.append({'San Andrés': 152, 'Armenia': 632, 'Barranquilla': 654, 'Bucaramanga': 857, 'Bogotá': 326, 'Cali': 754, 'Cartagena': 320, 'Cúcuta': 1015, 'Leticia': 359, 'Medellin': 895, 'Neiva': 426, 'Pereira': 305, 'Pasto': 1035, 'Santa Marta': 346, 'Valledupar': 952, 'Villavicencio': 104})
        self.relaciones.append({'San Andrés': 908, 'Armenia': 1205, 'Barranquilla': 326, 'Bucaramanga': 372, 'Bogotá': 421, 'Cali': 651, 'Cartagena': 569, 'Cúcuta': 1054, 'Medellin': 36, 'Monteria': 22, 'Pereira': 34, 'Pasto': 356, 'Santa Marta': 1000, 'Valledupar': 309, 'Villavicencio': 196})
        self.relaciones.append({'San Andrés': 1023, 'Barranquilla': 1006, 'Bucaramanga': 906, 'Bogotá': 205, 'Cali': 1052, 'Cartagena': 713, 'Cúcuta': 129, 'Leticia': 298, 'Medellin': 53, 'Monteria': 96, 'Neiva': 61, 'Pasto': 726, 'Santa Marta': 105, 'Valledupar': 136, 'Villavicencio': 372})
        self.relaciones.append({'San Andrés': 1084, 'Armenia': 896, 'Barranquilla': 643, 'Bucaramanga': 111, 'Bogotá': 907, 'Cali': 260, 'Cartagena': 1027, 'Cúcuta': 1035, 'Medellin': 49, 'Monteria': 106, 'Neiva': 185, 'Pereira': 549, 'Santa Marta': 164, 'Valledupar': 470, 'Villavicencio': 894})
        self.relaciones.append({'San Andrés': 256, 'Armenia': 871, 'Barranquilla': 753, 'Bucaramanga': 1111, 'Bogotá': 350, 'Cali': 609, 'Cartagena': 1109, 'Cúcuta': 1105, 'Leticia': 86, 'Medellin': 365, 'Monteria': 265, 'Neiva': 296, 'Pereira': 345, 'Pasto': 625, 'Santa Marta': 783, 'Valledupar': 322, 'Villavicencio': 103})
        self.relaciones.append({'San Andrés': 302, 'Armenia': 259, 'Barranquilla': 75, 'Bucaramanga': 21, 'Bogotá': 653, 'Cali': 892, 'Cartagena': 135, 'Cúcuta': 369, 'Leticia': 705, 'Medellin': 255, 'Monteria': 163, 'Neiva': 722, 'Pereira': 627, 'Pasto': 555, 'Valledupar': 936, 'Villavicencio': 888})
        self.relaciones.append({'San Andrés': 615, 'Armenia': 315, 'Barranquilla': 88, 'Bucaramanga': 19, 'Bogotá': 1045, 'Cali': 765, 'Cartagena': 1001, 'Cúcuta': 154, 'Medellin': 892, 'Monteria': 365, 'Neiva': 205, 'Pereira': 635, 'Pasto': 183, 'Santa Marta': 777, 'Villavicencio': 333})
        self.relaciones.append({'San Andrés': 789, 'Armenia': 98, 'Barranquilla': 93, 'Bucaramanga': 5, 'Bogotá': 1084, 'Cali': 365, 'Cartagena': 925, 'Cúcuta': 816, 'Leticia': 465, 'Medellin': 265, 'Monteria': 654, 'Neiva': 915, 'Pereira': 666, 'Pasto': 515, 'Santa Marta': 323, 'Valledupar': 845})'''
    