# -*- coding: utf-8 -*-

class Usuario():
    """
        Clase que define a un usuario de la aplicación.

        Args:
            email(string): Email del usuario. Valor por defecto None.
            nombre(string): Nombre del usuario. Valor por defecto None.
            ultimo_acceso(string): Fecha en formato yyyy/mm/dd. Valor por
                                   defecto None.

        Attributes:
            email(string): Email del usuario, usando como el id del mismo.
            nombre(string): Nombre del usuario.
            ultimo_acceso(string): Fecha en formato yyyy/mm/dd.
    """
    def __init__(self, email="", nombre="",
                    ultimo_acceso="", total_emails = 0):
        super(Usuario, self).__init__()
        self.email = email
        self.nombre = nombre
        self.ultimo_acceso = ultimo_acceso
        self.total_emails = total_emails

    #Métodos modificadores
    def set_email(self, email):
        self.email = email

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_ultimo_acceso(self, ultimo_acceso):
        self.ultimo_acceso = ultimo_acceso

    def set_total_emails(self, total_emails):
        self.total_emails = total_emails

    #Métodos consultores
    def get_email(self):
        return self.email

    def get_nombre(self):
        return self.nombre

    def get_ultimo_acceso(self):
        return self.ultimo_acceso

    def get_total_emails(self):
        return self.total_emails