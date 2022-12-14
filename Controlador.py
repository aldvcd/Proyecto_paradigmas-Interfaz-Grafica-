#!/usr/bin/env python3

from Model import *
from Muebles import *
from Persona import *
from Orden import *


class Deposito:
    def __init__(self):
        self.ultimo_codigo_orden=0
        self.model = Model()
        #Directorio donde se encuentra la base de muebles.
        self.directorioMuebles='./Persistencia/BaseMuebles/Muebles.fs'
        #Directorio donde se encuentra la base de Ordenes de venta/compra generada.
        self.directorioOrdenes='./Persistencia/BaseOrden/Ordenes.fs'
        #Directorio donde se enuentra la base de Personas a los que se le asigna una orden.
        self.directorioPersonas='./Persistencia/BasePersona/Personas.fs'

        #Se obtienen los datos de la persistencia y se almacenan dentro de las listas
        self.__muebles = self.model.generar_lista(self.directorioMuebles)
        self.__ordenes = self.model.generar_lista(self.directorioOrdenes)
        self.__personas = self.model.generar_lista(self.directorioPersonas)
        #Obtener el ultimo numero de orden
        if self.__ordenes:
            self.ultimo_codigo_orden = self.__ordenes[-1].codigo_orden+1

    def listar_muebles(self):
        '''Obtiene la lista de muebles para observar su stock'''
        return self.__muebles
    def listar_ordenes(self):
        '''Obtiene la lista de ordenes de compra/venta'''
        return self.__ordenes
    def vender(self,codigo,cantidad,cedula,nombre,apellido,ruc):
        '''Clase que se encarga de recibir el codigo de articulo y venderlo si hay stock disponible
            se invoca al articulo.vender() para que genere la orden de venta esta retorna una orden y
            se guarda en la persistencia
            self,codigo,articulo,cantidad, cliente
        '''
        cliente=Persona(cedula,nombre,apellido,ruc)
        for elemento in self.__muebles:
            if elemento.codigo==codigo:
                if elemento.stock>=cantidad:
                    ordenVenta=elemento.vender(self.ultimo_codigo_orden,elemento,cantidad,cliente)
                    self.model.guardar_objeto(self.directorioOrdenes, ordenVenta, self.ultimo_codigo_orden)
                    self.__ordenes = self.model.generar_lista(self.directorioOrdenes)
                    return 'OK'
                elif elemento.stock<cantidad:
                    return 'No existe stock suficiente'

        #self.__ordenes=self.model.generar_lista(self.directorioOrdenes)

    def reponer(self,codigo,cantidad):
        '''''Clase que se encarga de recibir el codigo de articulo y comprarlo si hay stock disponible
       se invoca al articulo.reponer() para que genere la orden de compra esta retorna una orden y
       se guarda en la persistencia'''
        for elemento in self.__muebles:
            if elemento.codigo == codigo:
                ordenCompra = elemento.reponer(self.ultimo_codigo_orden,elemento,cantidad)
                self.model.guardar_objeto(self.directorioOrdenes, ordenCompra, self.ultimo_codigo_orden)
                self.__ordenes = self.model.generar_lista(self.directorioOrdenes)
        return "OK"
    def gestionar_orden(self,codigo_orden,estado):
        '''Metodo que se encarga de aprobar una orden en especifico recibe com parametro
        el código de orden. Esta debe de pasar el estado de la orden y llamar al metodo
        vender o reponer del articulo.
        Recibe ademas un estado de tipo numerico el cual indica si la orden fue aprobada o rechazada.
        1-->Aprobado
        0-->Rechazado
        '''
        for elemento in self.__ordenes:
            for producto in self.__muebles:
                if elemento.codigo_orden==codigo_orden and producto.codigo==elemento.articulo.codigo:
                    if estado==1:

                        resultado=elemento.aprobar_orden(producto,elemento)
                        elemento.estado="APROBADO"
                        elementoNuevo=elemento
                        stockActual,mensaje =resultado[0],resultado[1]

                        self.model.guardar_objeto(self.directorioMuebles,stockActual,stockActual.codigo)
                        self.model.guardar_objeto(self.directorioOrdenes,elementoNuevo,elementoNuevo.codigo_orden)
                        self.__ordenes = self.model.generar_lista(self.directorioOrdenes)
                        if isinstance(elemento,OrdenVenta):
                            self.model.guardar_objeto(self.directorioPersonas,elemento.cliente,elemento.cliente.cedula_identidad)
                        return mensaje
                    elif estado==2:
                        mensaje=elemento.rechazar_orden()
                        elemento.estado = "RECHAZADO"
                        elementoNuevo=elemento
                        self.model.guardar_objeto(self.directorioOrdenes, elementoNuevo, elementoNuevo.codigo_orden)
                        self.__ordenes = self.model.generar_lista(self.directorioOrdenes)
                        return mensaje

        

    


if __name__=='__main__':
    Deposito1=Deposito()

    #Deposito1.reponer(1,10)
    #Deposito1.reponer(1, 10)
    Deposito1.reponer(2, 10)
    #Deposito1.vender(1,7,5290061,'ALEJANDRO','PEREZ','5290061-1')
    #Deposito1.reponer(2,10)
    #print(Deposito1.listar_ordenes()[3])
    #print(Deposito1.listar_muebles())
    #Deposito1.vender(1,10,5290061,"Alejandro","Velazquez",5290061)
    #print(Deposito1.listar_ordenes())
    #print(Deposito1.gestionar_orden(6,2))
    print(Deposito1.listar_ordenes())
    if not isinstance(Deposito1, Deposito):
        print("Asi es")

    