# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship, Path
from py2neo import authenticate
from CLASSES.usuario import Usuario
from CLASSES.grupo import Grupo
from CLASSES.gmail_api import GmailAPI
import datetime as dt

# Ruta a Base de Datos
PATH_BASE_DATOS = "http://superiorcore:71ZRUSThCdIOO5MYikj1@superiorcore.sb02.stations.graphenedb.com:24789/db/data/"
#PATH_BASE_DATOS = "localhost:7474"
#USUARIO = "neo4j"
#PASS = "admin_neo"


class ConexionBaseDatos():
    """
        Clase que conecta a la aplicación con la base de datos. Incluye las
        tareas normales de CRUD (Crear, Leer, Actualizar, Eliminar)

        Attributes:
            graph (Graph): Objeto de la clase Py2Neo, que nos permite el acceso
                           a la base de datos para la realización de consultas.
    """
    def __init__(self):
        super(ConexionBaseDatos, self).__init__()
        #authenticate(PATH_BASE_DATOS, USUARIO, PASS)    # Solo en local autenticación
        self.graph = Graph(PATH_BASE_DATOS)       # nube
        #self.graph = Graph()

    def consultar_grupo(self, grupo):
        """
            Permite consultar a la base de datos, por un grupo específico y sus
            datos.

            Args:
                grupo(Grupo): Objeto de tipo Grupo, del que se obtiene el
                    nombre del grupo.

            Returns:
                g(Grupo): Objeto de tipo grupo en caso de que exista el grupo,
                    de lo contrario retorna None (Null).
        """
        g = None    # Objeto que guardara el grupo, si existe
        consulta = ("MATCH (g:Grupo{nombre:{N}}) RETURN g.nombre AS nombre,"
            "g.descripcion AS descripcion")

        res = self.graph.cypher.execute(consulta, {"N": grupo.get_nombre()})

        if len(res) != 0:
            g = Grupo(res[0].nombre, res[0].descripcion)    # Creamos un grupo

        return g    # Retorna el grupo

    def consultar_usuario(self, usuario):
        """
            Permite consultar a la base de datos, por un usuario específico y
            sus datos.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene
                    el email del usuario.

            Returns:
                u(Usuario): Objeto de tipo Usuario en caso de que exista el
                    usuario, de lo contrario retorna None (Null).
        """
        u = None    # Objeto que guardara el usuario si existe
        consulta = ("MATCH (u:Usuario{email:{E}}) RETURN u.email AS email,"
            "u.ultimo_acceso AS ultimo_acceso, u.total_emails AS total_emails")

        res = self.graph.cypher.execute(consulta, {"E": usuario.get_email()})

        if len(res) != 0:
            # Creamos un usuario
            u = Usuario(res[0].email, res[0].ultimo_acceso, res[0].total_emails)

        return u    # Retorna el usuario


    def consultar_grupos_usuario(self, usuario):
        """
            Permite consultar todos los grupos a los que pertenece un usuario
            determinado.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene
                    el email del usuario.

            Returns:
                grupos(list<string>): Lista que contiene los nombres de los
                    grupos a los cuales pertenece el usuario.
        """
        consulta = ("MATCH(u:Usuario{email:{E}})-->(g:Grupo) RETURN g.nombre "
                    "AS nombre")
        grupos = []
        try:
            grupos = self.graph.cypher.execute(consulta,
                    {"E": usuario.get_email()})
            return grupos
        except:
            return grupos

    def consultar_usuarios_grupo(self, grupo):
        """
            Permite consultar todos los usuarios que pertenecen a un grupo
            determinado.

            Args:
                grupo(Grupo): Objeto de tipo Grupo, del cual se obtiene
                    el nombre del grupo.

            Returns:
                usuarios(list<string>): Lista que contiene los emails de los
                    usuarios pertenecientes al grupo.
        """
        consulta = ("MATCH(g:Grupo{nombre:{E}})<-[:EN_GRUPO]-(u:Usuario) "
            "RETURN u.email AS email")
        usuarios = []
        try:
            usuarios = self.graph.cypher.execute(consulta,
                    {"E": grupo.get_nombre()})
            return usuarios
        except:
            return usuarios

    def consultar_id_usuario(self, usuario):
        """
            Esta funcion consulta el identificador único de un Usuario dentro
            de la base de datos neo4j.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene el
                    email.

            Returns:
                Integer: Retorna el id del Usuario, en caso de error o de que
                    el usuario no exista retorna un (-1).
        """
        consulta = "MATCH (u:Usuario{email:{E}}) RETURN ID(u) AS id"
        id_usr = 0

        try:
            id_usr = self.graph.cypher.execute(consulta,
                        {"E": usuario.get_email()})

            if len(id_usr) != 0:
                return id_usr[0].id
            else:
                return -1
        except:
            return -1

    def consultar_propietario_grupo(self, usuario, grupo):
        """
            Verifica si un usuario es propietario de un grupo determinado, al
            consultar la propiedad Tipo de la relación EN_GRUPO. La propiedad
            debe ser P, lo que indica que el usuario es un propietario.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene el
                    email.
                grupo(Grupo): Objeto de tipo Grupo, del cual se obtiene el
                    nombre.

            Returns:
                boolean(True|False): Si determina que el Usuario es propietario
                    del grupo entonces retorna True, de lo contrario False.
        """
        consulta = ("MATCH (u:Usuario{email:{E}}), (g:Grupo{nombre:{N}}),"
            "(u)-[r:EN_GRUPO]->(g) RETURN r.tipo AS tipo")

        res = ""
        try:
            res = self.graph.cypher.execute(consulta, {"E": usuario.get_email(),
                "N": grupo.get_nombre()})

            if res[0].tipo == "P":
                return True
            else:
                return False
        except:
            return False

    def crear_grupo(self, grupo, usuario):
        """
            Crea un grupo nuevo e inmediatamente relaciona al usuario de la
            sesión activa como propietario del grupo.

            Args:
                grupo(Grupo): Objeto de tipo Grupo, del cual se obtiene
                    el nombre del grupo.
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene
                    el email del usuario.

            Returns:
                boolean: True, en caso de que el grupo sea creado con éxito.
                         False, en caso de que el grupo no sea creado.
        """
        consulta = ("CREATE (g:Grupo{nombre:{N}, descripcion:{D}})")
        try:
            self.graph.cypher.execute(consulta,
                    {"N": grupo.get_nombre(), "D": grupo.get_descripcion()})
            self.crear_rel_usuario_grupo(usuario, grupo, "P")
            return True
        except:
            return False

    def crear_usuario(self, usuario):
        """
            Crea un nuevo usuario dentro de la base de datos.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtienen
                    c/u de los datos, accediendo a los atributos del mismo.

            Returns:
                boolean: True, creación exitosa.
                         False, no se completa la operación.
        """
        consulta = ("CREATE (u:Usuario{email:{E}, ultimo_acceso:{U},"
             "total_emails:{T}})")
        try:
            self.graph.cypher.execute(consulta,
                    {"E": usuario.get_email(), "U": usuario.get_ultimo_acceso(),
                     "T": usuario.get_total_emails()})
            return True
        except:
            return False

    def crear_rel_usuario_grupo(self, usuario, grupo, tipo):
        """
            Permite crear la relación de un usuario determinado con un grupo
            específico. La relación se nombra EN_GRUPO y contiene el atributo
            tipo: P|M , que toma los valores P:Propietario ó M:Miembro.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtienen
                    c/u de los datos, accediendo a los atributos del mismo.
                grupo(Grupo): Objeto de tipo Grupo, del cual se obtiene
                    el nombre del grupo.
                tipo(string): Específica el tipo de relación con el grupo,
                    P: Propietario ó M: Miembro.

            Returns:
                boolean: True, creación exitosa.
                         False, no se completa la operación.
        """
        consulta = ("MATCH(u:Usuario),(g:Grupo) WHERE u.email={E} AND "
            "g.nombre={N} CREATE (u)-[r:EN_GRUPO{tipo:{T}}]->(g)")

        try:
            self.graph.cypher.execute(consulta, {"E": usuario.get_email(),
                    "N": grupo.get_nombre(), "T": tipo})
            return True
        except:
            return False

    def crear_rel_usuario_usuario(self, usuario1, usuario2):
        """
            Permite crear la relación de comunicación entre los usuarios
        """
        id_usr1 = "usr" + str(self.consultar_id_usuario(usuario1))
        id_usr2 = "usr" + str(self.consultar_id_usuario(usuario2))

        consulta = ("MATCH (u1:Usuario{email:{E1}}), (u2:Usuario{email:{E2}}) "
            "CREATE (u1)-[r:COM{" + id_usr1 + ":0," + id_usr2 + ":0}]->(u2)")

        try:
            self.graph.cypher.execute(consulta, {"E1": usuario1.get_email(),
                "E2": usuario2.get_email()})
            return True
        except:
            return False

    def act_ultimo_acceso_usr(self, usuario, ultimo_acceso):
        """
            Permite la actualización de la propiedad del usuario relativa al
            ultimo_acceso llevado a cabo por el usuario en la aplicación.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene
                    el email y se actualiza la propiedad ultimo_acceso.
                ultimo_acceso(string): Hace referencia a la fecha del ultimo
                    acceso a la aplicación. Toma el formato AAAA/MM/DD.

            Returns:
                boolean: True, actualización exitosa.
                         False, no se completa la operación.
        """
        consulta = ("MATCH(u:Usuario{email:{E}}) SET u.ultimo_acceso={U}")
        try:
            self.graph.cypher.execute(consulta, {"E": usuario.get_email(),
                    "U": ultimo_acceso})
            return True
        except:
            return False

    def act_total_emails_usr(self, usuario, total_emails):
        """
            Permite la actualización de la propiedad del usuario relativa a la
            cantidad de emails en su cuenta de correo de Gmail.

            Args:
                usuario(Usuario): Objeto de tipo Usuario, del cual se obtiene
                    el email y se actualiza la propiedad total_emails.
                total_emails(integer): Número Entero, hace referencia al total
                    de emails en la cuenta de Gmail.

            Returns:
                boolean: True, actualización exitosa.
                         False, no se completa la operación.
        """
        consulta = ("MATCH(u:Usuario{email:{E}}) SET u.total_emails={T}")
        try:
            self.graph.cypher.execute(consulta, {"E": usuario.get_email(),
                        "T": total_emails})
            return True
        except:
            return False

    def agregar_usuario_grupo(self, nuevo_usuario, grupo):
        lista_emails = []
        usr_tmp2 = None

        # Consulta si existe el usuario
        usuario_tmp = self.consultar_usuario(nuevo_usuario)
        lista_emails = self.consultar_usuarios_grupo(grupo)

        if usuario_tmp is None:
            self.crear_usuario(nuevo_usuario)
        else:
            for it in lista_emails:
                if it.email == usuario_tmp.get_email():
                    return True

        self.crear_rel_usuario_grupo(nuevo_usuario, grupo, "M")

        for it in lista_emails:
            usr_tmp2 = Usuario(it.email)
            self.crear_rel_usuario_usuario(usr_tmp2, nuevo_usuario)

    def eliminar_usuario_grupo(self, usuario, grupo):
        # Consulta referente a eliminar del grupo el usuario
        consulta1 = ("MATCH (u:Usuario{email:{E}}), (g:Grupo{nombre:{N}}),"
            "(u)-[r:EN_GRUPO]->(g) DELETE r")

        # Consulta referente a eliminar la comunicación con los usuarios
        consulta2 = ("MATCH (u:Usuario{email:{E}}), (u2:Usuario{email:{E2}}),"
            "(u)-[r:COM]-(u2) DELETE r")

        try:
            self.graph.cypher.execute(consulta1, {'E': usuario.get_email(),
                    'N': grupo.get_nombre()})
            usuarios = self.consultar_usuarios_grupo(grupo)

            for it in usuarios:
                self.graph.cypher.execute(consulta2, {'E': usuario.get_email(),
                        'E2': it.email})
            return True
        except:
            return False

    def guardar_enviados_usuario(self, usuario, grupo, gmail_service):
        id_usr = ""  # Var. id usuario, destinatario emails
        lista_usr_grp = self.consultar_usuarios_grupo(grupo)  # Lista usuarios grupo
        ultimo_acceso = usuario.get_ultimo_acceso()  # Obtengo fecha ultimo acceso usuario
        gmail_api = GmailAPI()    # Objeto de tipo GmailAPI
        query = ""  # Variable Temporal consulta a gmail api
        total = 0  # Var. guarda el total enviados a un usuario
        fecha = dt.datetime.now().strftime("%Y/%m/%d")

        for it in lista_usr_grp:
            if usuario.get_email() != it.email:
                query = 'to:' + it.email + ' after:' + ultimo_acceso
                print (query)
                usr_tmp = Usuario(email=it.email)    # Usuario Temporal
                id_usr = "usr" + str(self.consultar_id_usuario(usr_tmp))
                emails_sent = gmail_api.ListMessagesMatchingQuery(gmail_service,'me', query)
                total = len(emails_sent)

                # Consulta para guardar en la base de datos
                consulta = ("MATCH (u:Usuario{email:{E}}), (u2:Usuario{email:{E2}}),"
                    "(u)-[r:COM]-(u2) SET r." + id_usr + "=r." + id_usr + "+{T}")

                self.graph.cypher.execute(consulta, {'E': usuario.get_email(),
                        'E2': it.email, 'T': total})