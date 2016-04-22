# -*- coding: utf-8 -*-
import webbrowser
import httplib2

from apiclient import discovery
from oauth2client import client

#Constantes Globales
CLIENT_SECRET_FILE = 'CLASSES/client_id.json'   # Archivo de autorización
SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'    # Tipo de acceso

class Credencial():
    """
        Esta clase permite la obtención de las credenciales necesarias para
        obtener el acceso a los datos de la cuenta del usuario. Si existe una
        cuenta activa solicita los permisos, de lo contrario direcciona al
        usuario para que se auntentique en un navegador.

        Args:
            void : Esta clase no recibe argumentos.

        Attributes:
            flow : Flujo de sesión, que toma los permisos de la app y el
                   alcance de acceso de solo lectura.
            auth_uri : URL de solicitud de acceso mediante Google Auth 2.0
    """
    def __init__(self):
        super(Credencial, self).__init__()
        self.flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPE,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')

        self.auth_uri = self.flow.step1_get_authorize_url()
        webbrowser.open(self.auth_uri)

    def obtener_permisos(self, auth_code):
        """
            Permite el acceso a la cuenta de gmail del usuario, al comprobar el
            código de verificación recibido, luego de conceder los permisos.

            Args:
                auth_code (string): Código de autorización.

            Returns:
                gmail_service (Gmail API Service Object): Servicio de acceso
                a gmail, si auth_code es válido.

                bool: False, significa que no se obtuvo el permiso de acceso.
        """
        try:
            credentials = self.flow.step2_exchange(auth_code)
            http_auth = credentials.authorize(httplib2.Http())
            gmail_service = discovery.build('gmail', 'v1', http_auth)
            return gmail_service    # Retorna el servicio de acceso a la cuenta
        except client.FlowExchangeError:
            return False