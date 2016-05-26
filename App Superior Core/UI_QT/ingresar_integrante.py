# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresar_integrante.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ingresar_integrante(object):
    def setupUi(self, ingresar_integrante):
        ingresar_integrante.setObjectName(_fromUtf8("ingresar_integrante"))
        ingresar_integrante.resize(409, 137)
        self.label_3 = QtGui.QLabel(ingresar_integrante)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtintegrante = QtGui.QLineEdit(ingresar_integrante)
        self.txtintegrante.setGeometry(QtCore.QRect(120, 50, 231, 21))
        self.txtintegrante.setText(_fromUtf8(""))
        self.txtintegrante.setObjectName(_fromUtf8("txtintegrante"))
        self.btIntegrante = QtGui.QPushButton(ingresar_integrante)
        self.btIntegrante.setGeometry(QtCore.QRect(56, 90, 141, 23))
        self.btIntegrante.setObjectName(_fromUtf8("btIntegrante"))
        self.btCancelar = QtGui.QPushButton(ingresar_integrante)
        self.btCancelar.setGeometry(QtCore.QRect(210, 90, 151, 23))
        self.btCancelar.setObjectName(_fromUtf8("btCancelar"))
        self.label = QtGui.QLabel(ingresar_integrante)
        self.label.setGeometry(QtCore.QRect(60, 50, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ingresar_integrante)
        QtCore.QObject.connect(self.btCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), ingresar_integrante.reject)
        QtCore.QMetaObject.connectSlotsByName(ingresar_integrante)

    def retranslateUi(self, ingresar_integrante):
        ingresar_integrante.setWindowTitle(_translate("ingresar_integrante", "Ingresar Integrante", None))
        self.label_3.setText(_translate("ingresar_integrante", "Ingresar Integrante", None))
        self.btIntegrante.setText(_translate("ingresar_integrante", "Ingresar", None))
        self.btCancelar.setText(_translate("ingresar_integrante", "Cancelar", None))
        self.label.setText(_translate("ingresar_integrante", "Correo:", None))

