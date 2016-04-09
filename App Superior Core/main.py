# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys

from CLASSES.login import Login
from CLASSES.principal import Principal


# Funcion principal del programa
def main():
    """
        Función principal main de la aplicación, ejecuta la acción de
        lanzamiento de la aplicación y el entorno gráfico.
    """
    app = QtGui.QApplication(sys.argv)
    log = Login()

    if log.exec_() == QtGui.QDialog.Accepted:
        principal = Principal(log.get_permisos())
        principal.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()