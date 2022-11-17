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

                    if j == "Hola" or i == "Hola": 
                        cont = self.numeros

                    cont += 1
                    self.borrar_info(input_rect_1, input_rect_2)

                print(self.nodes)
                print(self.parents)
                self.draw_nodes()
        
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

    def borrar_info(self, input_rect_1, input_rect_2):
        self.win.fill((0,0,0))
        self.input_title()
        self.input_value_and_father()
        pygame.draw.rect(self.win, (255,255,255), self.input_rect, 2)
        pygame.draw.rect(self.win, (255,255,255), input_rect_1, 2)
        pygame.draw.rect(self.win, (255,255,255), input_rect_2, 2)
        text_surface = self.base_font.render(self.user_text, True, (0,255,255))
        self.win.blit(text_surface, (350,10))

    def draw_nodes(self):
        x = 300
        y = 160
        listo = False
        cont = 0
        i = 0

        while not listo:
            if self.parents[i] == 'None':
                pygame.draw.circle(self.win, (100,10,255), (400,100), 20, 5)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (392,90))
                self.son_padre(self.nodes[i], 400, 100)
                listo = True
                cont += 1
            elif cont == 0 and i == len(self.parents)-1:
                cont += 1
                self.out_range()
                listo = True

            i += 1
            pygame.display.flip()

    def out_range(self):
        text = '---------- NO HAY NODO RAIZ -------------'
        text_surface = self.base_font.render(text, True, (255,0,0))
        self.win.blit(text_surface, (170,self.alto-20))
        pygame.display.flip()

    def son_padre(self, value, xinicial, yinicial):
        x = xinicial-100
        y = yinicial+100

        for i in range(len(self.parents)):
            if value == self.parents[i]:
                print(value,'hola', self.parents[i])
                pygame.draw.circle(self.win, (100,10,255), (x,y), 20, 5)
                pygame.draw.line(self.win, (100,0,105), (xinicial-5,yinicial+10), (x,y-10), 4)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (x-5,y-10))
                
                pygame.display.flip()

                self.son_padre(self.nodes[i], x, y)
                x += 100




