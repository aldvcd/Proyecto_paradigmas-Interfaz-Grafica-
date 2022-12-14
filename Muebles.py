#!/usr/bin/env python3
'''
Modulo: Muebles
Contiene todos los datos y definiciones de las clases que se utilizaran cuando se quiera utilizar un
articulo del deposito
Autor:Alejandro David Velazquez.
'''
#!/usr/bin/env python3
from msilib.schema import InstallUISequence
from Orden import OrdenVenta,OrdenCompra
from abc import ABCMeta, abstractmethod


class Mueble(metaclass =ABCMeta):
    def __init__(self,codigo,descripcion,precio,proveedor):
        self.codigo=codigo
        self.descripcion=descripcion
        self.precio=precio
        self.stock=0
        self.proveedor=proveedor
        self.iva=10

    @abstractmethod
    def vender(self):
        '''Metodo abstracto para la venta de un articulo,
        la misma se encargará de generar la orden de venta'''
        pass
    @abstractmethod
    def reponer(self):
        '''Metdodo abstracto para la reposición de
        un articulo, la misma se encargara de generar
        la orden de compra'''
        pass
    @abstractmethod
    def calcular_precio(self):
        '''Metodo abstracto para calcular el precio de un
        articulo'''
        pass

    def __str__(self):
        '''Primero se establece el precio del articulo'''
        self.calcular_precio()
        return f'''
        Codigo del producto:     {self.codigo}
        Nombre del producto:     {self.descripcion}
        Precio unitario:         {self.precio}
        Stock Actual:            {self.stock}
        Proveedor:               {self.proveedor}
        Porcentaje de iva:       {self.iva}%
        '''
    def __repr__(self) -> str:
        return f'''
        Codigo del producto:     {self.codigo}
        Nombre del producto:     {self.descripcion}
        Precio unitario:         {self.precio}
        Stock Actual:            {self.stock}
        Proveedor:               {self.proveedor}
        Porcentaje de iva:       {self.iva}%
        '''
    def __eq__(self, codigo):
        '''Metodo para determinar si dos articulos son iguales'''
        return self.codigo == codigo

class MuebleCocina(Mueble):
    '''Clase que representa a los Muebles de cocina'''
    def __init__(self,codigo,descripcion,precio,proveedor='Arrex cocinas'):
        super().__init__(codigo,descripcion,precio,proveedor)
        self.recargo=0.2

    def __str__(self):
        return super().__str__()

    def __eq__(self, codigo):
        return super().__eq__(self,self.codigo)
    #TODO : Pendiente de implementar la clase Vender
    def vender(self,codigo,articulo,cantidad, cliente):
        '''Clase que se encargará de generar una orden de venta. La clase debe calcular el precio del articulo para instanciar
        el objeto OrdenVenta'''
        precioFinal=self.calcular_precio()*cantidad
        orden=OrdenVenta(codigo,articulo,cantidad,precioFinal,cliente)
        return orden


    #TODO : Pendiente de implementar la clase reponer
    def reponer(self,codigo,articulo,cantidad):
        '''Clase que se encargará de generar una orden de venta. La clase debe calcular el precio del articulo para instanciar
        el objeto OrdenCompra'''
        precioFinal=self.calcular_precio()*cantidad
        orden=OrdenCompra(codigo,articulo,cantidad,precioFinal)
        return orden


    def calcular_precio(self):
        '''Calculo del precio correspondiente a un mueble de Cocina. Requiere un calculo del recargo del 20% del precio de costo del 
        producto.'''

        precioFinal=self.precio+(self.precio*self.recargo)+(self.precio*self.iva/100)
        return precioFinal


class MueblaHabitacion(Mueble):
    '''Clase que representa a los Muebles de Habitación'''
    def __init__(self,codigo,descripcion,precio,proveedor='Koala S.A'):
        super().__init__(codigo,descripcion,precio,proveedor)

    def __str__(self):
        return super().__str__()
        
    def __eq__(self, codigo):
        return super().__eq__(self,self.codigo)
   
    #TODO : Pendiente de implementar la clase Vender
    def vender(self,codigo,articulo,cantidad, cliente):
        '''Clase que se encargará de generar una orden de venta. La clase debe calcular el precio del articulo para instanciar
        el objeto OrdenVenta
        codigo, articulo, cantidad, (articulo.calcular_precio() * cantidad), cliente'''
        precioFinal=self.calcular_precio()*cantidad
        orden = OrdenVenta(codigo, articulo, cantidad, precioFinal, cliente)
        return orden

    #TODO : Pendiente de implementar la clase reponer
    def reponer(self,codigo,articulo,cantidad):
        precioFinal = self.calcular_precio() * cantidad
        orden = OrdenCompra(codigo, articulo, cantidad, precioFinal)
        return orden


    def calcular_precio(self):
        '''Calculo del precio correspondiente a un mueble de Habitación. No requiere recargo.'''
        precioFinal=self.precio=self.precio+(self.precio*(self.iva)/100)
        return precioFinal

class MuebleSala(Mueble):
    '''Clase que representa a los Muebles de la sala'''
    def __init__(self,codigo,descripcion,precio,proveedor='Aimar muebles S.A'):
        super().__init__(codigo,descripcion,precio,proveedor)

    def __str__(self):
        return super().__str__()
        
    def __eq__(self, codigo):
        return super().__eq__(self,self.codigo)
     #TODO : Pendiente de implementar la clase Vender
    def vender(self,codigo,articulo,cantidad, cliente):
        '''Clase que se encargará de generar una orden de venta. La clase debe calcular el precio del articulo para instanciar
        el objeto OrdenVenta'''
        precioFinal=(self.calcular_precio()*cantidad)
        orden=OrdenVenta(codigo,articulo,cantidad,precioFinal,cliente)
        return orden
    #TODO : Pendiente de implementar la clase reponer
    def reponer(self,codigo,articulo,cantidad):
        precioFinal = (self.calcular_precio() * cantidad)
        orden=OrdenCompra(codigo,articulo,cantidad,precioFinal)
        return orden

    def calcular_precio(self):
        '''Calculo del precio correspondiente a un mueble de Sala. No requiere recargo.'''
        self.precio=self.precio+(self.precio*(self.iva)/100)
        return self.precio

class MuebleBaño(Mueble):
    '''Clase que representa a los Muebles de Baño'''
    def __init__(self,codigo,descripcion,precio,proveedor='Coexma S.R.L'):
        super().__init__(codigo,descripcion,precio,proveedor)

    def __str__(self):
        return super().__str__()
        
    def __eq__(self, codigo):
        return super().__eq__(self,self.codigo)
    #TODO : Pendiente de implementar la clase Vender
    def vender(self,codigo,articulo,cantidad, cliente):
        '''Clase que se encargará de generar una orden de venta. La clase debe calcular el precio del articulo para instanciar
        el objeto OrdenVenta'''
        precioFinal=(self.calcular_precio()*cantidad)
        orden=OrdenVenta(codigo,articulo,cantidad,precioFinal,cliente)
        return orden
    #TODO : Pendiente de implementar la clase Vender
    def reponer(self,codigo,articulo,cantidad):
        precioFinal = (self.calcular_precio() * cantidad)
        orden=OrdenCompra(codigo,articulo,cantidad,precioFinal)
        return orden

    @staticmethod
    def calcular_precio(self):
        '''Calculo del precio correspondiente a un mueble de baño. No requiere recargo.'''
        self.precio=self.precio+(self.precio*(self.iva)/100)
        return self.precio

if __name__=='__main__':
    mueble=MueblaHabitacion(1,"MuebleCocina",2000)
    if isinstance(mueble,MuebleCocina):
        print("Es mueble de cocina")
    else:
        print(type(mueble))

    orden=mueble.vender(1,mueble,2,"Juan Perez")
    print(orden)
    ordenCompra=mueble.reponer(1,mueble,2)
    print(ordenCompra)