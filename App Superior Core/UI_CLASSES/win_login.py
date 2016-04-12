# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_login.ui'
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

class Ui_win_login(object):
    def setupUi(self, win_login):
        win_login.setObjectName(_fromUtf8("win_login"))
        win_login.resize(407, 112)
        self.verticalLayout = QtGui.QVBoxLayout(win_login)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(win_login)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.txtCodigo = QtGui.QLineEdit(win_login)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Serif"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtCodigo.setFont(font)
        self.txtCodigo.setObjectName(_fromUtf8("txtCodigo"))
        self.verticalLayout_2.addWidget(self.txtCodigo)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btCancelar = QtGui.QPushButton(win_login)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btCancelar.setFont(font)
        self.btCancelar.setObjectName(_fromUtf8("btCancelar"))
        self.horizontalLayout.addWidget(self.btCancelar)
        self.btAceptar = QtGui.QPushButton(win_login)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btAceptar.setFont(font)
        self.btAceptar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btAceptar.setToolTip(_fromUtf8(""))
        self.btAceptar.setDefault(False)
        self.btAceptar.setObjectName(_fromUtf8("btAceptar"))
        self.horizontalLayout.addWidget(self.btAceptar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(win_login)
        QtCore.QObject.connect(self.btCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), win_login.close)
        QtCore.QMetaObject.connectSlotsByName(win_login)
        win_login.setTabOrder(self.txtCodigo, self.btAceptar)
        win_login.setTabOrder(self.btAceptar, self.btCancelar)

    def retranslateUi(self, win_login):
        win_login.setWindowTitle(_translate("win_login", "SuperiorCore App Login", None))
        self.label.setText(_translate("win_login", "Ingrese Código de Auntenticación:", None))
        self.btCancelar.setText(_translate("win_login", "Cancelar", None))
        self.btAceptar.setText(_translate("win_login", "Aceptar", None))

