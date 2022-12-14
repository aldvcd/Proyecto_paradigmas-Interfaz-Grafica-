#!/usr/bin/env python3
'''
Modulo: Orden
Contiene todos los datos y definiciones de las clases que se utilizaran cuando se quiera generar una 
orden de compra/venta
Autor:Alejandro David Velazquez.
'''
from abc import ABCMeta, abstractmethod



class Orden(metaclass=ABCMeta):
    '''Clase abstracta que representa cualquiera de las ordenes que se pueden emitir en el deposito'''
    def __init__(self,codigo_orden,articulo,cantidad,total_orden):
        self.codigo_orden=codigo_orden
        self.articulo=articulo
        self.cantidad=cantidad
        self.total_orden=total_orden
        self.estado='PENDIENTE'
    def __str__(self) -> str:
        return f'''
        ------------------------------------------------
        Codigo de orden:            {self.codigo_orden}
        Articulos:                  {self.articulo}
        ------------------------------------------------
        Cantidad Requerida:         {self.cantidad}
        Importe total:              {self.total_orden}
        Estado:                     {self.estado}
        '''
    def __repr__(self) -> str:
        return str(f'''
        
        Codigo de orden:            {self.codigo_orden}
        Articulos:                  {self.articulo}
        ------------------------------------------------
        Cantidad Requerida:         {self.cantidad}
        Importe total:              {self.total_orden}
        Estado:                     {self.estado}
        '''
        )
    @abstractmethod
    def aprobar_orden(self):
        '''Metodo abstracto que permitirá actualizar el stock del producto una vez aprobada la orden de venta/compra 
        '''
        pass
    def rechazar_orden(self):
        '''Clase que se encarga de rechazar una orden de pago, en caso que no corresponda la aprobación cambia el estado 
        a rechazado. Realiza la validación para que solamente se puedan aprobar ordenes en estado PENDIENTE'''
        if (self.estado=="PENDIENTE"):
            self.estado='RECHAZADO'
            return 'La orden ha sido rechazada'
        elif (self.estado=="APROBADO"):
            return 'No se puede rechazar una orden ya aprobada.'

class OrdenVenta(Orden):
    '''Clase que representa u   na orden de venta, esto quiere decir para los clientes que desean comprar
    un articulo o una serie de articulos'''
    def __init__(self, codigo_orden, articulo,cantidad,total_orden ,cliente):
        self.tipo='Venta'
        super().__init__(codigo_orden,articulo,cantidad,total_orden)
        self.cliente=cliente
    def __str__(self) -> str:
        return f'''
        ORDEN DE VENTA
        {super().__str__()}
        '''
    #TODO: Pendiente de implementar la clase aprobar_orden
    def aprobar_orden(self,articulo_stock,orden):
        '''La clase se encargará de realizar la actualización del stock si corresponde a una orden de venta, debe restar del stock
        actual registrada en la persistencia'''
        if orden.estado=='PENDIENTE':
            articulo_stock.stock=articulo_stock.stock-orden.cantidad
            orden.estado=='APROBADO'
            return articulo_stock,"Orden aprobada"
        elif orden.estado=='APROBADO':
            return articulo_stock,'No se puede aprobar una orden mas de una vez. Favor cargue una nueva orden.'
            #'No se puede aprobar una orden mas de una vez. Favor cargue una nueva orden.'
        elif orden.estado=='RECHAZADO':
            return articulo_stock,'No se puede aprobar una orden mas de una vez. Favor cargue una nueva orden.'
            #'No se puede aprobar una orden rechazada. Favor cargue una nueva orden.'

class OrdenCompra(Orden):
    def __init__(self, codigo_orden, articulo,cantidad,total_orden):
        super().__init__(codigo_orden,articulo,cantidad,total_orden)
    def __str__(self) -> str:
        return f'''
        ORDEN DE COMPRA
        {super().__str__()}
        '''

    def aprobar_orden(self, articulo_stock,orden):
        '''La clase se encargará de realizar la actualización del stock si corresponde a una orden de compra, debe sumar del stock
        actual registrada en la persistencia'''
        if orden.estado=='PENDIENTE':
            articulo_stock.stock=articulo_stock.stock+orden.cantidad
            orden.estado=='APROBADO'
            return articulo_stock,"Orden aprobada"
        elif orden.estado=='APROBADO':
            return articulo_stock,'No se puede aprobar una orden mas de una vez. Favor cargue una nueva orden.'
            #'No se puede aprobar una orden mas de una vez. Favor cargue una nueva orden.'
        elif orden.estado=='RECHAZADO':
            return articulo_stock,'No se puede aprobar una orden mas de una vez. Favor cargue una nueva orden.'
            #'No se puede aprobar una orden rechazada. Favor cargue una nueva orden.'


if __name__=='__main__':
   orden=OrdenCompra(1,"Amex",10,1500000)
   stock=MuebleCocina(1,"Amex",150000)
   ordenVenta=OrdenVenta(1,"Amex",5,50000,"Juan Perez")
   print(orden.aprobar_orden(stock,orden))
   print(ordenVenta.aprobar_orden(stock,ordenVenta))