# -*- coding: utf-8 -*-
"""proyecto1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14MvFe-pz3pP5FHvAV_VeujirD6XKp6T4
"""

class Producto():

    def __init__(self,nombre):
        self.nombre = nombre
        self.tiempoEntarea=0

class Proceso():

    def __init__(self,nombre):
        self.nombre = nombre
        self.cola=Cola()


    def agregarACola(self,object):
      self.cola.encolar(object)

    def sacarACola(self,object):
        self.cola.desencolar(object)

class Tarea(Proceso):

    def __init__(self,nombre,tiempo):
        super().__init__(nombre)
        self.ocupado=False
        self.productoEnProceso=""


    def __str__(self):
      return self.nombre

    def agregarACola(self,object):
      self.cola.encolar(object)

    def sacarACola(self,object):
        self.cola.desencolar(object)

class Nodo(object):

    def __init__(self, valor, siguiente=None):
        self.siguiente = siguiente
        self.valor = valor

    def __str__(self):
      return f'El valor del nodo es {self.valor} y apunta a {self.siguiente.valor}'

class Cola(object):

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def __str__(self):
        cola = ''
        siguiente = self.primero
        while siguiente:
            cola += '\n\t-{}'.format(siguiente.valor)
            siguiente = siguiente.siguiente
        return cola

    def encolar(self, elemento):
        """Guarda el elemento a insertar al final de la cola"""
        nodo = Nodo(elemento)
        self.tamanio += 1
        if not self.primero:
            self.primero = nodo
        else:
            self.ultimo.siguiente = nodo

        self.ultimo = nodo


    def desencolar(self):
        """Quita y retorna el primer elemento insertado"""
        nodo = self.primero
        try:
            elemento = nodo.valor
        except AttributeError:
            raise Exception(u'No se puede desencolar más elementos')
        self.primero = nodo.siguiente
        self.tamanio -= 1

        return elemento

    def esta_vacia(self):
        """Devuelve True si la cola no contiene elementos y
        False en el caso de que tenga al menos un elemento"""
        return not self.tamanio

class Lista(object):

    def __init__(self):
        self.primero = None
        self.cursor = None
        self.tamanio = 0

    def __str__(self):
        lista = '<Lista: '
        siguiente = self.primero
        while siguiente:
            lista += '{} | '.format(siguiente.valor.nombre)
            siguiente = siguiente.siguiente

        lista +='>'
        return lista

    def obtener_elemento(self):
        """Retorna el elemento de la posición actual"""
        try:
            return self.cursor.valor.nombre
        except AttributeError:
            return "lista vacia"

    def insertar_siguiente(self, elemento):
        """Guarda el elemento a insertar en la posición actual"""
        nodo = Nodo(elemento)
        if not self.primero:
            self.primero = nodo
        else:
            nodo.siguiente = self.cursor.siguiente
            self.cursor.siguiente = nodo

        self.cursor = nodo
        self.tamanio += 1

    def eliminar(self, posicion):
        """Elimina el elemento de la posición indicada"""
        if posicion > self.tamanio:
            msg = u'Se quiere borrar la posición {0} y la lista sólo tiene' \
                  u' {1} elementos'
            raise Exception(msg.format(posicion, self.tamanio))
        elif posicion == 1:
            nodo = self.primero
            self.primero = self.primero.siguiente
        else:
            nodo_anterior = self.primero
            pos_nodo = 2
            while pos_nodo < posicion:
                nodo_anterior = nodo_anterior.siguiente
                pos_nodo += 1
            # Nodo a borrar
            nodo = nodo_anterior.siguiente

            if self.cursor == nodo_anterior.siguiente:
                self.cursor = nodo_anterior.siguiente.siguiente

            #Si no es el ultimo de la lista
            if nodo_anterior.siguiente:
                nodo_anterior.siguiente = nodo_anterior.siguiente.siguiente

        self.tamanio -= 1
        return nodo

    def ir_al_primero(self):
        """Posiciona el cursor apuntando al primer elemento de la lista"""
        self.cursor = self.primero

    def ir_al_ultimo(self):
        self.ir_al_primero()
        i=1
        while(i!=self.tamanio):
            self.cursor=self.cursor.siguiente
            i+=1

    def buscar(self,dato):
        self.ir_al_primero()
        i=1
        while(i<=self.tamanio):
            if(self.cursor.valor.nombre==dato):
                return self.cursor.valor
            else:
                self.cursor=self.cursor.siguiente
                i+=1

        return "no existe en la lista"

    def siguiente(self):
        if(self.cursor.siguiente==None):
            self.cursor =self.primero
        else:
            self.cursor = self.cursor.siguiente


    def anterior(self):
            if(self.cursor!=self.primero):
                n1=self.primero
                antes=None
                while(n1!=self.cursor):
                    antes=n1
                    n1=n1.siguiente
                self.cursor=antes
            else:
                n1=self.primero
                i=1
                while(i!=self.tamanio):
                    n1=n1.siguiente
                    i+=1
                self.cursor=n1


    def esta_vacia(self):
        return not self.tamanio



    def get_cursor_pos(self):
        n1=self.primero
        i=1
        while(n1.valor.nombre!=self.cursor.valor.nombre):
            n1=n1.siguiente
            i+=1
        return i

    def set_cursor(self,pos):
        self.ir_al_primero()
        i=1
        while(i!=pos):
            self.cursor=self.cursor.siguiente
            i+=1

    def get_nodo_pos(self,pos):
        n1=self.primero
        i=1
        while(i!=pos):
            n1=n1.siguiente
            i+=1
        return n1

    def mov(self,ind2Mov,posicion):
           self.set_cursor(ind2Mov)
           tmp=self.get_nodo_pos(posicion-1)
           tmp2=self.get_nodo_pos(ind2Mov-1)
           tmp2.siguiente= self.cursor.siguiente
           self.cursor.siguiente=tmp.siguiente
           tmp.siguiente=self.cursor

class LineaProduccion(object):

    def __init__(self):
        self.procInicial = Proceso("Inicio")
        self.procfunal = Proceso("Fin")
        self.lProce = Lista()
        self.lProce.insertar_siguiente(self.procInicial)
        self.lProce.insertar_siguiente(self.procfunal)
        self.lProce.set_cursor(1)

    def GenerarReporte(self):
        """Recorre todos los procesos, tareas y productos asociados en la línea de producción"""
        nodo_proceso = self.lProce.primero

        while nodo_proceso:
            proceso = nodo_proceso.valor
            print(f"Proceso: {proceso.nombre}")

            if not proceso.cola.esta_vacia():
                nodo_tarea = proceso.cola.primero

                while nodo_tarea:
                    tarea = nodo_tarea.valor
                    print(f"\tTarea: {tarea.nombre}")

                    if not tarea.cola.esta_vacia():
                        nodo_producto = tarea.cola.primero

                        while nodo_producto:
                            producto = nodo_producto.valor
                            print(f"\t\tProducto: {producto.nombre}")

                            nodo_producto = nodo_producto.siguiente

                    nodo_tarea = nodo_tarea.siguiente

            nodo_proceso = nodo_proceso.siguiente


    def insertarProceso(self,pro):
      self.lProce.insertar_siguiente(pro)

    #def insertarTarea(tarea):

l=LineaProduccion()
#l.GenerarReporte()
p1=Proceso("Preparar")
l.insertarProceso(p1)
#l.GenerarReporte()
t1=Tarea("Pintar",1)
p1.agregarACola(t1)


t2=Tarea("Empacar",1)
p1.agregarACola(t2)

pr1=Producto("Figura")
pr2=Producto("Figura2")
t1.agregarACola(pr1)
t1.agregarACola(pr2)
l.GenerarReporte()

import datetime

def imprimir_cada_segundo():
    contador = 0
    tiempo_inicial = datetime.datetime.now()
    while True:
        tiempo_actual = datetime.datetime.now()
        if (tiempo_actual - tiempo_inicial).seconds >= 1:
            print("Segundo:", contador)
            contador += 1
            tiempo_inicial = tiempo_actual

# Llama a la función para empezar a imprimir cada segundo
imprimir_cada_segundo()