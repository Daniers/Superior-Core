# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_QT/principal.ui'
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

class Ui_principal(object):
    def setupUi(self, principal):
        principal.setObjectName(_fromUtf8("principal"))
        principal.resize(382, 506)
        self.centralwidget = QtGui.QWidget(principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lb_usuario = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_usuario.setFont(font)
        self.lb_usuario.setFrameShape(QtGui.QFrame.Panel)
        self.lb_usuario.setFrameShadow(QtGui.QFrame.Sunken)
        self.lb_usuario.setText(_fromUtf8(""))
        self.lb_usuario.setObjectName(_fromUtf8("lb_usuario"))
        self.horizontalLayout_4.addWidget(self.lb_usuario)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lb_total = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_total.setFont(font)
        self.lb_total.setFrameShape(QtGui.QFrame.Panel)
        self.lb_total.setFrameShadow(QtGui.QFrame.Sunken)
        self.lb_total.setText(_fromUtf8(""))
        self.lb_total.setObjectName(_fromUtf8("lb_total"))
        self.horizontalLayout_5.addWidget(self.lb_total)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.listaGrupos = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listaGrupos.setFont(font)
        self.listaGrupos.setFrameShape(QtGui.QFrame.WinPanel)
        self.listaGrupos.setFrameShadow(QtGui.QFrame.Raised)
        self.listaGrupos.setAlternatingRowColors(True)
        self.listaGrupos.setViewMode(QtGui.QListView.ListMode)
        self.listaGrupos.setObjectName(_fromUtf8("listaGrupos"))
        self.verticalLayout_2.addWidget(self.listaGrupos)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.btNuevo = QtGui.QPushButton(self.centralwidget)
        self.btNuevo.setObjectName(_fromUtf8("btNuevo"))
        self.verticalLayout.addWidget(self.btNuevo)
        self.btInfo = QtGui.QPushButton(self.centralwidget)
        self.btInfo.setObjectName(_fromUtf8("btInfo"))
        self.verticalLayout.addWidget(self.btInfo)
        self.btActualizar = QtGui.QPushButton(self.centralwidget)
        self.btActualizar.setObjectName(_fromUtf8("btActualizar"))
        self.verticalLayout.addWidget(self.btActualizar)
        self.btEliminar = QtGui.QPushButton(self.centralwidget)
        self.btEliminar.setObjectName(_fromUtf8("btEliminar"))
        self.verticalLayout.addWidget(self.btEliminar)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line.raise_()
        self.line_2.raise_()
        principal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        principal.setMenuBar(self.menubar)
        self.actionSalir = QtGui.QAction(principal)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(principal)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), principal.close)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        principal.setWindowTitle(_translate("principal", "SuperiorCore App", None))
        self.label_5.setText(_translate("principal", "Información de Login:", None))
        self.label.setText(_translate("principal", "Usuario:", None))
        self.label_3.setText(_translate("principal", "Total Emails:", None))
        self.label_2.setText(_translate("principal", "Grupos", None))
        self.label_4.setText(_translate("principal", "Opciones", None))
        self.btNuevo.setText(_translate("principal", "Nuevo", None))
        self.btInfo.setText(_translate("principal", "Ver Info.", None))
        self.btActualizar.setText(_translate("principal", "Actualizar", None))
        self.btEliminar.setText(_translate("principal", "Eliminar", None))
        self.pushButton.setText(_translate("principal", "Salir", None))
        self.menuArchivo.setTitle(_translate("principal", "Archivo", None))
        self.actionSalir.setText(_translate("principal", "Salir", None))

