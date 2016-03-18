# -*- coding: utf-8 -*-
import webbrowser
import httplib2

from apiclient import discovery
from oauth2client import client

#Constantes Globales
CLIENT_SECRET_FILE = 'CLASSES/client_id.json'   # Archivo de autorización
SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'    #Tipo de acceso

class Credencial():

    def __init__(self):
        super(Credencial, self).__init__()
        self.flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPE,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')

        self.auth_uri = self.flow.step1_get_authorize_url()
        webbrowser.open(self.auth_uri)

    def obtener_permisos(self, auth_code):
        """
            obtener_permisos, permite el acceso a la cuenta de gmail, solicitando
            al usuario los permisos necesarios.

            Args:
                auth_code : código de autorización devuelto por gmail

            Returns:
                gmail_service : servicio de acceso a gmail
                1 : significa que no se obtuvo el permiso de acceso
        """
        try:
            credentials = self.flow.step2_exchange(auth_code)
            http_auth = credentials.authorize(httplib2.Http())
            gmail_service = discovery.build('gmail', 'v1', http_auth)
            return gmail_service    # Retorna el servicio de acceso a la cuenta
        except:
            return 1
