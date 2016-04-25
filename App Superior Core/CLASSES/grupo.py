# -*- coding: utf-8 -*-

class Grupo():
    """
        Clase que define a un grupo dentro de la aplicación.

        Args:
            nombre(string): Nombre grupo. Valor por defecto None.
            descripcion(string): Descripción breve del grupo. Valor por
                            defecto None
            fecha_creacion(string): Fecha creacion grupo.Valor por defecto None.

        Attributes:
            nombre(string): Nombre del grupo, utilizado como identificador
                            dentro de la aplicación.
            descripcion(string): Descripción breve acerca del grupo.
    """
    def __init__(self, nombre="", descripcion=""):
        super(Grupo, self).__init__()
        self.nombre = nombre
        self.descripcion = descripcion

    # Métodos Modificadores
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    # Métodos consultores
    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion
