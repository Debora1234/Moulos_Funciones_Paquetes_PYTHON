#función
def FUNCION (LadoCargado, UnidadCargada):
	"""Esta funcion calcula el perimetro de un cuadrado
	Arg:
		Recibe el largo del lado(int) y la unidad (int)
	Return: 	
		Retorna el perimetro (int), unidad (int). Nos devuelve una dupla.
	"""
	perimetro=int(LadoCargado) * 4
	return (perimetro, UnidadCargada)


"""
comento todo para poder importar este módulo

# cargamos los valores para mandar a nuestra función
LadoCargado = input("carge el valor del lado del cuadrado ")
UnidadCargada = input("carge la unidad con la que midio el lado del cuadrado ")
# mostramos los valores cargados
print("lado ", LadoCargado)
print("unidad ", UnidadCargada)
# llamamos a la función,  y guardamos los valores como dupla
PerimetroCalculado = FUNCION (LadoCargado, UnidadCargada)
# muestro el resultado  
print ("Mostramos el resultado como dupla: ", PerimetroCalculado)  #los muestro usandolos como dulpa
# llamamos a la función, pero guardo los dos valores por separado
PerimetroCalculado_Valor, PerimetroCalculado_Unidad = FUNCION (LadoCargado, UnidadCargada)
# muestro el resultado  
print ("Mostramos solo el valor numerico del perimetro: ",PerimetroCalculado_Valor)  #los uso como dulpa, solo muestro el numero


"""