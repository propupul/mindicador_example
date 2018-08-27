''''
This is a helper class to the Chilean economic indicator http://mindicador.cl/
using the awesome requests library you can get uf, ivp, dolar, etc.
a simple example:
>> m = Mindicador()
>> uf = m.get_uf()
>> uf
{'fecha': '2017-07-23T04:00:00.000Z', 'nombre': 'Unidad de fomento (UF)', 'codigo': 'uf',
'unidad_medida': 'Pesos', 'valor': 26624.85}
The above response is returned as a json ready object; you can use the object as a Python dictionary with {key: value}:
>> for ufs in uf:
      print("{} : {}".format(ufs, uf.get(ufs)))
fecha : 2017-07-23T04:00:00.000Z
nombre : Unidad de fomento (UF)
codigo : uf
unidad_medida : Pesos
valor : 26624.85
Note: Some -if not most- of the words in the responses are in Spanish(Chilean).
'''
import sys
import requests

class Mindicador():
 
    def __init__(self):
        if requests.get('http://mindicador.cl/api').status_code == requests.codes.ok:
            self.api_url = requests.get('http://mindicador.cl/api')
        else:
            self.bad_r = requests.get('http://mindicador.cl/api')
            sys.exit("The API request returned a {}".format(self.bad_r))

    def get_uf(self):
        api_url = self.api_url.json()
        return api_url.get('uf')
    
    def get_ivp(self):
        api_url = self.api_url.json()
        return api_url.get('ivp')
    
    def get_dolar(self):
        api_url = self.api_url.json()
        return api_url.get('dolar')

    def get_dolar_intercambio(self):
        api_url = self.api_url.json()
        return api_url.get('dolar_intercambio')

    def get_euro(self):
        api_url = self.api_url.json()
        return api_url.get('euro')

    def get_ipc(self):
        api_url = self.api_url.json()
        return api_url.get('ipc')

    def get_utm(self):
        api_url = self.api_url.json()
        return api_url.get('utm')

    def get_imacec(self):
        api_url = self.api_url.json()
        return api_url.get('imacec')

    def get_tpm(self):
        api_url = self.api_url.json()
        return api_url.get('tpm')

    def get_libra_cobre(self):
        api_url = self.api_url.json()
        return api_url.get('libra_cobre')  

    def get_tasa_desempleo(self):
        api_url = self.api_url.json()
        return api_url.get('tasa_desempleo')

    def get_bitcoin(self):
        api_url = self.api_url.json()
        return api_url.get('bitcoin')
