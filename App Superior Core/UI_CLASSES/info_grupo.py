# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_grupo.ui'
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

class Ui_info_grupo(object):
    def setupUi(self, info_grupo):
        info_grupo.setObjectName(_fromUtf8("info_grupo"))
        info_grupo.resize(370, 573)
        self.label_4 = QtGui.QLabel(info_grupo)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 177, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btSalir = QtGui.QPushButton(info_grupo)
        self.btSalir.setGeometry(QtCore.QRect(130, 530, 121, 24))
        self.btSalir.setObjectName(_fromUtf8("btSalir"))
        self.btdiagramabarras = QtGui.QPushButton(info_grupo)
        self.btdiagramabarras.setGeometry(QtCore.QRect(200, 470, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btdiagramabarras.setFont(font)
        self.btdiagramabarras.setObjectName(_fromUtf8("btdiagramabarras"))
        self.btenviados = QtGui.QPushButton(info_grupo)
        self.btenviados.setGeometry(QtCore.QRect(50, 500, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btenviados.setFont(font)
        self.btenviados.setObjectName(_fromUtf8("btenviados"))
        self.btrecibidos = QtGui.QPushButton(info_grupo)
        self.btrecibidos.setGeometry(QtCore.QRect(200, 500, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btrecibidos.setFont(font)
        self.btrecibidos.setObjectName(_fromUtf8("btrecibidos"))
        self.bteliminarintegrante = QtGui.QPushButton(info_grupo)
        self.bteliminarintegrante.setGeometry(QtCore.QRect(50, 470, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bteliminarintegrante.setFont(font)
        self.bteliminarintegrante.setObjectName(_fromUtf8("bteliminarintegrante"))
        self.btAbandonargrupo = QtGui.QPushButton(info_grupo)
        self.btAbandonargrupo.setGeometry(QtCore.QRect(200, 440, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAbandonargrupo.setFont(font)
        self.btAbandonargrupo.setObjectName(_fromUtf8("btAbandonargrupo"))
        self.label_3 = QtGui.QLabel(info_grupo)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.listIntegrantes = QtGui.QListWidget(info_grupo)
        self.listIntegrantes.setGeometry(QtCore.QRect(40, 310, 292, 114))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listIntegrantes.setFont(font)
        self.listIntegrantes.setFrameShape(QtGui.QFrame.WinPanel)
        self.listIntegrantes.setFrameShadow(QtGui.QFrame.Raised)
        self.listIntegrantes.setAlternatingRowColors(True)
        self.listIntegrantes.setObjectName(_fromUtf8("listIntegrantes"))
        self.btAgregar = QtGui.QPushButton(info_grupo)
        self.btAgregar.setEnabled(True)
        self.btAgregar.setGeometry(QtCore.QRect(50, 440, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAgregar.setFont(font)
        self.btAgregar.setObjectName(_fromUtf8("btAgregar"))
        self.label_2 = QtGui.QLabel(info_grupo)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 68, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtDescripcion = QtGui.QTextEdit(info_grupo)
        self.txtDescripcion.setGeometry(QtCore.QRect(40, 90, 291, 171))
        self.txtDescripcion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.txtDescripcion.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.txtGrupo = QtGui.QLineEdit(info_grupo)
        self.txtGrupo.setGeometry(QtCore.QRect(100, 40, 231, 20))
        self.txtGrupo.setReadOnly(True)
        self.txtGrupo.setObjectName(_fromUtf8("txtGrupo"))
        self.label = QtGui.QLabel(info_grupo)
        self.label.setGeometry(QtCore.QRect(40, 40, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(info_grupo)
        QtCore.QObject.connect(self.btSalir, QtCore.SIGNAL(_fromUtf8("clicked()")), info_grupo.reject)
        QtCore.QMetaObject.connectSlotsByName(info_grupo)

    def retranslateUi(self, info_grupo):
        info_grupo.setWindowTitle(_translate("info_grupo", "Información Grupo", None))
        self.label_4.setText(_translate("info_grupo", "Información de Grupo", None))
        self.btSalir.setText(_translate("info_grupo", "Salir", None))
        self.btdiagramabarras.setText(_translate("info_grupo", "Diagrama Barras", None))
        self.btenviados.setText(_translate("info_grupo", "Enviados", None))
        self.btrecibidos.setText(_translate("info_grupo", "Recibidos", None))
        self.bteliminarintegrante.setText(_translate("info_grupo", "Eliminar Integrante", None))
        self.btAbandonargrupo.setText(_translate("info_grupo", "Abandonar Grupo", None))
        self.label_3.setText(_translate("info_grupo", "Integrantes:", None))
        self.btAgregar.setText(_translate("info_grupo", "Añadir Integrante", None))
        self.label_2.setText(_translate("info_grupo", "Descripción:", None))
        self.label.setText(_translate("info_grupo", "Nombre:", None))

