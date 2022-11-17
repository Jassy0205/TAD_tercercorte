class Tree: 
    class csll: 
        class Node: 
            #Creamos el metodo inicializador de la clase nodo
            def __init__(self, value, father): 
                self.value = value
                self.father = father
                self.son = None
                self.next = None

        #Ingreso a la clase sll y creamos el metodo inicializador 
        def __init__(self): 
            self.head = None
            self.tail = None
            self.length = 0

        #Creamos el metodo append para añadir al final del nodo 
        def append(self, value, father): 
            new_node = self.Node(value, father)

            if self.head == None and self.tail == None: 
                self.head = new_node
                self.tail = new_node
                self.tail.next = self.head
            else: 
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node
            self.length += 1

    #Salgo de la clase SLL y entro a la clase Tree
    def __init__(self): 
        self.root = None 
        self.length = 0

    def insert(self, value, father):
        if self.root is None:
            self.root = self.csll()
            self.root.append(value, None)
        else: 
            current_node = self.root.head
            return self.tree_route(value, father, current_node)

    def tree_route(self, value, father, node, comparision_node_value=None):
        auxiliar_node = node.father
        if value == father: 
            print('El nodo ya existe')
        elif node.value == father: 
            if node.son == None: 
                node.son = self.csll() 
                node.son.append(value, node.value)
            else: 
                node.son.append(value, node)
            self.length += 1
            print(value,'->', node.value)
            return True 
        else: 
            if node.son != None: 
                if node.son.head.value is comparision_node_value: 
                    if node.value is self.root.head.value: #node.son.head.value: 
                        print('Valores duplicados')
                    elif node.next.value is not auxiliar_node.son.head.value:
                        return self.tree_route(value, father, node.next, node.value)
                    else: 
                        return self.tree_route(value, father, node.father, node.next.value)
                else:
                    return self.tree_route(value, father, node.son.head, node.son.head.value)
            elif node.next.value != auxiliar_node.son.head.value:
                return self.tree_route(value, father, node.next, node.value)
            else:
                return self.tree_route(value, father, node.father, node.next.value)
                '''elif node.next.value is not auxiliar_node.son.head.value:
                    return self.tree_route(value, father, node.next, node.value)
                else: 
                    return self.tree_route(value, father, node.father, node.next.value)'''





