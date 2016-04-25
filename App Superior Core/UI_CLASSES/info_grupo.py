# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_QT/info_grupo.ui'
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
        info_grupo.resize(283, 368)
        self.verticalLayout_3 = QtGui.QVBoxLayout(info_grupo)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(info_grupo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(info_grupo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.txtGrupo = QtGui.QLineEdit(info_grupo)
        self.txtGrupo.setReadOnly(True)
        self.txtGrupo.setObjectName(_fromUtf8("txtGrupo"))
        self.horizontalLayout.addWidget(self.txtGrupo)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(info_grupo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.txtDescripcion = QtGui.QTextEdit(info_grupo)
        self.txtDescripcion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.txtDescripcion.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.verticalLayout.addWidget(self.txtDescripcion)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(info_grupo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.listIntegrantes = QtGui.QListWidget(info_grupo)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listIntegrantes.setFont(font)
        self.listIntegrantes.setFrameShape(QtGui.QFrame.WinPanel)
        self.listIntegrantes.setFrameShadow(QtGui.QFrame.Raised)
        self.listIntegrantes.setAlternatingRowColors(True)
        self.listIntegrantes.setObjectName(_fromUtf8("listIntegrantes"))
        self.verticalLayout_2.addWidget(self.listIntegrantes)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btAgregar = QtGui.QPushButton(info_grupo)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAgregar.setFont(font)
        self.btAgregar.setObjectName(_fromUtf8("btAgregar"))
        self.horizontalLayout_2.addWidget(self.btAgregar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btSalir = QtGui.QPushButton(info_grupo)
        self.btSalir.setObjectName(_fromUtf8("btSalir"))
        self.horizontalLayout_3.addWidget(self.btSalir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(info_grupo)
        QtCore.QObject.connect(self.btSalir, QtCore.SIGNAL(_fromUtf8("clicked()")), info_grupo.reject)
        QtCore.QMetaObject.connectSlotsByName(info_grupo)

    def retranslateUi(self, info_grupo):
        info_grupo.setWindowTitle(_translate("info_grupo", "Información Grupo", None))
        self.label_4.setText(_translate("info_grupo", "Información de Grupo", None))
        self.label.setText(_translate("info_grupo", "Nombre:", None))
        self.label_2.setText(_translate("info_grupo", "Descripción:", None))
        self.label_3.setText(_translate("info_grupo", "Integrantes:", None))
        self.btAgregar.setText(_translate("info_grupo", "Añadir", None))
        self.btSalir.setText(_translate("info_grupo", "Salir", None))

