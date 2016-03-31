# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.principal import Ui_principal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Principal(QtGui.QMainWindow):

    def __init__(self, permisos, parent=None):
        super(Principal, self).__init__(parent)
        self.principal = Ui_principal()
        self.principal.setupUi(self)
        self.gmail_service = permisos
        results= self.gmail_service.users().getProfile(userId='me').execute()
        user = results.get('emailAddress',[])
        self.principal.lb_usuario.setText("Este es un Ejemplo\nUsuario: "+user)