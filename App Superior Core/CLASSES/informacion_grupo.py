# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.info_grupo import Ui_info_grupo
from CLASSES.grupo import Grupo
from CLASSES.otronodo import Otronodo

class InformacionGrupo(QtGui.QDialog):
    """
        Clase que hacer referencia a la ventana Informacion de Grupo, que
        contiene todo lo relacionado a la información de un grupo específico.
        Args:
            conexionDB(obj): Hereda la conexion con la base de datos para consultas.
            nombre_grupo(string): Nombre del grupo seleccionado
            usuario_actual(string): usuario actual

        Attributes:
            info(Ui_info_grupo): Objeto de la clase info_grupo que permite
                                 interactuar con la interfaz de la ventana de informacion del grupo.
            grupo_actual(Grupo): Objeto que envia los datos actuales del grupo
                                        a la clase grupo y manejar los setters y getters de esta.
    """
    def __init__(self, conexionDB, nombre_grupo,usuario_actual):
        super(InformacionGrupo, self).__init__()
        self.info = Ui_info_grupo()
        self.info.setupUi(self)
        self.conexionDB=conexionDB
        self.nombre_grupo=nombre_grupo
        self.usuario_actual=usuario_actual
        self.grupo_actual=None
        self.llenar_datos_grupo()
        self.exec_()

    def llenar_datos_grupo(self):
        """
            Se encarga de cargar los datos del grupo a la interfaz de informacion del
            grupo.

            Args:
                void: no recibe atributos

            Returns: no retorna nada
        """
        self.grupo_actual = Grupo(nombre=self.nombre_grupo, descripcion="")
        grupo_descripcion = self.conexionDB.consultar_grupo(self.grupo_actual)
        usuarios_grupo = self.conexionDB.consultar_usuarios_grupo(self.grupo_actual)
        self.llenar_tabla_usuarios(usuarios_grupo)
        otro=Otronodo(usuarios=usuarios_grupo) #ejemplo para graficar los nodos, SOLO EJEMPLO
        descripciontexto=grupo_descripcion.get_descripcion()
        self.info.txtDescripcion.setText(str(descripciontexto))
        self.info.txtGrupo.setText(str(self.nombre_grupo))

    def llenar_tabla_usuarios(self, usuarios):
        """
            Metodo que permite llenar el jlisttable con los usuarios(emails)
            pertenecientes al grupo

            Args:
                void: no recibe atributos

            Returns: no retorna nada
        """
        if len(usuarios) != 0:
            for item in usuarios:
                self.info.listIntegrantes.addItem(item.email)
