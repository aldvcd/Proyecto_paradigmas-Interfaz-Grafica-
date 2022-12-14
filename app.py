from Controlador import Deposito
from View import *
from tkinter import Tk
import sys

class app():
    class App:
        '''Clase que se utiliza para iniciar el sistema'''

        @staticmethod
        def main():
            control = Deposito()
            root = Tk()  # raiz de la vista Tkinter
            vista = View(control, root)
            vista.mainloop()

    if __name__ == '__main__':
        App.main()
