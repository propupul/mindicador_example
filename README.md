# mindicador_example
Helper class for economic indicator of the Chilean stock market

''''
This is a helper class to the Chilean economic indicator http://mindicador.cl/
using the awesome requests library you can get uf, ivp, dolar, etc.
a simple example:
>> m = Mindicador()
>> m = m.get_uf()
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
