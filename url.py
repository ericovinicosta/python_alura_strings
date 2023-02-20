url='https://mail.google.com/mail/u/0/?inbox/FMfcgzGrcjMjjNkgnSJlzWcRCWxCptdG'

#Sanitização da URL
url = url.replace(' ','')

#Validação da URL
if url=='':
    raise ValueError('URL vazia')

#Separação dos parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

print(url_parametros)

#busca o valor no parametro
