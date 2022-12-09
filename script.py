from test.hola.saludo import Saludo
from saludos import * #Al poner esto en vez del import total, ocupamos menos espacio de memoria
#poner * si no sabes las funciones 
from test.adios.despedida import Despedida

saludo = saludos('Channie')
saludo.saludar()
despedida = Despedida('Lee Know')
despedida.despedida()