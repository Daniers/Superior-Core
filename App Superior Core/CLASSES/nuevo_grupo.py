# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.crear_grupo import Ui_crear_grupo
from CLASSES.grupo import Grupo


class NuevoGrupo(QtGui.QDialog):

    def __init__(self, conexionDB, usuario_actual):
        super(NuevoGrupo, self).__init__()
        self.conexionDB = conexionDB    # Obtenemos conexion base datos
        self.usr_actual = usuario_actual    # Obtenemos el usuario loggeado
        self.nuevo = Ui_crear_grupo()
        self.nuevo.setupUi(self)
        QtCore.QObject.connect(self.nuevo.btCrear, QtCore.SIGNAL('clicked()'),
                            self.crear)
        self.exec_()

    def crear(self):
        nuevo_grupo = None
        nombre = self.nuevo.txtNombre.text().lower()
        descripcion = self.nuevo.txtDescripcion.toPlainText()
        existe_grupo = None
        ok = False

        if len(nombre) != 0:
            nuevo_grupo = Grupo(nombre, descripcion)
            existe_grupo = self.conexionDB.consultar_grupo(nuevo_grupo)

            if existe_grupo is None:
                ok = self.conexionDB.crear_grupo(nuevo_grupo, self.usr_actual)
                if ok:
                    self.accept()
                    QtGui.QMessageBox.warning(self, 'informacion', 'El grupo se'
                    ' creo exitosamente.')
                else:
                    QtGui.QMessageBox.warning(self, 'Error', 'Ocurrio un '
                      'problema al crear el grupo ' + nombre + ' vuelva a '
                      'intentarlo.')
            else:
                QtGui.QMessageBox.warning(self, 'Información', ('El Grupo ' +
                     nombre + ' ya existe, pruebe con otro nombre.'))
                self.nuevo.txtNombre.clear()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Debe asignar un nombre '
                'al grupo.')