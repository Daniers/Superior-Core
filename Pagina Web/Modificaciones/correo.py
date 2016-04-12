# vim: set fileencoding=utf-8 :
import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('correo', 'contraseña')
string_busqueda="Prueba"

type, resBusq = mail.search(None, '(ALL SUBJECT "' + string_busqueda + '")')

if resBusq[0] == '':
  print 'No se encontraron mensajes con la cadena "%s" en asunto' % (string_busqueda)
else:
  resBusq = resBusq[0].split(' ')
  print 'Se encontraron %s mensajes con la cadena "%s" en asunto' % (len(resBusq), string_busqueda)
  for num in resBusq[0].split():
    typ, resBusq = mail.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, resBusq[0][1])
mail.logout()