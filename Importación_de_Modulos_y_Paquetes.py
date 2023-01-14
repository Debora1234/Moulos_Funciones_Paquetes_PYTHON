#importamos el modulo Funciones creado por nosotros
from Funciones import FUNCION

#pedimos por teclado el valor del lado y la unidad
lado_1= input("Ingrese el lado del cuadrado ")
unidad_lado_1= input("Ingrese la unidad del lado del cuadrado ")

#llamamos a la funcion, llamada FUNCION, del modulo Funciones, 
#le mandamos los valores correspondientes,  lo que recibimos lo guradamos en una variable 
resultado_funcion = FUNCION (lado_1, unidad_lado_1)
print("El resultado es: ", resultado_funcion)



#si deseamos crear un paquete, (funciones y clases; un "carpeta"), debemos poner si o si 
#un archivo vacio con el nombre __init__.py
#luego ponemos todos los modulos que deseamos que tenga esta "carpeta", y lo llamamos igual, 
#la unica diferencia es cuando lo importamos 
# import NombreCarpeta.NombreModulo from  NombreFuncion
