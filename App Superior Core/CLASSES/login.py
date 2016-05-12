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
    """
        Gestiona la conexión de la aplicación con la cuenta del usuario en
        gmail, desplegando una ventana de inicio de sesión, mediante la
        solicitud del código de autenticación.

        Args:
            void : Esta clase no recibe argumentos

        Attributes:
            login (Ui_win_login): Ventana de Qt inicio de sesión.
            acceso (Credencial): Objeto que permite la obtención de las
                                 credenciales en la cuenta de gmail del usuario.
            permiso (Gmail API Service Object): Servicio de autorización de
                acceso a la cuenta.
    """
    def __init__(self):
        super(Login, self).__init__()
        self.login = Ui_win_login()
        self.login.setupUi(self)
        QtCore.QObject.connect(self.login.btAceptar, QtCore.SIGNAL('clicked()'),
                            self.manejador_login)
        self.acceso = Credencial()
        self.permiso = None

    def manejador_login(self):
        """
            Método que controla en la ventana desplegada de Login, la obtención
            del código de autenticación y la solicitud de permisos para acceder
            a los datos del usuario.

            Args:
                void : Este método no recibe argumentos

            Returns:
                void : Este método no ofrece retornos
        """
        codigo = self.login.txtCodigo.text()
        self.permiso = self.acceso.obtener_permisos(codigo)
        if False != self.permiso:
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error',
                'El código de autenticación es incorrecto.')
            self.login.txtCodigo.clear()

    def get_permisos(self):
        """
            Función consultora del atributo de clase permiso

            Args:
                void:No recibe argumentos.

            Returns:
                permiso : Servicio de autorización de acceso a la cuenta.
        """
        return self.permiso