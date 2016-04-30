# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.info_grupo import Ui_info_grupo
from CLASSES.grupo import Grupo

class InformacionGrupo(QtGui.QDialog):
    """
        Clase que hacer referencia a la ventana Informacion de Grupo, que
        contiene todo lo relacionado a la información de un grupo específico.
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
        self.grupo_actual = Grupo(nombre=self.nombre_grupo, descripcion="")
        grupo_descripcion = self.conexionDB.consultar_grupo(self.grupo_actual)
        usuarios_grupo = self.conexionDB.consultar_usuarios_grupo(self.grupo_actual)
        self.llenar_tabla_usuarios(usuarios_grupo)
        descripciontexto=grupo_descripcion.get_descripcion()
        self.info.txtDescripcion.setText(str(descripciontexto))
        self.info.txtGrupo.setText(str(self.nombre_grupo))

    def llenar_tabla_usuarios(self, usuarios):
        if len(usuarios) != 0:
            for item in usuarios:
                self.info.listIntegrantes.addItem(item.email)
