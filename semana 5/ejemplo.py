class Nodo:

    def __init__(self, dato):
        self.data = dato
        self.siguiente = None

    a = Nodo (5)
    b = Nodo (10)

    print("referencia de a: ",a)
    print("referencia de b: ",b)

    a.siguiente = b

    c = Nodo(15)
    d = Nodo(20)
    b.siguiente = c
    c.siguiente = d
    print("referencia de c: ",c)
    print("referencia de d: ",d)

    print("referencia de a.siguiente: ",a.dato)
    print("referencia de b.siguiente: ",b.dato)
    print("referencia de c.siguiente: ",c.dato)
    print("referencia de d.siguiente: ",d.dato)
#-----------------------------------------------
#Asignación de valores a los nodos
#________________________________________________

n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

n1.siguiente = n3
#opcion 1 variable temoral
temporal = n1.siguiente
n1.siguiente.siguiente = temporal
#opcion 2: sin variable temporal
n1.siguiente = n2
n2.siguiente = n3
