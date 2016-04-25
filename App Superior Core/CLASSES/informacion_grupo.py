# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.info_grupo import Ui_info_grupo

class InformacionGrupo(QtGui.QDialog):
    """
        Clase que hacer referencia a la ventana Informacion de Grupo, que
        contiene todo lo relacionado a la información de un grupo específico.
    """
    def __init__(self, conexionDB, nombre_grupo, usuario_actual):
        super(InformacionGrupo, self).__init__()
        self.info = Ui_info_grupo()
        self.info.setupUi(self)
        self.exec_()