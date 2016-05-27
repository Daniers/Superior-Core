# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.ingresar_integrante import Ui_ingresar_integrante
from CLASSES.usuario import Usuario

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class IngresarIntegrante(QtGui.QDialog):

    def __init__(self,grupo_actual,conexionDB):
        super(IngresarIntegrante, self).__init__()
        self.ingreso = Ui_ingresar_integrante()
        self.ingreso.setupUi(self)
        self.grupo_actual=grupo_actual
        self.conexionDB=conexionDB
        self.ing_integrante=None
        QtCore.QObject.connect(self.ingreso.btIntegrante, QtCore.SIGNAL('clicked()'),
                            self.Ingresar)
        self.exec_()


    def Ingresar(self):
        integrant=self.ingreso.txtintegrante.text()
        ing_integrante=Usuario(email=integrant,ultimo_acceso="", total_emails=0)
        ok = self.conexionDB.agregar_usuario_grupo(ing_integrante, self.grupo_actual)
        print(ok)
        if ok is None:
            QtGui.QMessageBox.warning(self, 'informacion', 'El Integrante se ha'
            ' ingresado exitosamente.')
        else:
            QtGui.QMessageBox.warning(self, 'Error', ' El correo ya existe, intentelo'
            ' de nuevo.')

