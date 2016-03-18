# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import httplib2
from apiclient import discovery, errors

from UI_CLASSES.win_login import Ui_win_login
from UI_CLASSES.principal import Ui_principal
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


class Principal(QtGui.QMainWindow):

    def __init__(self, permisos, parent=None):
        super(Principal, self).__init__(parent)
        self.principal = Ui_principal()
        self.principal.setupUi(self)
        self.gmail_service = permisos
        results= self.gmail_service.users().getProfile(userId='me').execute()
        user = results.get('emailAddress',[])
        self.principal.lb_usuario.setText("Este es un Ejemplo\nUsuario: "+user)

# Funcion principal del programa
def main():
    app= QtGui.QApplication(sys.argv)
    log= Login()

    if log.exec_() == QtGui.QDialog.Accepted:
        principal = Principal(log.get_permisos())
        principal.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()