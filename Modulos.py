
#modulos: archivos que contienen funciones o clases, ya existentes o que creamos nosotros mismos
#importamos un modulo ya existente, la libreria, datetime
import datetime
hora_actual=datetime.datetime.now()
print ("hora actual", hora_actual)

import datetime as dt #asi usamos un nombre para no usar el nombre completo de la libreria
hora_actual_2 = dt.time.min
print ("minutos actuales", hora_actual_2)

