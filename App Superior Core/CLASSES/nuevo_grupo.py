# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.crear_grupo import Ui_crear_grupo

class NuevoGrupo(QtGui.QDialog):

    def __init__(self, conexionDB, usuario_actual):
        super(NuevoGrupo, self).__init__()
        self.nuevo = Ui_crear_grupo()
        self.nuevo.setupUi(self)
        self.exec_()