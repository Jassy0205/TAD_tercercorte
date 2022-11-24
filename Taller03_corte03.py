from anytree import Node, RenderTree
import pygame
import sys

class arbol():
    def __init__(self):
        pygame.init()

        self.alto = 500
        self.ancho = 850
        self.terminar = False
        self.terminar_1 = False

        self.user_text = ''

        self.base = 'Cantidad de nodos del arbol: '
        self.value = 'Valor del nodo: '
        self.father = 'Valor del padre: '
        self.input_rect = pygame.Rect(346, 5, 100, 30)

        self.numeros = 0
        self.nodes = []
        self.parents = []
        self.ubicacion = []

        self.base_font = pygame.font.Font(None, 32)

        self.win = pygame.display.set_mode((self.ancho, self.alto))
        self.win.fill((0,0,0))

        print("guhu")

        '''root = Node(10)

        level_1_child_1 = Node(34, parent=root)
        level_1_child_2 = Node(89, parent=root)
        level_2_child_1 = Node(45, parent=level_1_child_1)
        level_2_child_2 = Node(50, parent=level_1_child_2)

        for pre, fill, node in RenderTree(root):
            print("%s%s" % (pre, node.name))'''
    
    #Se crea una función
    def input_title(self):
        text_surface = self.base_font.render(self.base, True, (255,255,50))
        self.win.blit(text_surface, (30,10))

    def input_value_and_father(self):
        text_surface = self.base_font.render(self.value, True, (255,255,50))
        self.win.blit(text_surface, (30,50))

        text_surface = self.base_font.render(self.father, True, (255,255,50))
        self.win.blit(text_surface, (550,50))

    def input_information(self):
        self.input_title()
        self.input_nodes()
        input_rect_1 = pygame.Rect(200, 45, 50, 30)
        input_rect_2 = pygame.Rect(720, 45, 80, 30)
        cont = 0

        while not self.terminar:
            for event in pygame.event.get():

                if event.type == pygame.QUIT: 
                    self.terminar = True

                while cont < self.numeros:
                    self.input_value_and_father()
                    pygame.draw.rect(self.win, (255,255,255), input_rect_1, 2)
                    pygame.draw.rect(self.win, (255,255,255), input_rect_2, 2)

                    i = self.input_value(input_rect_1, input_rect_2)
                    j = self.input_father(input_rect_1, input_rect_2)
                    self.draw_node(cont)

                    if j == "Hola" or i == "Hola": 
                        cont = self.numeros

                    self.borrar_info(input_rect_1, input_rect_2, cont)
                    cont += 1

                print(self.nodes)
                print(self.parents)
                print(self.ubicacion)
        
        pygame.quit()
        sys.exit()

    def validar_int(self, numero):
        try:
            conversion = int(numero)
            return conversion
        except:
            return False

    def input_nodes(self):
        r = 0

        while not self.terminar_1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: 
                        self.user_text = self.user_text[:-1]
                        self.win.fill((0,0,0))
                        self.input_title()
                    elif event.key == pygame.K_SPACE:
                        self.terminar_1 = True
                    else:
                        self.user_text += event.unicode
                        r = self.validar_int(self.user_text)

            pygame.draw.rect(self.win, (255,255,255), self.input_rect, 2)
            text_surface = self.base_font.render(self.user_text, True, (0,255,255))
            self.win.blit(text_surface, (350,10))
            pygame.display.flip()

        self.numeros = r
        print(self.numeros)

    def input_value(self, input_rect_1, input_rect_2):
        terminar_value = False
        value = ''

        while not terminar_value:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    terminar_value = True
                    return "Hola"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        terminar_value = True
                    elif event.key == pygame.K_BACKSPACE: 
                        value = value[:-1]
                        self.borrar_info(input_rect_1, input_rect_2)
                    else:
                        value += event.unicode

            text_surface_1 = self.base_font.render(value, True, (0,255,255))
            self.win.blit(text_surface_1, (210,50))
            pygame.display.flip()

        self.ingresar_node(value, input_rect_1, input_rect_2)

    def ingresar_node(self, value, input_rect_1, input_rect_2):
        if value in self.nodes:
            self.borrar_info(input_rect_1, input_rect_2)
            self.input_value(input_rect_1, input_rect_2)
        else: 
            self.nodes.append(value)

    def input_father(self, input_rect_1, input_rect_2):
        terminar_father = False
        father = ''

        while not terminar_father:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    terminar_father = True
                    return "Hola"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        terminar_father = True
                    elif event.key == pygame.K_BACKSPACE: 
                        father = father[:-1]
                        self.borrar_info(input_rect_1, input_rect_2)
                    else:
                        father += event.unicode

            text_surface_2 = self.base_font.render(father, True, (0,255,255))
            self.win.blit(text_surface_2, (730,50))
            pygame.display.flip()

        self.parents.append(father)

    def borrar_info(self, input_rect_1, input_rect_2, cont):
        self.win.fill((0,0,0))
        self.input_title()
        self.input_value_and_father()
        pygame.draw.rect(self.win, (255,255,255), self.input_rect, 2)
        pygame.draw.rect(self.win, (255,255,255), input_rect_1, 2)
        pygame.draw.rect(self.win, (255,255,255), input_rect_2, 2)
        text_surface = self.base_font.render(self.user_text, True, (0,255,255))
        print('A borrar')
        self.draw_nodes_actual()
        self.win.blit(text_surface, (350,10))

    def ubicacion_father(self, value):
        i = 0
        listo = False

        while listo == False and i < len(self.nodes): 
            if self.nodes[i] == value: 
                listo = True
                return self.ubicacion[i]
            i += 1

    def draw_nodes_actual(self):
        for i in range(len(self.nodes)):
            posicion_actual = self.ubicacion[i]
            pygame.draw.circle(self.win, (100,10,255), posicion_actual, 20, 5)

            if self.parents[i] != 'None':
                posicion_inicial = self.ubicacion_father(self.parents[i])
                pygame.draw.line(self.win, (100,0,105), (posicion_inicial[0]-5,posicion_inicial[1]+10), (posicion_actual[0],posicion_actual[1]-10), 4)

            texto = self.nodes[i]
            text_surface = self.base_font.render(texto, True, (0,255,255))
            self.win.blit(text_surface, (posicion_actual[0]-5,posicion_actual[1]-10))
            pygame.display.flip()

    def draw_node(self, actual):
        i = 0
        x = 450
        y = 100

        while i <= actual:
            if self.parents[i] == 'None':
                pygame.draw.circle(self.win, (100,10,255), (x, y), 20, 5)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (x-5,90))
                self.ubicacion.append((x, y))
                self.son_father_draw(self.nodes[i], x, y)
            
            i += 1
            pygame.display.flip()

    def out_range(self):
        text = '---------- NO HAY NODO RAIZ -------------'
        text_surface = self.base_font.render(text, True, (255,0,0))
        self.win.blit(text_surface, (170,self.alto-20))
        pygame.display.flip()

    def son_father_draw(self, value, xinicial, yinicial):
        distancia = 100
        y = yinicial + distancia
        suma = y/100
        x = xinicial - (suma*100)

        for i in range(len(self.parents)):
            
            if value == self.parents[i]:
                posicion = self.insert_posicion(i, x, y)
                pygame.draw.circle(self.win, (100,10,255), posicion, 20, 5)
                pygame.draw.line(self.win, (100,0,105), (xinicial-5,yinicial+10), (posicion[0],posicion[1]-10), 4)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (x-5,y-10))

                self.son_father_draw( self.nodes[i], posicion[0], posicion[1])
                x += ((suma*100)+250)

                pygame.display.flip()

    def son_padre(self, value, xinicial, yinicial):
        y = yinicial+100
        algo_2 = 0
        algo = self.verifica_ubicacion(y)
        x = xinicial
        if algo > 1 :
            x -= (100*algo)
        else: 
            x -= 100

        for i in range(len(self.parents)):

            if value == self.parents[i]:
                print(algo, ' algo ', x, 'nodo', self.nodes[i])

                pygame.draw.circle(self.win, (100,10,255), (x,y), 20, 5)
                self.ubicacion.insert(i, (x, y))

                if len(self.ubicacion) > i+1:
                    self.ubicacion.pop(i+1)

                pygame.draw.line(self.win, (100,0,105), (xinicial-5,yinicial+10), (x,y-10), 4)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (x-5,y-10))
                
                pygame.display.flip()

                self.son_padre(self.nodes[i], x, y) 

                algo_2 = self.verifica_ubicacion_2(y, i)
                if algo_2 > 1 :
                    x += (100*algo_2)
                else: 
                    x += 100

    def verifica_ubicacion(self, y):
        cont = 0
        x = 0

        for i in range(len(self.ubicacion)):
            actual = self.ubicacion[i]
            if actual[1] == y: 
                cont += 1

        if cont > 3: 
            x = (150*cont)
        else: 
            x = 100

        return x

    def insert_posicion(self, i, x, y):
        self.ubicacion.insert(i, (x, y))

        while len(self.ubicacion) > i+1:
            self.ubicacion.pop(i+1)
        
        print(i, 'ki', self.ubicacion[i-1])
        print(self.ubicacion[i])
        return self.ubicacion[i]

    def verifica_ubicacion_2(self, y, actual_index):
        cont = 0
        i = 0

        while i < len(self.ubicacion) and i < actual_index:
            actual = self.ubicacion[i]
            if actual[1] == y: 
                cont += 1
            
            i += 1

        return cont




