#!/usr/bin/env python3

class Persona:
    def __init__(self,cedula_identidad, nombres,apellidos,ruc):
        self.cedula_identidad=cedula_identidad
        self.nombres=nombres
        self.apellidos=apellidos
        self.ruc=ruc
    def __str__(self) -> str:
        return f'''
        Numero de cedula:   {self.cedula_identidad}
        Nombre completo:    {self.nombres}     
        Apellido completo;  {self.apellidos}
        RUC:                {self.ruc}

        '''
if __name__=='__main__':
   pass