# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
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
        principal.resize(640, 478)
        self.centralwidget = QtGui.QWidget(principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lb_usuario = QtGui.QLabel(self.centralwidget)
        self.lb_usuario.setGeometry(QtCore.QRect(60, 80, 471, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_usuario.setFont(font)
        self.lb_usuario.setText(_fromUtf8(""))
        self.lb_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_usuario.setObjectName(_fromUtf8("lb_usuario"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 390, 86, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        principal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        principal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        principal.setStatusBar(self.statusbar)

        self.retranslateUi(principal)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), principal.close)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        principal.setWindowTitle(_translate("principal", "SuperiorCore App", None))
        self.pushButton.setText(_translate("principal", "Salir", None))

