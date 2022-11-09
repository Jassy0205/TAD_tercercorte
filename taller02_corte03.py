import pygame
import sys 

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
    def mostrar_cola1(self):
        # Muestra los elementos de la queue
        array = []
        nodo_actual = self.cabeza

        while nodo_actual != None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente

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

    #Metodo que muestra todos los nodos de la pila
    def mostrar_cola_4filas(self, array):
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

        while not self.terminar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.terminar = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 

                    if self.input_rect1.collidepoint(pygame.mouse.get_pos()):
                        tam_pila = self.proceso_pila(cont_pila, tam_pila)
                        cont_pila += 1

                    elif self.input_rect2.collidepoint(pygame.mouse.get_pos()):
                        tam_cola = self.proceso_cola(cont_cola, tam_cola)
                        cont_cola += 1

                    elif self.input_rect3.collidepoint(pygame.mouse.get_pos()):
                        print("Clic Arboles")

                    elif self.input_rect4.collidepoint(pygame.mouse.get_pos()):
                        print("Clic Grafos")

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

    #Se crea un metodo que muestre haga todo el procedo de crear la cola, y mostrarla
    def proceso_cola(self, cont_cola, tam_cola):
        self.win.fill((0,0,0))
        if cont_cola == 0:
            self.crear_cola()
            self.crear_botones()
            self.cartas_apiladas(self.n_cartas)
            tam_cola = self.mostrar_cola1()
            self.mostrar_cola_4filas(tam_cola)
        else: 
            if cont_cola%2 == 0: 
                self.crear_botones()
                self.mostrar_cola_4filas(tam_cola)
            else: 
                self.crear_botones()
                self.cartas_apiladas(self.n_cartas)
        
        return tam_cola

    #Se crea un metodo que muestre haga todo el procedo de crear la pila, y mostrarla
    def proceso_pila(self, cont_pila):
        self.win.fill((0,0,0))
        if cont_pila == 0:
            self.crear_cola()
            self.crear_botones()
            self.cartas_apiladas(self.n_cartas)
            tam = self.mostrar_cola1()
            self.mostrar_cola_4filas(tam)
        else: 
            if cont_pila%2 == 0: 
                self.crear_botones()
                tam = self.mostrar_cola1()
                self.mostrar_cola_4filas(tam)
            else: 
                self.crear_botones()
                self.cartas_apiladas(13)
        cont_pila += 1
        return cont_pila