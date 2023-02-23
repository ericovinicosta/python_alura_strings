import re

class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.valida_url()


    def sanitiza_url(self, url):
        if(type(url)==str):
            return url.strip()
        raise ValueError('Não é possível realizar o procedimento')

    def valida_url(self):
        if(self._url == ''):
            raise ValueError('URL vazia')

        #Valida url por regex
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        url = padrao_url.match(self._url)
        if not url:
            raise ValueError('URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self._url.find('?')
        url_base = self._url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self._url.find('?')
        url_parametros = self._url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, valor_parametro):
        indice_parametro_busca = self.get_url_parametros().find(valor_parametro)
        indice_valor = indice_parametro_busca + len(valor_parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&',indice_valor)
        if(indice_e_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self._url)

    def __str__(self):
        return self._url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self._url == other._url

extrator = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
# extrator = ExtratorURL(None)
valor_quantidade = extrator.get_valor_parametro('quantidade')
moeda_destino = extrator.get_valor_parametro('moedaDestino')
if(moeda_destino.upper() == 'DOLAR'):
    print(int(valor_quantidade)*5.5)

print(valor_quantidade)
print(extrator)
print(len(extrator))
