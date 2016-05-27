# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.info_grupo import Ui_info_grupo
from CLASSES.grupo import Grupo
from CLASSES.graficos import Graficos
from CLASSES.ingresar_integrante import IngresarIntegrante
from CLASSES.usuario import Usuario

class InformacionGrupo(QtGui.QDialog):
    """
        Clase que hacer referencia a la ventana Informacion de Grupo, que
        contiene todo lo relacionado a la información de un grupo específico.
        Args:
            conexionDB(obj): Hereda la conexion con la base de datos para consultas.
            nombre_grupo(string): Nombre del grupo seleccionado
            usuario_actual(string): usuario actual

        Attributes:
            info(Ui_info_grupo): Objeto de la clase info_grupo que permite
                                 interactuar con la interfaz de la ventana de informacion del grupo.
            grupo_actual(Grupo): Objeto que envia los datos actuales del grupo
                                        a la clase grupo y manejar los setters y getters de esta.
    """
    def __init__(self, conexionDB, nombre_grupo,usuario_actual,aux):
        super(InformacionGrupo, self).__init__()
        self.info = Ui_info_grupo()
        self.info.setupUi(self)
        self.graficos = Graficos()    # Objeto para graficar
        self.conexionDB=conexionDB
        self.nombre_grupo=nombre_grupo
        self.usuario_actual=usuario_actual
        self.aux=aux
        self.item_integrante = ""
        self.eliminar_seleccionado=None
        self.grupo_actual=None
        self.llenar_datos_grupo()
        self.listeners()
        self.permisos_crud() #Permisos para eliminar y agregar
        self.exec_()

    def permisos_crud(self):
        if self.aux is False:
            self.info.btAgregar.setEnabled(False)
            self.info.bteliminarintegrante.setEnabled(False)


    def listeners(self):
        QtCore.QObject.connect(self.info.btAgregar,QtCore.SIGNAL('clicked()'),
                            self.Agregar_integrante)
        self.info.listIntegrantes.itemClicked.connect(self.item_seleccionado)
        QtCore.QObject.connect(self.info.bteliminarintegrante,QtCore.SIGNAL('clicked()'),
                            self.Eliminar_integrante)
        QtCore.QObject.connect(self.info.btAbandonargrupo,QtCore.SIGNAL('clicked()'),
                            self.Abandonar_grupo)
        QtCore.QObject.connect(self.info.btdiagramabarras,QtCore.SIGNAL('clicked()'),
                            self.Diagrama_barras)

    def item_seleccionado(self,item):
        self.item = item
        self.item_integrante = item.text()

    def Eliminar_integrante(self):
        self.eliminar_seleccionado=Usuario(email=self.item_integrante,ultimo_acceso="", total_emails=0)
        aux = self.conexionDB.eliminar_usuario_grupo(self.eliminar_seleccionado,self.grupo_actual)
        self.info.listIntegrantes.clear()
        self.llenar_datos_grupo()

    def Abandonar_grupo(self):
        abandonar=Usuario(email=self.usuario_actual,ultimo_acceso="", total_emails=0)
        aux = self.conexionDB.eliminar_usuario_grupo(abandonar,self.grupo_actual)
        self.info.listIntegrantes.clear()
        self.llenar_datos_grupo()

    def Agregar_integrante(self):
        agregar = IngresarIntegrante(self.grupo_actual, self.conexionDB)
        self.info.listIntegrantes.clear()
        self.llenar_datos_grupo()

    def Diagrama_barras(self):
        diagrama=Usuario(email=self.item_integrante,ultimo_acceso="", total_emails=0)
        aux = self.conexionDB.consultar_enviados_usuario(diagrama,self.grupo_actual)
        m=Graficos.DiagramaDeBarras(aux)


    def llenar_datos_grupo(self):
        """
            Se encarga de cargar los datos del grupo a la interfaz de informacion del
            grupo.

            Args:
                void: no recibe atributos

            Returns: no retorna nada
        """
        self.grupo_actual = Grupo(nombre=self.nombre_grupo, descripcion="")
        grupo_descripcion = self.conexionDB.consultar_grupo(self.grupo_actual)
        usuarios_grupo = self.conexionDB.consultar_usuarios_grupo(self.grupo_actual)
        self.llenar_tabla_usuarios(usuarios_grupo)
        #otro=Otronodo(usuarios=usuarios_grupo) #ejemplo para graficar los nodos, SOLO EJEMPLO
        descripciontexto=grupo_descripcion.get_descripcion()
        self.info.txtDescripcion.setText(str(descripciontexto))
        self.info.txtGrupo.setText(str(self.nombre_grupo))

    def llenar_tabla_usuarios(self, usuarios):
        """
            Metodo que permite llenar el jlisttable con los usuarios(emails)
            pertenecientes al grupo

            Args:
                void: no recibe atributos

            Returns: no retorna nada
        """
        if len(usuarios) != 0:
            for item in usuarios:
                self.info.listIntegrantes.addItem(item.email)
