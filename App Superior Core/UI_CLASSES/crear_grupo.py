# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_QT/crear_grupo.ui'
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

class Ui_crear_grupo(object):
    def setupUi(self, crear_grupo):
        crear_grupo.setObjectName(_fromUtf8("crear_grupo"))
        crear_grupo.resize(283, 294)
        self.verticalLayout_2 = QtGui.QVBoxLayout(crear_grupo)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(crear_grupo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(crear_grupo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.txtNombre = QtGui.QLineEdit(crear_grupo)
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.horizontalLayout.addWidget(self.txtNombre)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(crear_grupo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.txtDescripcion = QtGui.QTextEdit(crear_grupo)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.verticalLayout.addWidget(self.txtDescripcion)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btCancelar = QtGui.QPushButton(crear_grupo)
        self.btCancelar.setObjectName(_fromUtf8("btCancelar"))
        self.horizontalLayout_2.addWidget(self.btCancelar)
        self.btCrear = QtGui.QPushButton(crear_grupo)
        self.btCrear.setObjectName(_fromUtf8("btCrear"))
        self.horizontalLayout_2.addWidget(self.btCrear)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(crear_grupo)
        QtCore.QObject.connect(self.btCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), crear_grupo.reject)
        QtCore.QMetaObject.connectSlotsByName(crear_grupo)
        crear_grupo.setTabOrder(self.txtNombre, self.txtDescripcion)
        crear_grupo.setTabOrder(self.txtDescripcion, self.btCrear)
        crear_grupo.setTabOrder(self.btCrear, self.btCancelar)

    def retranslateUi(self, crear_grupo):
        crear_grupo.setWindowTitle(_translate("crear_grupo", "Nuevo Grupo", None))
        self.label_3.setText(_translate("crear_grupo", "Nuevo Grupo", None))
        self.label.setText(_translate("crear_grupo", "Nombre:", None))
        self.label_2.setText(_translate("crear_grupo", "Descripción:", None))
        self.btCancelar.setText(_translate("crear_grupo", "Cancelar", None))
        self.btCrear.setText(_translate("crear_grupo", "Crear", None))

