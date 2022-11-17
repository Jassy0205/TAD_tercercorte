import pygame
import sys
from Taller03_corte03 import arbol

class barajas():
    #Se crea la clase nodo
    class _Nodo:
        #Se hace el metodo incializador de la clase nodo
        def __init__(self, valor):
            self.valor = valor
            self.nodo_siguiente = None

    #Se hace el metodo incializador de la clase barajas
    def __init__(self):
        pygame.init()

        self.n_cartas = 0

        self.cabeza = None
        self.cola = None
        self.tamaño = 0

        self.alto = 500
        self.ancho = 990
        self.terminar = False
        self.terminar_1 = False
        self.terminar_arbol = False

        #Se establecen las inscripciones que tendrán los input para los arboles
        self.base = 'Cantidad de nodos del arbol: '
        self.value = 'Valor del nodo: '
        self.father = 'Valor del padre: '
        self.input_rect = pygame.Rect(346, 5, 100, 30)

        #Se crean las variables que serán utilizadas para el arbol
        self.user_text = ''
        self.numeros = 0
        self.nodes = []
        self.parents = []

        #Se establecen la inscripción que tendrán los botones
        self.base1 = 'Pilas'
        self.base2 = 'Colas'
        self.base3 = 'Árboles'
        self.base4 = 'Grafos'

        #Se crean tres rectangulos para los botones
        self.input_rect1 = pygame.Rect(30, 10, 100, 30)
        self.input_rect2 = pygame.Rect(160, 10, 100, 30)
        self.input_rect3 = pygame.Rect(290, 10, 100, 30)
        self.input_rect4 = pygame.Rect(420, 10, 100, 30)

        #Se instancian a cada una de las imagenes
        self.imgA = pygame.image.load("a.jpg")
        self.img2 = pygame.image.load("2mod.jpg")
        self.img3 = pygame.image.load("3.jpg")
        self.img4 = pygame.image.load("4mod.jpg")
        self.img5 = pygame.image.load("5mod.jpg")
        self.img6 = pygame.image.load("6mod.jpg")
        self.img7 = pygame.image.load("7mod.jpg")
        self.img8 = pygame.image.load("8mod.jpg")
        self.img9 = pygame.image.load("9mod.jpg")
        self.img10 = pygame.image.load("10mod.jpg")
        self.imgj = pygame.image.load("jmod.jpg")
        self.imgq = pygame.image.load("qmod.jpg")
        self.imgk = pygame.image.load("kmod.jpg")
        self.imgAtras = pygame.image.load("atrasmod.jpg")

        #Se le da el tipo de letra y el tamaño de la letra que será utilizada para los botones
        self.base_font = pygame.font.Font(None, 32)

        #Se dibuja la ventana con las especificaciones de ancho y alto establecidas 
        # y se le da el color negro 
        self.win = pygame.display.set_mode((self.ancho, self.alto))
        self.win.fill((0,0,0))

    #Se crean los cuatro botones que serán utilizados
    def crear_botones(self):
        pygame.draw.rect(self.win, (255,255,255), self.input_rect1)
        pygame.draw.rect(self.win, (255,255,255), self.input_rect2)
        pygame.draw.rect(self.win, (255,255,255), self.input_rect3)
        pygame.draw.rect(self.win, (255,255,255), self.input_rect4)

        text_surface = self.base_font.render(self.base1, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect1.x + (self.input_rect1.width - text_surface.get_width()) / 2, (self.input_rect1.y + (self.input_rect1.height - text_surface.get_height())/2)))

        text_surface = self.base_font.render(self.base2, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect2.x + (self.input_rect2.width - text_surface.get_width()) / 2, (self.input_rect2.y + (self.input_rect2.height - text_surface.get_height())/2)))

        text_surface = self.base_font.render(self.base3, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect3.x + (self.input_rect3.width - text_surface.get_width()) / 2, (self.input_rect3.y + (self.input_rect3.height - text_surface.get_height())/2)))

        text_surface = self.base_font.render(self.base4, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect4.x + (self.input_rect4.width - text_surface.get_width()) / 2, (self.input_rect4.y + (self.input_rect4.height - text_surface.get_height())/2)))

    #Se crea un metodo que muestre todas las cartas apiladas
    def cartas_apiladas(self, jugando):
        left = 800
        top = 10

        for i in range(0, jugando):
            tam_image = self.imgAtras.get_rect()
            tam_image.left = left         
            tam_image.top = top
            left += 3

            self.win.blit(self.imgAtras, tam_image)

    #Metodo para agregar nodos a la pila
    def enqueue(self, valor):
        # Agrega un elemento al final de la queue
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1

    #Agrega todas las cartas a la cola
    def crear_cola(self):
        self.enqueue(self.imgA)
        self.n_cartas -= 1

        self.enqueue(self.imgk)
        self.n_cartas -= 1

        self.enqueue(self.imgq)
        self.n_cartas -= 1

        self.enqueue(self.imgj)
        self.n_cartas -= 1

        self.enqueue(self.img10)
        self.n_cartas -= 1

        self.enqueue(self.img9)
        self.n_cartas -= 1

        self.enqueue(self.img8)
        self.n_cartas -= 1

        self.enqueue(self.img7)
        self.n_cartas -= 1

        self.enqueue(self.img6)
        self.n_cartas -= 1

        self.enqueue(self.img5)
        self.n_cartas -= 1

        self.enqueue(self.img4)
        self.n_cartas -= 1

        self.enqueue(self.img3)
        self.n_cartas -= 1

        self.enqueue(self.img2)
        self.n_cartas -= 1

    #Metodo que convierte la pila en un array 
    def mostrar_cola1(self, n_cartas):
        # Muestra los elementos de la queue
        array = []
        nodo_actual = self.cabeza
        cont = 0

        while nodo_actual != None and cont < n_cartas:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
            cont+=1

        return array

    def stack(self, valor):
        # Agrega un elemento al principio de la Stack
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    #Metodo que agrega todas las cartas a la pila
    def crear_pila(self):
        self.stack(self.imgA)
        self.n_cartas -= 1

        self.stack(self.imgk)
        self.n_cartas -= 1

        self.stack(self.imgq)
        self.n_cartas -= 1

        self.stack(self.imgj)
        self.n_cartas -= 1

        self.stack(self.img10)
        self.n_cartas -= 1

        self.stack(self.img9)
        self.n_cartas -= 1

        self.stack(self.img8)
        self.n_cartas -= 1

        self.stack(self.img7)
        self.n_cartas -= 1

        self.stack(self.img6)
        self.n_cartas -= 1

        self.stack(self.img5)
        self.n_cartas -= 1

        self.stack(self.img4)
        self.n_cartas -= 1

        self.stack(self.img3)
        self.n_cartas -= 1

        self.stack(self.img2)
        self.n_cartas -= 1

    #Metodo que muestra todos los nodos de la cola
    def mostrar_cola_4filas(self, array, pila):
        top = 60
        espaciado = 310

        left1 = self.ancho - 450
        refl = left1
        reft = 0
        cont = 0

        for i in range(0, len(array)):
            if i == len(array)-1:
                tam_image = array[i].get_rect()
                tam_image.left = (refl+espaciado)+26       
                tam_image.top = reft+36
            else: 
                if i == (len(array)-4)-1:
                    left1 -= 36

                reft = top
                if cont < 3: 
                    tam_image = array[i].get_rect()
                    tam_image.left = left1         
                    tam_image.top = top

                    top += 36
                    left1 += 26
                    cont += 1
                elif cont == 3: 
                    tam_image = array[i].get_rect()
                    tam_image.left = left1         
                    tam_image.top = top

                    left1 = refl-espaciado
                    top = 60
                    cont = 0

                refl = left1

            self.win.blit(array[i], tam_image)

    #Se crea un metodo para mostrar los nodos de la pila
    def mostrar_pila_4filas(self, array, pila):
        top = 60
        espaciado = 310

        left1 = self.ancho - 450
        refl = left1
        reft = 0
        cont = 0

        for i in range(len(array)-1, -1, -1):
            if i == 0:
                tam_image = array[i].get_rect()
                tam_image.left = (refl+espaciado)+(26)   
                tam_image.top = reft+36
            else: 
                if i == (0+4):
                    left1 -= 36

                reft = top
                if cont < 3: 
                    tam_image = array[i].get_rect()
                    tam_image.left = left1         
                    tam_image.top = top

                    top += 36
                    left1 += 26
                    cont += 1
                elif cont == 3: 
                    tam_image = array[i].get_rect()
                    tam_image.left = left1         
                    tam_image.top = top

                    left1 = refl-espaciado
                    top = 60
                    cont = 0

                refl = left1

            self.win.blit(array[i], tam_image)

    #Se crea un metodo que cree los botones, y realice las funciones según el botón que sea seleccionado
    def jugar_cartas(self, numero_cartas):
        #self.input_title()
        self.n_cartas = numero_cartas
        self.crear_botones()
        self.cartas_apiladas(self.n_cartas)
        cont_cola = 0
        cont_pila = 0
        tam_cola = []
        tam_pila = []
        btn_pila = False
        btn_cola = False

        while not self.terminar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.terminar = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 

                    if self.input_rect1.collidepoint(pygame.mouse.get_pos()):
                        btn_pila = True
                        if btn_cola is False:
                            tam_pila = self.proceso_pila(cont_pila, tam_pila, btn_cola, numero_cartas)
                        else: 
                            tam_pila = self.proceso_pila(cont_pila, tam_cola, btn_cola,numero_cartas)
                        cont_pila += 1

                    elif self.input_rect2.collidepoint(pygame.mouse.get_pos()):
                        '''btn_cola = True
                        if btn_pila is False:
                            tam_cola = self.proceso_cola(cont_cola, tam_cola, btn_pila)
                        else: 
                            tam_cola = self.proceso_cola(cont_cola, tam_pila, btn_pila)
                        cont_cola += 1'''
                        print("click cola")

                    elif self.input_rect3.collidepoint(pygame.mouse.get_pos()):
                        self.win.fill((0,0,0))
                        self.input_information()
                        self.win.fill((0,0,0))
                        self.crear_botones()
                        self.cartas_apiladas(numero_cartas)

                    elif self.input_rect4.collidepoint(pygame.mouse.get_pos()):
                        print("Clic Grafos")

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

    #Se crea un metodo que muestre haga todo el procedo de crear la cola, y mostrarla
    def proceso_cola(self, cont_cola, tam_cola, btn_pila, n_cartas):
        self.win.fill((0,0,0))
        if cont_cola == 0:
            self.crear_cola()
            self.crear_botones()
            self.cartas_apiladas(self.n_cartas)
            if btn_pila is False:
                tam_cola = self.mostrar_cola1(n_cartas)
            self.mostrar_cola_4filas(tam_cola, False)
        else: 
            if cont_cola%2 == 0: 
                self.crear_botones()
                self.mostrar_cola_4filas(tam_cola, False)
            else: 
                self.crear_botones()
                self.cartas_apiladas(13)
        
        return tam_cola

    #Se crea un metodo que muestre haga todo el procedo de crear la pila, y mostrarla
    def proceso_pila(self, cont_pila, tam_pila, btn_cola, n_cartas):
        self.win.fill((0,0,0))
        if cont_pila == 0:
            self.crear_pila()
            self.crear_botones()
            self.cartas_apiladas(self.n_cartas)
            if btn_cola == False: 
                tam_pila = self.mostrar_cola1(n_cartas)
            self.mostrar_pila_4filas(tam_pila, True)
        else: 
            if cont_pila%2 == 0: 
                self.crear_botones()
                self.mostrar_pila_4filas(tam_pila, True)
            else: 
                self.crear_botones()
                self.cartas_apiladas(13)
        cont_pila += 1

        return tam_pila


    #-------------------------------- Arbol -------------------------------

    #Se crea una función que imprima el titulo del primer input: El número de nodos a dibujar
    def input_title(self):
        text_surface = self.base_font.render(self.base, True, (255,255,50))
        self.win.blit(text_surface, (30,10))

    #función que imprima el titulo de los dos input siguientes: 
    #valor del nodo hijo y el valor del padre
    def input_value_and_father(self):
        text_surface = self.base_font.render(self.value, True, (255,255,50))
        self.win.blit(text_surface, (30,50))

        text_surface = self.base_font.render(self.father, True, (255,255,50))
        self.win.blit(text_surface, (550,50))

    #Función que acciona todo el proceso del arbol
    def input_information(self):
        self.input_title()
        self.input_nodes()
        input_rect_1 = pygame.Rect(200, 45, 50, 30)
        input_rect_2 = pygame.Rect(720, 45, 80, 30)
        cont = 0

        while not self.terminar_arbol:
            for event in pygame.event.get():

                if event.type == pygame.QUIT: 
                    self.terminar_arbol = True

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

    #Se crea un metodo que valide que el dato ingresado corresponda a un valor entero
    def validar_int(self, numero):
        try:
            conversion = int(numero)
            return conversion
        except:
            return False

    #Metodo que reciba la información del input del número de nodos
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

    #Metodo que reciba la información del input del valor del nodo a ingresar
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

    #Se verifique que el nuevo noodo que se desea ingresar no esté ya incorporado en la lista
    def ingresar_node(self, value, input_rect_1, input_rect_2):
        if value in self.nodes:
            self.borrar_info(input_rect_1, input_rect_2)
            self.input_value(input_rect_1, input_rect_2)
        else: 
            self.nodes.append(value)

    #Metodo que reciba la información del input del valor del nodo padre
    # del nuevo nodo a ingresar
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

    #Metodo que resetee las cuadriculas de los input de value y padre
    def borrar_info(self, input_rect_1, input_rect_2):
        self.win.fill((0,0,0))
        self.input_title()
        self.input_value_and_father()
        pygame.draw.rect(self.win, (255,255,255), self.input_rect, 2)
        pygame.draw.rect(self.win, (255,255,255), input_rect_1, 2)
        pygame.draw.rect(self.win, (255,255,255), input_rect_2, 2)
        text_surface = self.base_font.render(self.user_text, True, (0,255,255))
        self.win.blit(text_surface, (350,10))

    #Metodo que busca y dibuja a la raíz del arbol 
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

    #Imprime un mensaje en la interfaz grafica si no se ingresa un nodo "raíz" al arbol
    def out_range(self):
        text = '---------- NO HAY NODO RAIZ -------------'
        text_surface = self.base_font.render(text, True, (255,0,0))
        self.win.blit(text_surface, (150,self.alto-20))
        pygame.display.flip()

    #Metodo que dibuja los circulos para representar los nodos graficamente 
    # y las lineas que representan los enlaces entre los nodos
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

    