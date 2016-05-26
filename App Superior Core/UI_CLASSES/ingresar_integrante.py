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
        ingresar_integrante.resize(392, 188)
        self.label_3 = QtGui.QLabel(ingresar_integrante)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(ingresar_integrante)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 60, 301, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtintegrante = QtGui.QLineEdit(self.layoutWidget)
        self.txtintegrante.setObjectName(_fromUtf8("txtintegrante"))
        self.horizontalLayout_2.addWidget(self.txtintegrante)
        self.layoutWidget_2 = QtGui.QWidget(ingresar_integrante)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 90, 331, 51))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btCancelar = QtGui.QPushButton(self.layoutWidget_2)
        self.btCancelar.setObjectName(_fromUtf8("btCancelar"))
        self.horizontalLayout_3.addWidget(self.btCancelar)
        self.btIntegrante = QtGui.QPushButton(self.layoutWidget_2)
        self.btIntegrante.setObjectName(_fromUtf8("btIntegrante"))
        self.horizontalLayout_3.addWidget(self.btIntegrante)

        self.retranslateUi(ingresar_integrante)
        QtCore.QObject.connect(self.btCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), ingresar_integrante.reject)
        QtCore.QMetaObject.connectSlotsByName(ingresar_integrante)

    def retranslateUi(self, ingresar_integrante):
        ingresar_integrante.setWindowTitle(_translate("ingresar_integrante", "Ingresar Integrante", None))
        self.label_3.setText(_translate("ingresar_integrante", "Ingresar Integrante", None))
        self.label_2.setText(_translate("ingresar_integrante", "Correo:", None))
        self.btCancelar.setText(_translate("ingresar_integrante", "Cancelar", None))
        self.btIntegrante.setText(_translate("ingresar_integrante", "Ingresar", None))

