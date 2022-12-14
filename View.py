import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from Controlador import Deposito
from Orden import *
class View(Frame):
    def __init__(self,controlador,ventana=None):
        Frame.__init__(self,ventana)
        self.control=controlador
        ventana.title("DEPOS")
        ventana.geometry("900x550")
        ventana.resizable(0,0)

        #Ventana Vender
        self.ventanaVender=None
        self.ventanaComprar=None
        self.ventanaGestionar=None
        self.cajaCodigo=None
        self.cajaCantidad=None
        self.cajaCedula=None
        self.cajaNombre=None
        self.cajaApellido=None
        self.cajaRuc=None
        self.cajaCodigoOrden=None
        self.cajaEstado=None


        #Variables
        self.codigoArticulo=None
        self.cantidadArticulo=StringVar()
        self.cedulaCliente=StringVar()
        self.nombreCliente=StringVar()
        self.apellidoCliente=StringVar()
        self.rucCliente=StringVar()


        #icono
        self.icono=PhotoImage(file='logo.png')
        ventana.tk.call('wm', 'iconphoto', ventana._w, self.icono)
        #Etiqueta=DEPOS
        etiqueta=tkinter.Label(ventana,text="DEPOS",width=10,height=5)
        etiqueta.grid(row=0,column=0)


        #Pantalla lateral
        self.pantallaLateral=tkinter.Text(height=32,width=80,state="disable")
        self.pantallaLateral.place(x=210, y=20)
        scroll = tkinter.Scrollbar(orient=tkinter.VERTICAL, command=self.pantallaLateral.yview())
        scroll.place(x=860,y=20,height=515,width=20)
        scroll.config(command=self.pantallaLateral.yview())
        self.pantallaLateral.config(yscrollcommand=scroll.set)

        # Botones
        botonListarMuebles = tkinter.Button(ventana, text="Listar Muebles", width=25, height=2,command=self.listarMuebles)
        botonListarOrdenes = tkinter.Button(ventana, text="Listar Ordenes", width=25, height=2,command=self.listarOrdenes)
        botonVender = tkinter.Button(ventana, text="Vender", width=25, height=2,command=self.Vender)
        botonReponer = tkinter.Button(ventana, text="Reponer", width=25, height=2,command=self.Comprar)
        botonGestionarOrden = tkinter.Button(ventana, text="Aprobar/Rechazar Orden", width=25, height=2,command=self.gestionarOrden)
        botonAgregarMueble = tkinter.Button(ventana, text="Agregar ariculo", width=25, height=2)
        botonListarMuebles.grid(row=1, pady=10, padx=10)
        botonListarOrdenes.grid(row=2, pady=10)
        botonVender.grid(row=3, pady=10)
        botonReponer.grid(row=4, pady=10)
        botonGestionarOrden.grid(row=5, pady=10)
        botonAgregarMueble.grid(row=6, pady=10)

        #Menus desplegables
        #ventanaVender()

    def listarMuebles(self):
        articulos=self.control.listar_muebles()
        self.pantallaLateral.config(state=NORMAL)
        self.pantallaLateral.delete("1.0", "end")
        for elementos in articulos:
            self.pantallaLateral.insert(END,'Codigo del producto: ')
            self.pantallaLateral.insert(END,elementos.codigo)
            self.pantallaLateral.insert(END, ' ('+elementos.descripcion+')\n---------------------------------------------\n')
            self.pantallaLateral.insert(END, '\tPrecio Unitario: '+str(elementos.precio)+'\n')
            self.pantallaLateral.insert(END, '\tStock actual: '+str(elementos.stock)+'\n')
            self.pantallaLateral.insert(END, '\tProveedor: ' + str(elementos.proveedor) + '\n')
            self.pantallaLateral.insert(END, '\tPorcentaje de IVA: ' + str(elementos.iva) + '\n\n')
        print("Hola mundo")
        self.pantallaLateral.config(state=DISABLED)

    def listarOrdenes(self):
        ordenes=self.control.listar_ordenes()
        self.pantallaLateral.config(state=NORMAL)
        self.pantallaLateral.delete("1.0", "end")
        for elementos in ordenes:
            if isinstance(elementos,OrdenVenta):
                self.pantallaLateral.insert(END, '\n'+str(elementos.codigo_orden+1)+') ORDEN DE VENTA\n')
                self.pantallaLateral.insert(END,'Codigo de orden:\t\t'+str(elementos.codigo_orden)+'\n')
                self.pantallaLateral.insert(END, '------------------------------------------------\n')
                self.pantallaLateral.insert(END, 'Articulos:\n' + str(elementos.articulo) + '\n')
                self.pantallaLateral.insert(END, '------------------------------------------------\n')
                self.pantallaLateral.insert(END, 'Cantidad requerida: ' + str(elementos.cantidad) + '\n')
                self.pantallaLateral.insert(END, 'Cantidad total: ' + str(elementos.total_orden) + '\n')
                self.pantallaLateral.insert(END, 'Estado: ' + str(elementos.estado) + '\n')
                self.pantallaLateral.insert(END, '------------------------------------------------\n')
            elif isinstance(elementos,OrdenCompra):
                self.pantallaLateral.insert(END, '\n'+str(elementos.codigo_orden+1)+') ORDEN DE COMPRA\n')
                self.pantallaLateral.insert(END, 'Codigo de orden:\t\t' + str(elementos.codigo_orden) + '\n')
                self.pantallaLateral.insert(END, '------------------------------------------------\n')
                self.pantallaLateral.insert(END, 'Articulos:\n' + str(elementos.articulo) + '\n')
                self.pantallaLateral.insert(END, '------------------------------------------------\n')
                self.pantallaLateral.insert(END, 'Cantidad requerida: ' + str(elementos.cantidad) + '\n')
                self.pantallaLateral.insert(END, 'Cantidad total: ' + str(elementos.total_orden) + '\n')
                self.pantallaLateral.insert(END, 'Estado: ' + str(elementos.estado) + '\n')
                self.pantallaLateral.insert(END, '------------------------------------------------\n')
        print("Hola mundo")
        self.pantallaLateral.config(state=DISABLED)
    #TODO: TERMINAR LA CLASE VENDER, AHORA CENTRARSE SOLO EN REPONER Y APROBAR
    def Vender(self):
        self.ventanaVender=tkinter.Toplevel()
        self.ventanaVender.title("Venta de articulos")
        self.ventanaVender.geometry("400x400")
        etiquetaTitulo=tkinter.Label(self.ventanaVender, textvariable=self.codigoArticulo,text="VENTA DE ARTICULOS",font=("Arial",15))
        etiquetaTitulo.place(x=90,y=20)

        etiquetaCodigo=tkinter.Label(self.ventanaVender,text="Codigo de articulo: ")
        etiquetaCodigo.place(x=10,y=70)
        self.cajaCodigo=tkinter.Entry(self.ventanaVender,width=20)
        self.cajaCodigo.place(x=120,y=70)

        etiquetaCantidad = tkinter.Label(self.ventanaVender, text="Cantidad requerida: ")
        etiquetaCantidad.place(x=10, y=100)
        self.cajaCantidad = tkinter.Entry(self.ventanaVender, width=20)
        self.cajaCantidad.place(x=120, y=100)


        etiquetaDatosCli = tkinter.Label(self.ventanaVender, text="DATOS DEL CLIENTE", font=("Arial", 15))
        etiquetaDatosCli.place(x=90, y=130)

        etiquetaCedula = tkinter.Label(self.ventanaVender, text="Cedula: ")
        etiquetaCedula.place(x=10, y=170)
        self.cajaCedula = tkinter.Entry(self.ventanaVender, width=20)
        self.cajaCedula.place(x=120, y=170)

        etiquetaNombre = tkinter.Label(self.ventanaVender, text="Nombres: ")
        etiquetaNombre.place(x=10, y=200)
        self.cajaNombre = tkinter.Entry(self.ventanaVender, width=30)
        self.cajaNombre.place(x=120, y=200)

        etiquetaApellido = tkinter.Label(self.ventanaVender, text="Apellidos: ")
        etiquetaApellido.place(x=10, y=230)
        self.cajaApellido = tkinter.Entry(self.ventanaVender, width=30)
        self.cajaApellido.place(x=120, y=230)

        etiquetaRuc = tkinter.Label(self.ventanaVender, text="Ruc: ")
        etiquetaRuc.place(x=10, y=260)
        self.cajaRuc = tkinter.Entry(self.ventanaVender, width=30)
        self.cajaRuc.place(x=120, y=260)

        botonAceptar = tkinter.Button(self.ventanaVender, text="Aceptar", width=25, height=2
                                      ,command=self.guardarVenta)
        botonAceptar.place(x=120, y=300)

    def guardarVenta(self):
        mensaje=self.control.vender(int(self.cajaCodigo.get()),int(self.cajaCantidad.get()),int(self.cajaCedula.get()),
                                    str(self.cajaNombre.get()),str(self.cajaApellido.get()),str(self.cajaRuc.get()))
        if mensaje=="OK":
            messagebox.showinfo('NOTIFICACION', 'ORDEN DE VENTA REGISTRADA CORRECTAMENTE', parent=self.ventanaVender)
            self.ventanaVender.destroy()
        else:
            messagebox.showerror('NOTIFICACION', mensaje, parent=self.ventanaVender)
            self.ventanaVender.destroy()


    # MENU COMPRAR
    def Comprar(self):
        self.ventanaComprar = tkinter.Toplevel()
        self.ventanaComprar.title("Compra de articulos")
        self.ventanaComprar.geometry("400x400")
        etiquetaTitulo = tkinter.Label(self.ventanaComprar, textvariable=self.codigoArticulo, text="COMPRA DE ARTICULOS",
                                       font=("Arial", 15))
        etiquetaTitulo.place(x=90, y=20)

        etiquetaCodigo = tkinter.Label(self.ventanaComprar, text="Codigo de articulo: ")
        etiquetaCodigo.place(x=10, y=70)
        self.cajaCodigo = tkinter.Entry(self.ventanaComprar, width=20)
        self.cajaCodigo.place(x=120, y=70)

        etiquetaCantidad = tkinter.Label(self.ventanaComprar, text="Cantidad requerida: ")
        etiquetaCantidad.place(x=10, y=100)
        self.cajaCantidad = tkinter.Entry(self.ventanaComprar, width=20)
        self.cajaCantidad.place(x=120, y=100)

        botonAceptar = tkinter.Button(self.ventanaComprar, text="Aceptar", width=25, height=2
                                      , command=self.guardarCompra)
        botonAceptar.place(x=120, y=300)

    # Funcion del boton Aceptar de guardarComprar
    def guardarCompra(self):
        codigoArticulo=self.cajaCodigo.get()
        cantidadArticulo=self.cajaCantidad.get()
        mensaje=self.control.reponer(int(self.cajaCodigo.get()),int(self.cajaCantidad.get()))
        if mensaje=="OK":
            messagebox.showinfo('NOTIFICACION', 'ORDEN DE COMPRA REGISTRADA CORRECTAMENTE', parent=self.ventanaComprar)
            self.ventanaComprar.destroy()
        print(mensaje)
        print(type(int(codigoArticulo)))
        print(type(cantidadArticulo))

    #MENU GESTIONAR ORDEN
    def gestionarOrden(self):
        '''
        Esta pantalla sirve para aprobar o rechazar una orden.
        '''
        self.ventanaGestionar = tkinter.Toplevel()
        self.ventanaGestionar.title("Gestionar Orden")
        self.ventanaGestionar.geometry("400x400")
        etiquetaTitulo = tkinter.Label(self.ventanaGestionar, text="GESTIONAR ORDEN",font=("Arial", 15))
        etiquetaTitulo.place(x=90, y=20)

        etiquetaCodigoOrden = tkinter.Label(self.ventanaGestionar, text="Codigo de orden: ")
        etiquetaCodigoOrden.place(x=10, y=70)
        self.cajaCodigoOrden = tkinter.Entry(self.ventanaGestionar, width=20)
        self.cajaCodigoOrden.place(x=120, y=70)

        etiquetaEstado = tkinter.Label(self.ventanaGestionar, text="Estado: ")
        etiquetaEstado.place(x=10, y=100)
        self.cajaEstado = tkinter.ttk.Combobox(self.ventanaGestionar,state="readonly",values=["APROBADO","RECHAZADO"])
        self.cajaEstado.place(x=120, y=100)
        botonAceptar = tkinter.Button(self.ventanaGestionar, text="Aceptar", width=25, height=2,command=self.guardarGestion)
        botonAceptar.place(x=120, y=300)

    #Funcion del boton Aceptar de guardarGestion
    def guardarGestion(self):
        '''
        Funcion que realiza permite grabar los registros, esta se relaciona directamente con el controlador e invoca al
        metodo gestionar_orden()
        '''
        respuesta=self.cajaEstado.get()
        if respuesta=="APROBADO":
            mensaje=self.control.gestionar_orden(int(self.cajaCodigoOrden.get()),1)
            messagebox.showinfo('NOTIFICACION', mensaje, parent=self.ventanaGestionar)
            self.ventanaGestionar.destroy()
        elif respuesta=="RECHAZADO":
            mensaje = self.control.gestionar_orden(int(self.cajaCodigoOrden.get()), 2)
            messagebox.showinfo('NOTIFICACION', mensaje, parent=self.ventanaGestionar)
            self.ventanaGestionar.destroy()

if __name__ == '__main__':
    Control = Deposito()
    ventana=Tk()
    vista=View(Control,ventana)
    vista.mainloop()


