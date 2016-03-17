# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os
#from datetime import datetime, date, time, deltatime

from apiclient import discovery, errors
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
#CLIENT_SECRET_FILE = 'client_secret.json'
CLIENT_SECRET_FILE = 'client_id.json'
#APPLICATION_NAME = 'Gmail API Python Quickstart'
APPLICATION_NAME = 'SuperiorCore'
#EMISOR = 'juan.rey.reina@unillanos.edu.co'
#EMISOR = 'bayrondanilo92@gmail.com'
EMISOR = 'alexus142@gmail.com'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'usuario.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def ListMessagesMatchingQuery(service, user_id, query=''):
    """List all Messages of the user's mailbox matching the query.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        query: String used to filter messages returned.
        Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
        List of Messages that match the criteria of the query. Note that the
        returned list contains Message IDs, you must use get with the
        appropriate ID to get the details of a Message.
    """
    try:
        response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages
    except errors.HttpError as error:
        print ('An error occurred: %s' % error)


def consultarRecibidos(emisor=''):
    """
        Consulta el # total de mensajes recibidos de un mismo emisor.

        Args:
            emisor: email de la persona que envía el correo.
        Returns:
            Retorna un número entero, de la cantidad de correos recibidos.
    """

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    mensajes = ListMessagesMatchingQuery(service, 'me', 'from:' + emisor)

    return len(mensajes)


def consultarEnviados(destinatario=''): #issue 21
    """
        Consulta el # total de mensajes enviados a un destinatario especifico.

        Args:
            receptor: dirección de correo del destinatario

        Returns:
            Retorna un número entero, de la cantidad de correos enviados.
    """

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    mensajes = ListMessagesMatchingQuery(service, 'me', 'in:sent ' + destinatario)

    return len(mensajes)


def consultarEnviadosFecha(fechaIni, fechaFin, destinatario=''):
    """
        Consulta el # total de mensajes enviados a un destinatario especifico,
        dado un rango de fecha especifico

        Args:
            receptor: dirección de correo del destinatario
            fechaIni: Fecha inicial de busqueda emails enviados
            fechaFin: Fecha final de busqueda emails enviados.

        Returns:
            Retorna un número entero, de la cantidad de correos enviados.
    """

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    mensajes = ListMessagesMatchingQuery(service, 'me', 'in:sent after: ' +
                    fechaIni + ' before: ' + fechaFin + ' ' + destinatario)

    return len(mensajes)


# Función Principal
def main():

    print ('Receptor: bayron.ortiz@unillanos.edu.co')
    print ('Emisor: ', EMISOR)
    print ('Total Recibidos: ', consultarRecibidos(EMISOR))

    """
    print ('\nDestinatario: ', EMISOR)
    print ('Total Enviados: ', consultarEnviados(EMISOR))

    fechaIni = '2016/03/13'
    fechaFin = '2016/03/14'
    print ('\nDestinatario', EMISOR)
    print ('Entre las Fechas %s y %s' % (fechaIni, fechaFin))
    print ('Total Enviados: ', consultarEnviadosFecha(fechaIni, fechaFin, EMISOR))
    """

if __name__ == '__main__':
    main()
