import pygame
import sys
import random
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
        self.ancho = 1070
        self.terminar = False
        self.terminar_1 = False
        self.terminar_arbol = False

        #variable creada para guardar la información de la posición
        #en la que estaba la imagen que se está moviendo
        self.posicion_inicial = None

        #Se establecen las inscripciones que tendrán los input para el arbol
        self.base = 'Noodos del arbol: '
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
        self.base2 = 'Árboles'
        self.base3 = 'Grafos'

        #Se crean tres rectangulos para los botones
        self.input_rect1 = pygame.Rect(60, 10, 100, 30)
        self.input_rect2 = pygame.Rect(190, 10, 100, 30)
        self.input_rect3 = pygame.Rect(320, 10, 100, 30)

        #Función para cargar todas las imagenes para el juego
        self.carga_imagenes()

        #Se crean las variables que serán utilizadas para la pila
        self.array = []
        self.array_tam_image = []
        self.mov_mouse_1() 
        self.terminar_pila = False

        #Se crean las variables con la ubicación de cada una de las rectas que corresponden a las diferentes pilas
        self.rect1 = pygame.Rect(20, 200, 95, 166)
        self.rect2 = pygame.Rect(130, 200, 95, 166)
        self.rect3 = pygame.Rect(240, 200, 95, 166)
        self.rect4 = pygame.Rect(350, 200, 95, 166)
        self.rect5 = pygame.Rect(460, 200, 95, 166)
        self.rect6 = pygame.Rect(570, 200, 95, 166)
        self.rect7 = pygame.Rect(680, 200, 95, 166)

        #Se crea el vector que guardará las copias que han sido creadas en el metodo posterior
        self.vector_copy_imagenes = []

        #Se crean unas copias de estas posiciones iniciales de las pilas
        self.crear_copias()

        #Se crean los vectores de cada pila que guardarán las cartas que haya en cada una de ellas
        self.pila1 = []
        self.pila2 = []
        self.pila3 = []
        self.pila3 = []
        self.pila4 = []
        self.pila5 = []
        self.pila6 = []
        self.pila7 = []

        #Se crea la variable que guarda la posición de la carta que será girada
        self.voltear = None

        #variable que indica la pila en la que estaba la carta a la que se le está dando movimiento
        self.mov_pila1 = False
        self.mov_pila2 = False
        self.mov_pila3 = False
        self.mov_pila4 = False
        self.mov_pila5 = False
        self.mov_pila6 = False
        self.mov_pila7 = False

        #Se crean unos contadores para llevar una noción del numero de cartas disponibles en cada pila
        self.cont_pila1 = 3
        self.cont_pila2 = 3
        self.cont_pila3 = 3
        self.cont_pila4 = 3
        self.cont_pila5 = 3
        self.cont_pila6 = 3
        self.cont_pila7 = 3
        
        #variable utilizada para guardar la información de la imagen extraida de las pilas inferiores
        self.tam_image_2 = None
        self.imagen_mov = None

        #Se le da el tipo de letra y el tamaño de la letra que será utilizada para los botones
        self.base_font = pygame.font.Font(None, 32)

        #Se dibuja la ventana con las especificaciones de ancho y alto establecidas 
        # y se le da el color negro 
        self.win = pygame.display.set_mode([self.ancho, self.alto])
        self.win.fill((0,0,0))

    def carga_imagenes(self):
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

        self.Aca = pygame.image.load("Aca.png")
        self.I4ca = pygame.image.load("4ca.png")
        self.I5ca = pygame.image.load("5ca.png")
        self.Ijca = pygame.image.load("Jca.png")
        self.IQca = pygame.image.load("Qca.png")

        self.Ic2 = pygame.image.load("2c.png")
        self.Ic6 = pygame.image.load("6c.png")
        self.Ic7 = pygame.image.load("7c.png")
        self.Ic8 = pygame.image.load("8c.png")
        self.Ic10 = pygame.image.load("10c.png")
        self.IcQ = pygame.image.load("Qc.png")
        self.Ick = pygame.image.load("Kc.png")

        self.imagenes = [self.I4ca, self.IcQ, self.Ic6, self.Ic2, self.Ic7, self.Ic10, self.IQca, self.Ick, self.Ijca, self.I5ca, self.Aca, self.Ic8, self.img9, self.img3]

    #Se crean los cuatro botones que serán utilizados
    def crear_botones(self):
        pygame.draw.rect(self.win, (255,255,255), self.input_rect1)
        pygame.draw.rect(self.win, (255,255,255), self.input_rect2)
        pygame.draw.rect(self.win, (255,255,255), self.input_rect3)

        text_surface = self.base_font.render(self.base1, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect1.x + (self.input_rect1.width - text_surface.get_width()) / 2, (self.input_rect1.y + (self.input_rect1.height - text_surface.get_height())/2)))

        text_surface = self.base_font.render(self.base2, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect2.x + (self.input_rect2.width - text_surface.get_width()) / 2, (self.input_rect2.y + (self.input_rect2.height - text_surface.get_height())/2)))

        text_surface = self.base_font.render(self.base3, True, (0,0,0))
        self.win.blit(text_surface, (self.input_rect3.x + (self.input_rect3.width - text_surface.get_width()) / 2, (self.input_rect3.y + (self.input_rect3.height - text_surface.get_height())/2)))

    #Se crea un metodo que muestre todas las cartas apiladas
    def cartas_apiladas(self, jugando):
        left = 600
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
        self.n_cartas = numero_cartas
        self.crear_botones()
        self.cartas_apiladas(self.n_cartas)
        cont = 0
        cont_cartas = 0
        mov = False

        while not self.terminar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.terminar = True
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 

                    if self.input_rect1.collidepoint(pygame.mouse.get_pos()):
                        self.terminar_pila = False
                        self.win.fill((25,111,61))
                        self.tam_image = self.apiladas(13)
                        cont_cartas = self.control_pila_mouse(cont_cartas)
                        self.win.fill((0,0,0))
                        self.crear_botones()
                        self.cartas_apiladas(numero_cartas)

                    elif self.input_rect2.collidepoint(pygame.mouse.get_pos()):
                        self.terminar_arbol = False
                        self.win.fill((255,255,255))
                        self.input_information()
                        self.win.fill((0,0,0))
                        self.crear_botones()
                        self.cartas_apiladas(numero_cartas)

                    elif self.input_rect3.collidepoint(pygame.mouse.get_pos()):
                        print("Clic Grafos")

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

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
        text_surface = self.base_font.render(self.base, True, (100,30,22))
        self.win.blit(text_surface, (30,10))

    #función que imprima el titulo de los dos input siguientes: 
    #valor del nodo hijo y el valor del padre
    def input_value_and_father(self):
        text_surface = self.base_font.render(self.value, True, (100,30,22))
        self.win.blit(text_surface, (30,50))

        text_surface = self.base_font.render(self.father, True, (100,30,22))
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
                    pygame.draw.rect(self.win, (0,0,0), input_rect_1, 2)
                    pygame.draw.rect(self.win,  (0,0,0), input_rect_2, 2)

                    i = self.input_value(input_rect_1, input_rect_2)
                    j = self.input_father(input_rect_1, input_rect_2)
                    self.draw_nodes()

                    if j == "Hola" or i == "Hola": 
                        cont = self.numeros
                    elif j == True: 
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
                        self.win.fill((255,255,255))
                        self.input_title()
                    elif event.key == pygame.K_SPACE:
                        r = self.validar_int(self.user_text)
                        if r != False:
                            self.terminar_1 = True
                        else: 
                            self.user_text = self.user_text[:-1]
                            self.win.fill((255,255,255))
                            self.input_title()
                    else:
                        self.user_text += event.unicode

            pygame.draw.rect(self.win, (0,0,0), self.input_rect, 2)
            text_surface = self.base_font.render(self.user_text, True, (28,40,51))
            self.win.blit(text_surface, (350,10))
            pygame.display.flip()

        self.numeros = r
        print(self.numeros)

    def validar_nodo_cabeza(self, father):
        padre = father.lower()
        print(padre, 'g', len(self.nodes))

        if len(self.nodes) == 1:
            if padre == "n" or padre == "none":
                self.parents.append(father)
                return True 
            else:
                self.out_range()
                self.nodes = []
                return False
        elif self.parents[0] == 'n' or self.parents[0] == 'none':
            self.parents.append(father)

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

            text_surface_1 = self.base_font.render(value, True, (27,48,49))
            self.win.blit(text_surface_1, (210,50))
            pygame.display.flip()

        self.ingresar_node(value, input_rect_1, input_rect_2)

    #Se verifica que el nuevo noodo que se desea ingresar no esté ya incorporado en la lista
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

            text_surface_2 = self.base_font.render(father, True, (27,48,49))
            self.win.blit(text_surface_2, (730,50))
            pygame.display.flip()

        #self.parents.append(father)
        r = self.validar_nodo_cabeza(father)
        return r

    #Metodo que resetee las cuadriculas de los input de value y padre
    def borrar_info(self, input_rect_1, input_rect_2):
        self.win.fill((255,255,255))
        self.input_title()
        self.input_value_and_father()
        pygame.draw.rect(self.win, (0,0,0), self.input_rect, 2)
        pygame.draw.rect(self.win, (0,0,0), input_rect_1, 2)
        pygame.draw.rect(self.win, (0,0,0), input_rect_2, 2)
        text_surface = self.base_font.render(self.user_text, True, (28,40,51))
        self.win.blit(text_surface, (350,10))
        self.draw_nodes()

    #Metodo que busca y dibuja a la raíz del arbol 
    def draw_nodes(self):
        x = 300
        y = 160
        listo = False
        cont = 0
        i = 0

        while not listo and len(self.nodes) >= 1 and len(self.parents) >= 1:
            if self.parents[i] == 'n' or self.parents[i] == 'none':
                pygame.draw.circle(self.win, (100,10,255), (400,100), 20, 5)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (392,90))
                self.son_padre(self.nodes[i], 400, 100)
                listo = True
                cont += 1
            elif cont == 0 and i == len(self.parents)-1:
                cont += 1
                #self.out_range()
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
        y = yinicial+100
        suma = y/100
        x = xinicial - (suma*50)
        resta = 50

        for i in range(len(self.parents)):
            if value == self.parents[i]:
                print(x,'hola', self.nodes[i])
                if suma > 2:
                    print('hg1')
                    x += 50
                pygame.draw.circle(self.win, (100,10,255), (x,y), 20, 5)
                pygame.draw.line(self.win, (100,0,105), (xinicial-5,yinicial+10), (x,y-10), 4)
                texto = self.nodes[i]
                text_surface = self.base_font.render(texto, True, (0,255,255))
                self.win.blit(text_surface, (x-5,y-10))
                
                pygame.display.flip()

                self.son_padre(self.nodes[i], x, y)
                if suma > 2:
                    print('hg')
                    x -= 80
                    resta += (suma*40)
                x += ((suma*100)+70)-resta

#----------------------------- Pila --------------------------------

    #Se desarrolla un metodo que controle los movimientos del mouse y el teclado una vez que se ha presionado el botón 'pila'
    def control_pila_mouse(self, cont_cartas):
        #Se crean las variables locales que serán utilizadas al dibujar las cartas
        activar = False
        cont = 0
        mov = False
        i = -1
        otros = False
        hola = False
        abajo = False
        carta_pila_superior = None


        #Se inicia in ciclo que abre una interfaz para organizar las cartas de la pila
        #ciclo que termina al darle en la x de la interfaz grafica
        while not self.terminar_pila: 
            if len(self.vector_copy_imagenes) == 0: 
                self.crear_imagenes_pilas()

            for event in pygame.event.get():
                if event.type == pygame.QUIT : self.terminar_pila = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                    
                    hola = self.carta_actual_collision_2()
                    if hola == True: 
                        activar = True
                        hola = False

                    #Se lleva un control de clicks para definir en que momento hacer que acción
                    elif cont == 0 and self.tam_image.collidepoint(pygame.mouse.get_pos()):
                        #self.apiladas(13)
                        activar = True
                        carta = self.imgAtras
                    else: 
                        if cont%2 == 0: 
                            i = self.carta_actual_collision(mov)
                            #Se pregunta si la carta que se desea mover está en la pila o ya salió de ella
                            if i != -1: 
                                activar = True
                                mov = False
                                carta = self.array[i]
                                otros = True
                                print('aja4')
                            else:
                                activar = False
                                mov = False
                                otros = False
                                print('aja3')
                                if abajo: 
                                    mouse_pos = pygame.mouse.get_pos()
                                    self.ingreso_nueva_pila(mouse_pos, self.imagen_mov)
                                    abajo = False
                                else:
                                    print(carta_pila_superior)
                                    mouse_pos = pygame.mouse.get_pos()
                                    self.ingreso_nueva_pila(mouse_pos, carta_pila_superior)
                        else: 
                            #Se llega a esta parte cuando ya se quiere dejar la carta en un lugar 
                            #especifico de la pantalla
                            if self.tam_image.collidepoint(pygame.mouse.get_pos()):
                                self.tam_image = self.imgAtras.get_rect()
                                carta = self.imgAtras
                                activar = True
                                mov = False
                                print('aja')
                    cont += 1

            #Se extrae la posición del mouse
            mouse_pos = pygame.mouse.get_pos()
            if activar == True: 
                #Se posiciona la carta que sigue en la pila, una vez que se ha seleccionado la misma
                if mov == False and self.tam_image.collidepoint(pygame.mouse.get_pos()): 
                    self.win.fill((25,111,61))
                    if not otros:
                        cont_cartas += 1
                        self.tam_image = self.apiladas(13)
                        carta = self.definir_carta(cont_cartas-1)

                        if carta != None:
                            self.win.blit(carta, self.tam_image)

                    mov = True
                elif self.carta_actual_collision_2() and mov == False and self.tam_image_2.collidepoint(pygame.mouse.get_pos()): 
                    print("whatsaap")
                    mov = True
                    abajo = True
                    #self.posicion_inicial = self.imagen_mov.get_rect()
                    self.quitar_carta_mov_pila()
                #Se resetea la pantalla y se le da movimiento con el mouse a la imagen seleccionada
                elif mov == True: 
                    #Se pregunta si es una carta recién sacada de la pila o si ya estaba
                    #haciendo uso de la variable 'otros'
                    if not otros and not abajo:
                        carta_pila_superior = self.mov_true(cont_cartas, mouse_pos)
                        self.tam_image = self.apiladas(13)
                    elif abajo: 
                        self.apiladas(13)
                        self.mov_true_3(cont_cartas, mouse_pos)
                #Se deja la carta en la ulitima posición que tomó mientras se movía
                else:
                    #Se pregunta si es una carta recién sacada de la pila o si ya estaba
                    #haciendo uso de la variable 'otros'
                    if not otros:
                        self.tam_image = self.apiladas(13)
                    else: 
                        self.tam_image = self.imgAtras.get_rect()
                        carta = self.imgAtras
                        self.apiladas(13)
                        print('aja2')
                        otros = False

            self.apiladas(13)
            pygame.display.flip()

        return cont_cartas

    #con este metodo se verifica la posicion del mouse en la pantalla para establecer la pila donde se ingresaría la carta
    def ingreso_nueva_pila(self, mouse_pos, imagen):

        #Se establecen algunos rangos tomando la posición en x (mouse_pos[0]) del mouse y la posicion en y
        #para establecer el rango entre los limites de la pila con un margen de error de aproximadamente 2%
        if mouse_pos[0] >= self.rect1.left-10 and mouse_pos[0] < self.rect1.left+70 and mouse_pos[1] >= self.rect1.top-10:
            #Se verifica si la pila está vacía o no
            if self.cont_pila1 == 0: 
                self.cont_pila1 += 1
                self.pila1.insert(0, imagen)
            #Se verifica que la carta corresponda a la carta siguiente a la que ya está en la pila
            elif self.verificar_continuidad_orden(self.pila1, self.cont_pila1, imagen):
                self.cont_pila1 += 1
                self.pila1.insert(self.cont_pila1 -1, imagen)
            else: 
                print(imagen, self.pila1[self.cont_pila1-1], self.cont_pila1-1)

        elif mouse_pos[0] >= self.rect2.left-10 and mouse_pos[0] < self.rect2.left+70 and mouse_pos[1] >= self.rect2.top-10:
            if self.cont_pila2 == 0: 
                self.cont_pila2 += 1
                self.pila2.insert(0, imagen)
            elif self.verificar_continuidad_orden(self.pila2, self.cont_pila2, imagen):
                self.cont_pila2 += 1
                self.pila2.insert(self.cont_pila2 -1, imagen)
            else: 
                print(imagen, self.pila2[self.cont_pila2-1], self.cont_pila2-1)

        elif mouse_pos[0] >= self.rect3.left-10 and mouse_pos[0] < self.rect3.left+70 and mouse_pos[1] >= self.rect3.top-10 :
            if self.cont_pila3 == 0: 
                self.cont_pila3 += 1
                self.pila3.insert(0, imagen)
            elif self.verificar_continuidad_orden(self.pila3, self.cont_pila3, imagen):
                self.cont_pila3 += 1
                self.pila3.insert(self.cont_pila3 -1, imagen)
            else: 
                print(imagen, self.pila3[self.cont_pila3-1], self.cont_pila3-1)
                print("Te encontre")

        elif mouse_pos[0] >= self.rect4.left-10 and mouse_pos[0] < self.rect4.left+70 and mouse_pos[1] >= self.rect4.top-10 :
            self.cont_pila4 += 1
            self.pila4.insert(self.cont_pila4 -1, imagen)
        elif mouse_pos[0] >= self.rect5.left-10 and mouse_pos[0] < self.rect5.left+70 and mouse_pos[1] >= self.rect5.top-10 :
            self.cont_pila5 += 1
            self.pila5.insert(self.cont_pila5 -1, imagen)
        elif mouse_pos[0] >= self.rect6.left-10 and mouse_pos[0] < self.rect6.left+70 and mouse_pos[1] >= self.rect6.top-10 :
            self.cont_pila6 += 1
            self.pila6.insert(self.cont_pila6 -1, imagen)
        elif mouse_pos[0] >= self.rect7.left-10 and mouse_pos[0] < self.rect7.left+70 and mouse_pos[1] >= self.rect7.top-10:
            self.cont_pila7 += 1
            self.pila7.insert(self.cont_pila7 -1, imagen)

    #Se verifica que la carta que se desea ingresar corresponda a la carta que le sigue a la que ya está en la pila
    def verificar_continuidad_orden(self, pila, posicion, imagen):
        listo = False

        if pila[posicion-1] == self.imgA or pila[posicion-1] == self.Aca: 
            if imagen == self.imgk or imagen == self.Ick: 
                listo = True
            else:
                listo = False
        elif pila[posicion-1] == self.imgk or pila[posicion-1] == self.Ick: 
            if imagen == self.imgq or imagen == self.IQca or imagen == self.IcQ: 
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.imgq or  pila[posicion-1] == self.IQca or  pila[posicion-1] == self.IcQ: 
            if imagen == self.imgj or imagen == self.Ijca:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.imgj or pila[posicion-1] == self.Ijca: 
            if imagen == self.img10 or imagen == self.Ic10:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img10 or pila[posicion-1] == self.Ic10: 
            if imagen == self.img9:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img9: 
            if imagen == self.img8 or imagen == self.Ic8:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img8 or pila[posicion-1] == self.Ic8: 
            if imagen == self.img7 or imagen == self.Ic7:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img7 or pila[posicion-1] == self.Ic7: 
            if imagen == self.img6 or imagen == self.Ic6:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img6 or pila[posicion-1] == self.Ic6: 
            if imagen == self.img5 or imagen == self.I5ca:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img5 or pila[posicion-1] == self.I5ca: 
            if imagen == self.img4 or imagen == self.I4ca:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img4 or pila[posicion-1] == self.I4ca: 
            if imagen == self.img3:
                listo = True
            else:
                listo = False
        elif  pila[posicion-1] == self.img3: 
            if imagen == self.img2 or imagen == self.Ic2:
                listo = True
            else:
                listo = False

        return listo

    #Se ingresa la imagen en la ultima posición de la pila
    def confirmar_ingreso_pila(self, imagen):
        if self.voltear.left == self.copy_rect2.left and self.pila2[self.cont_pila2-1] == self.imgAtras:
            self.pila2[self.cont_pila2-1] = imagen
        elif self.voltear.left == self.copy_rect3.left and self.pila3[self.cont_pila3-1] == self.imgAtras:
            self.pila3[self.cont_pila3-1] = imagen
        elif self.voltear.left == self.copy_rect4.left and self.pila4[self.cont_pila4-1] == self.imgAtras:
            self.pila4[self.cont_pila4-1] = imagen
        elif self.voltear.left == self.copy_rect5.left and self.pila5[self.cont_pila5-1] == self.imgAtras:
            self.pila5[self.cont_pila5-1] = imagen
        elif self.voltear.left == self.copy_rect6.left and self.pila6[self.cont_pila6-1] == self.imgAtras:
            self.pila6[self.cont_pila6-1] = imagen
        elif self.voltear.left == self.copy_rect7.left and self.pila7[self.cont_pila7-1] == self.imgAtras:
            self.pila7[self.cont_pila7-1] = imagen
        elif self.voltear.left == self.copy_rect1.left and self.pila1[self.cont_pila1-1] == self.imgAtras:
            self.pila1[self.cont_pila1-1] = imagen

    #Con este metodo se 'crea' la pila
    def mov_mouse_1(self):
        self.array = [self.imgA, self.imgk, self.imgq, self.imgj, self.img10, self.img9, self.img8, self.img7, self.img6, self.img5, self.img4, self.img3, self.img2]
        self.array_tam_image = [self.imgA.get_rect(), self.imgk.get_rect(), self.imgq.get_rect(), self.imgj.get_rect(), 
                            self.img10. get_rect(), self.img9.get_rect(), self.img8.get_rect(), self.img7.get_rect(), 
                            self.img6.get_rect(), self.img5.get_rect(), self.img4.get_rect(), self.img3.get_rect(), self.img2.get_rect()]
        self.tam_image = self.imgAtras.get_rect()
        print('listo')

    #Se verifica que cartas ya han sido sacadas del monto y se han intriducido al juego
    #esto para dibujarlas de nuevo cada que la pantalla sea 'reseteada'
    '''def verificar_cartas_dibujadas(self, cont):
        if cont <= 13:
            for i in range(0, cont):
                tam_image = self.array_tam_image[i]
                self.win.blit(self.array[i], tam_image)'''

    #Se define la carta que sigue en la extracción de las mismas del monto
    def definir_carta(self, cont):
        carta = None

        if cont < 13 and cont >= 0:
            carta = self.array[cont]
        return carta 

    #Metodo creado para que las imagenes una vez que son sacadas del monto
    #se muevan junto al mouse, mientras se re-dibuja la pantalla 
    def mov_true(self, cont_cartas, mouse_pos):
        self.win.fill((25,111,61))
        carta = self.definir_carta(cont_cartas-1)
        
        #se le da la posición del mouse a la imagen 
        tam_image_1 = carta.get_rect()
        tam_image_1.left = mouse_pos[0]
        tam_image_1.top = mouse_pos[1]
        
        #se modifica la posición de esa carta en el vector 
        #que guarda las posiciones de cada carta
        self.array_tam_image[cont_cartas-1] = tam_image_1
        self.win.blit(carta, tam_image_1)

        return carta

    #Metodo creado para que las imagenes que sean seleccionadas y que ya han sido extraidas del monto
    #puedan moverse con el mouse, mientras se re-dibuja la pantalla 
    '''def mov_true_2(self, cont_cartas, i, mouse_pos):
        self.win.fill((25,111,61))
        self.verificar_cartas_dibujadas(cont_cartas-1)

        tam_image_1 = self.array[i].get_rect()
        tam_image_1.left = mouse_pos[0]
        tam_image_1.top = mouse_pos[1]
        
        self.array_tam_image[i] = tam_image_1
        self.win.blit(self.array[i], tam_image_1)'''

    #Metodo creado para que la imagen que sea seleccionada de las 7 pilas de abajo
    #pueda moverse con el mouse, mientras se re-dibuja la pantalla 
    def mov_true_3(self, cont_cartas, mouse_pos):
        self.win.fill((25,111,61))

        tam_image_1 = self.imagen_mov.get_rect()
        tam_image_1.left = mouse_pos[0]
        tam_image_1.top = mouse_pos[1]
        
        self.win.blit(self.imagen_mov, tam_image_1)

    #Se le resta una unidad a la variable que cuenta la cantidad de cartas que hay en cada pila
    #esto cada vez que se retire una carta de la pila
    def quitar_carta_mov_pila(self): 
        if self.mov_pila1 == True: 
            self.cont_pila1 -= 1
        elif self.mov_pila2 == True: 
            self.cont_pila2 -= 1
        elif self.mov_pila3 == True: 
            self.cont_pila3 -= 1
        elif self.mov_pila4 == True: 
            self.cont_pila4 -= 1
        elif self.mov_pila5 == True: 
            self.cont_pila5 -= 1
        elif self.mov_pila6 == True: 
            self.cont_pila6 -= 1
        elif self.mov_pila7 == True: 
            self.cont_pila7 -= 1

        self.confirmar_identidad_mov_carta()
        self.crear_imagenes_pilas()

    #Se le da a la variable self.iamgen_mov la equivalencia de la carta que se esté moviendo en el momento
    #De las pilas de abajo
    def confirmar_identidad_mov_carta(self):
        if self.mov_pila1 == True: 
            self.imagen_mov = self.pila1[self.cont_pila1]
        elif self.mov_pila2 == True: 
            self.imagen_mov = self.pila2[self.cont_pila2]
        elif self.mov_pila3 == True: 
            self.imagen_mov = self.pila3[self.cont_pila3]
        elif self.mov_pila4 == True: 
            self.imagen_mov = self.pila4[self.cont_pila4]
        elif self.mov_pila5 == True: 
            self.imagen_mov = self.pila5[self.cont_pila5]
        elif self.mov_pila6 == True: 
            self.imagen_mov = self.pila6[self.cont_pila6]
        elif self.mov_pila7 == True: 
            self.imagen_mov = self.pila7[self.cont_pila7]

    #Se dibuja el monto de cartas en una esquina de la pantalla, pero solo para la interfaz de pila
    #también se ilustran los rectangulos de la parte superior de la pantalla
    def apiladas(self, numero):
        left = 20
        top = 10
        tam_image_1 = None
        grey = (213,219,219)

        r1 = pygame.Rect(350, 10, 95, 166)
        r2 = pygame.Rect(470 , 10, 95, 166)
        r3 = pygame.Rect(570, 10, 95, 166)
        r4 = pygame.Rect(680, 10, 95, 166)

        pygame.draw.rect(self.win, grey, r1, 4, 5)
        pygame.draw.rect(self.win, grey, r2, 4, 5)
        pygame.draw.rect(self.win, grey, r3, 4, 5)
        pygame.draw.rect(self.win, grey, r4, 4, 5)
        self.apiladas_abajo_juego()
        self.crear_copias()

        for i in range(0, numero+1):
            tam_image_1 = self.imgAtras.get_rect()
            tam_image_1.left = left         
            tam_image_1.top = top

            self.win.blit(self.imgAtras, tam_image_1)

        return tam_image_1

    #Con este metodo se llaman todos los metodos que organizan a las diferentes pilas
    def apiladas_abajo_juego(self):
        #Se crea la variable que contendrá la posición de la última carta disponible en cada pila
        self.cartas_abajo_apiladas = []

        self.organizar_pila_1()
        self.organizar_pila_2()
        self.organizar_pila_3()
        self.organizar_pila_4()
        self.organizar_pila_5()
        self.organizar_pila_6()
        self.organizar_pila_7()

    #Dibuja las cartas que estan en la pil 1 a en el rango que se estable con la variable self.cont_pila1
    #variable que aumenta o disminuye cada que se saque o inserte una carta a la pila
    def organizar_pila_1(self):
        top = self.copy_rect1.top

        #Se verifica que la variable sea positiva y que en la pila todavia hayan cartas
        if self.cont_pila1 > 0:
            #Se recorre la lista que tiene las cartas de la pila, desde 0 hasta el número que la variable nos diga
            for i in range(0, self.cont_pila1): 
                tam_image_1 = self.copy_rect1
                tam_image_1.top = top
                top += 20
                
                #Se pregunta si estamos en la ultima posicion de la lista para agregar la ubicacion 
                #en una lista que después nos permitirá conocer la ubicación de la carta a la que se 
                #le puede dar movimiento con el mouse
                if i == self.cont_pila1-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect1)

                #Se pregunta si la lista ya ha sido llenada
                if len(self.pila1) > i:
                    #en caso de que así sea, se pregunta cual es la carta que está 
                    #y se procede a dibujarla
                    if self.pila1[i] != self.imgAtras:
                        self.win.blit(self.pila1[i], tam_image_1)
                    #en el caso contrario se muestra una imagen que muestra la parte trasera de las cartas
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                #en caso de que le lista no haya sido llenada, se le agrega la imagen que muestra la parte trasera de las cartas
                else:
                    self.pila1.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

            #Se hace una pequeña verificación para eliminar de la pila las cartas que ya han sido sacadas 
            #esto preguntando si el tamaño de la pila es igual al de la variable global que nos lleva una cuenta 
            #de las cartas con las que disponemos en la pila
            i = self.cont_pila1
            while len(self.pila1) > i: 
                self.pila1.pop(i)
                i += 1

    #Dibuja las cartas que estan en la pila 2 en el rango que se estable con la variable self.cont_pila2
    #variable que aumenta o disminuye cada que se saque o inserte una carta a la pila
    def organizar_pila_2(self):
        top = self.copy_rect2.top

        if self.cont_pila2 > 0:
            for i in range(0, self.cont_pila2): 
                tam_image_1 = self.copy_rect2
                tam_image_1.top = top
                top += 20
                
                if i == self.cont_pila2-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect2)

                if len(self.pila2) > i:
                    if self.pila2[i] != self.imgAtras:
                        self.win.blit(self.pila2[i], tam_image_1)
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                else:
                    self.pila2.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

    #Dibuja las cartas que estan en la pila 3 en el rango que se estable con la variable self.cont_pila3
    def organizar_pila_3(self):
        top = self.copy_rect3.top

        if self.cont_pila3 > 0:
            for i in range(0, self.cont_pila3): 
                tam_image_1 = self.copy_rect3
                tam_image_1.top = top
                top += 20
                
                if i == self.cont_pila3-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect3)

                if len(self.pila3) > i:
                    if self.pila3[i] != self.imgAtras:
                        self.win.blit(self.pila3[i], tam_image_1)
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                else:
                    self.pila3.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

    #Dibuja las cartas que estan en la pila 4 en el rango que se estable con la variable self.cont_pila4
    def organizar_pila_4(self):
        top = self.copy_rect4.top

        if self.cont_pila4 > 0:
            for i in range(0, self.cont_pila4): 
                tam_image_1 = self.copy_rect4
                tam_image_1.top = top
                top += 20
                
                if i == self.cont_pila4-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect4)

                if len(self.pila4) > i:
                    if self.pila4[i] != self.imgAtras:
                        self.win.blit(self.pila4[i], tam_image_1)
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                else:
                    self.pila4.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

    #Dibuja las cartas que estan en la pila 5 en el rango que se estable con la variable self.cont_pila5
    def organizar_pila_5(self):
        top = self.copy_rect5.top

        if self.cont_pila5 > 0:
            for i in range(0, self.cont_pila5): 
                tam_image_1 = self.copy_rect5
                tam_image_1.top = top
                top += 20
                
                if i == self.cont_pila5-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect5)

                if len(self.pila5) > i:
                    if self.pila5[i] != self.imgAtras:
                        self.win.blit(self.pila5[i], tam_image_1)
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                else:
                    self.pila5.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

    #Dibuja las cartas que estan en la pila 6 en el rango que se estable con la variable self.cont_pila6
    def organizar_pila_6(self):
        top = self.copy_rect6.top

        if self.cont_pila6 > 0:
            for i in range(0, self.cont_pila6): 
                tam_image_1 = self.copy_rect6
                tam_image_1.top = top
                top += 20
                
                if i == self.cont_pila6-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect6)

                if len(self.pila6) > i:
                    if self.pila6[i] != self.imgAtras:
                        self.win.blit(self.pila6[i], tam_image_1)
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                else:
                    self.pila6.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

    #Dibuja las cartas que estan en la pila 7 en el rango que se estable con la variable self.cont_pila7
    def organizar_pila_7(self):
        top = self.copy_rect7.top

        if self.cont_pila7 > 0:
            for i in range(0, self.cont_pila7): 
                tam_image_1 = self.copy_rect7
                tam_image_1.top = top
                top += 20
                
                if i == self.cont_pila7-1:
                    self.cartas_abajo_apiladas.append(self.copy_rect7)

                if len(self.pila7) > i:
                    if self.pila7[i] != self.imgAtras:
                        self.win.blit(self.pila7[i], tam_image_1)
                    else:
                        self.win.blit(self.imgAtras, tam_image_1)
                else:
                    self.pila7.append(self.imgAtras)
                    self.win.blit(self.imgAtras, tam_image_1)

    def crear_copias(self):
        self.copy_rect1 = pygame.Rect(20, 200, 95, 166)
        self.copy_rect2 = pygame.Rect(130, 200, 95, 166)
        self.copy_rect3 = pygame.Rect(240, 200, 95, 166)
        self.copy_rect4 = pygame.Rect(350, 200, 95, 166)
        self.copy_rect5 = pygame.Rect(460, 200, 95, 166)
        self.copy_rect6 = pygame.Rect(570, 200, 95, 166)
        self.copy_rect7 = pygame.Rect(680, 200, 95, 166)

        self.vector_copy = [self.copy_rect1, self.copy_rect2, self.copy_rect3, self.copy_rect4, self.copy_rect5, self.copy_rect6, self.copy_rect7]

    def crear_imagenes_pilas(self):
        self.crear_copias()

        for i in range(0, len(self.vector_copy)): 
            actual = self.vector_copy[i]
            numero = random.randrange(0, len(self.imagenes)-1)
            imag = self.imagenes[numero]
            self.vector_copy_imagenes.append(imag)
            self.voltear = actual
            self.confirmar_ingreso_pila(imag)

    #retorna la pisición (en la pila) en donde está la carta que ha sido seleccionada
    def carta_actual_collision(self, mov):
        listo = False
        i = 0

        #Se verifica que la carta que se desee mover no esté en el monto
        if mov is False:
            #se recorre la pila hasta que se encuentre o 'i' pase su tamaño
            while not listo and  i < len(self.array):
                tam_imagen = self.array_tam_image[i]
                if tam_imagen.collidepoint(pygame.mouse.get_pos()):
                    self.tam_image = self.array_tam_image[i]
                    listo = True
                i += 1

        return i-1

    #Se verifica la colision del mouse con una de las cartas de las 7 pilas de la parte baja
    def carta_actual_collision_2(self):
        listo = False
        i = 0

        #se recorre la lista que tiene un registro de las ultima carta que se encuentra en cada pila
        while not listo and  i < len(self.cartas_abajo_apiladas):
            tam_imagen = self.cartas_abajo_apiladas[i]

            #se verifica que la carta que la carta actual haya sido clickponeada 
            #y de ser el caso se identifica la pila en la que se encuentra la carta
            #para llamar a una función que diga que todas las demas pilas no son
            if tam_imagen.collidepoint(pygame.mouse.get_pos()):
                if tam_imagen.left == self.rect1.left:
                    self.mov_pila1 = True
                    self.imagen_mov_pila1()
                elif tam_imagen.left == self.rect2.left:
                    self.mov_pila2 = True
                    self.imagen_mov_pila2()
                elif tam_imagen.left == self.rect3.left:
                    self.mov_pila3 = True
                    self.imagen_mov_pila3()
                elif tam_imagen.left == self.rect4.left:
                    self.mov_pila4 = True
                    self.imagen_mov_pila4()
                elif tam_imagen.left == self.rect5.left:
                    self.mov_pila5 = True
                    self.imagen_mov_pila5()
                elif tam_imagen.left == self.rect6.left:
                    self.mov_pila6 = True
                    self.imagen_mov_pila6()
                elif tam_imagen.left == self.rect7.left:
                    self.mov_pila7 = True
                    self.imagen_mov_pila7()

                #Se estable la ubicación de la carta tocada, ingresando esta en la variable global
                self.tam_image_2 = self.cartas_abajo_apiladas[i]
                #Se le notifica al ciclo que ya ha sido encontrada la carta para que se suspenda y deje de buscar
                listo = True
            i += 1

        return listo

    def imagen_mov_pila1(self):
        self.mov_pila2 = False
        self.mov_pila3 = False
        self.mov_pila4 = False
        self.mov_pila5 = False
        self.mov_pila6 = False
        self.mov_pila7 = False
    
    def imagen_mov_pila2(self):
        self.mov_pila1 = False
        self.mov_pila3 = False
        self.mov_pila4 = False
        self.mov_pila5 = False
        self.mov_pila6 = False
        self.mov_pila7 = False

    def imagen_mov_pila3(self):
        self.mov_pila1 = False
        self.mov_pila2 = False
        self.mov_pila4 = False
        self.mov_pila5 = False
        self.mov_pila6 = False
        self.mov_pila7 = False

    def imagen_mov_pila4(self):
        self.mov_pila1 = False
        self.mov_pila2 = False
        self.mov_pila3 = False
        self.mov_pila5 = False
        self.mov_pila6 = False
        self.mov_pila7 = False

    def imagen_mov_pila5(self):
        self.mov_pila1 = False
        self.mov_pila2 = False
        self.mov_pila4 = False
        self.mov_pila3 = False
        self.mov_pila6 = False
        self.mov_pila7 = False

    def imagen_mov_pila6(self):
        self.mov_pila1 = False
        self.mov_pila2 = False
        self.mov_pila4 = False
        self.mov_pila3 = False
        self.mov_pila5 = False
        self.mov_pila7 = False

    def imagen_mov_pila7(self):
        self.mov_pila1 = False
        self.mov_pila2 = False
        self.mov_pila4 = False
        self.mov_pila3 = False
        self.mov_pila5 = False
        self.mov_pila6 = False