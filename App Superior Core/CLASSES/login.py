# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from UI_CLASSES.win_login import Ui_win_login
from CLASSES.credencial import Credencial

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Login(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.login = Ui_win_login()
        self.login.setupUi(self)
        QtCore.QObject.connect(self.login.btAceptar, QtCore.SIGNAL('clicked()'), self.manejador_login)
        self.acceso = Credencial()
        self.permiso = None

    def manejador_login(self):
        codigo = self.login.txtCodigo.text()
        self.permiso = self.acceso.obtener_permisos(codigo)
        if self.permiso != 1:
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error',
                'El código de autenticación es incorrecto.')
            self.login.txtCodigo.clear()

    def get_permisos(self):
        return self.permiso