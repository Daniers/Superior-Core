# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import datetime as dt
from UI_CLASSES.principal import Ui_principal
from CLASSES.informacion_grupo import InformacionGrupo
from CLASSES.nuevo_grupo import NuevoGrupo
from CLASSES.usuario import Usuario
from CLASSES.conexion_base_datos import ConexionBaseDatos
from CLASSES.grupo import Grupo

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Principal(QtGui.QMainWindow):
    """
        Clase que hace referencia a la ventana principal de la aplicación y
        todas las funciones. (Aún en desarrollo)

        Args:
            permisos (Gmail API Service Object): Servicio de autorización
                                                de acceso a la cuenta.

        Attributes:
            principal (Ui_principal): Ventana principal del entorno en Qt.
            gmail_service:Servicio de autorización de acceso a la cuenta gmail
            usr_actual(Usuario):Carga los datos del usuario de la sesión
                            actual
    """
    def __init__(self, permisos):
        super(Principal, self).__init__()
        self.principal = Ui_principal()
        self.principal.setupUi(self)
        self.gmail_service = permisos
        self.item_nombre = ""
        self.usr_actual = None
        self.conexionDB = ConexionBaseDatos()    #Creamos una conexion DB
        self.conectarSlots()    # Funcion que conecta las funciones
        self.cargar_usuario_actual()


    def conectarSlots(self):
        # Conectando Slots y Signals
        QtCore.QObject.connect(self.principal.btInfo,QtCore.SIGNAL('clicked()'),
                            self.info_grupo)
        QtCore.QObject.connect(self.principal.btNuevo,QtCore.SIGNAL('clicked()'),
                            self.nuevo_grupo)
        self.principal.listaGrupos.itemClicked.connect(self.item_seleccionado)


    def item_seleccionado(self,item):
        self.item=item
        self.item_nombre=item.text()

    def cargar_usuario_actual(self):
        results = self.gmail_service.users().getProfile(userId='me').execute()
        email = results.get('emailAddress',[])
        total_mensajes = results.get('messagesTotal',[])
        fecha = dt.datetime.now().strftime("%Y/%m/%d")
        self.usr_actual = Usuario(email=email, ultimo_acceso=fecha,
                     total_emails=total_mensajes)

        # Consulta base datos
        u = self.conexionDB.consultar_usuario(self.usr_actual)
        if u == None:
            self.conexionDB.crear_usuario(self.usr_actual)
        else:
            self.conexionDB.act_ultimo_acceso_usr(self.usr_actual, fecha)
            self.conexionDB.act_total_emails_usr(self.usr_actual,
                                        total_mensajes)
            grupos = self.conexionDB.consultar_grupos_usuario(self.usr_actual)
            self.llenar_tabla_grupos(grupos)

        self.principal.lb_usuario.setText(self.usr_actual.get_email())
        self.principal.lb_total.setText(str(self.usr_actual.get_total_emails()))

    def info_grupo(self):
        info = InformacionGrupo(self.conexionDB,self.item_nombre,self.usr_actual.get_email())
        info.show()

    def nuevo_grupo(self):    #  Pruebas
        ob = NuevoGrupo()


    def llenar_tabla_grupos(self, grupos):
        if len(grupos) != 0:
            for item in grupos:
                self.principal.listaGrupos.addItem(item.nombre)